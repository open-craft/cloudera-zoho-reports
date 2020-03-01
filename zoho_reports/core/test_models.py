"""Tests for core models."""

from django.test import TestCase
from django_dynamic_fixture import G
from social_django.models import UserSocialAuth

from zoho_reports.core.models import Page, User


# pylint: disable=no-member
class UserTests(TestCase):
    """User model tests."""
    TEST_CONTEXT = {'foo': 'bar', 'baz': None}

    def test_access_token(self):
        """Test the access_token property on the custom user model."""
        user = G(User)
        self.assertIsNone(user.access_token)

        social_auth = G(UserSocialAuth, user=user)
        self.assertIsNone(user.access_token)

        access_token = 'My voice is my passport. Verify me.'
        social_auth.extra_data['access_token'] = access_token  # pylint: disable=unsupported-assignment-operation
        social_auth.save()
        self.assertEqual(user.access_token, access_token)

    def test_get_full_name(self):
        """Test that the user model concatenates first and last name if the full name is not set."""
        full_name = 'George Costanza'
        user = G(User, full_name=full_name)
        self.assertEqual(user.get_full_name(), full_name)

        first_name = 'Jerry'
        last_name = 'Seinfeld'
        user = G(User, full_name=None, first_name=first_name, last_name=last_name)
        expected = '{first_name} {last_name}'.format(first_name=first_name, last_name=last_name)
        self.assertEqual(user.get_full_name(), expected)

        user = G(User, full_name=full_name, first_name=first_name, last_name=last_name)
        self.assertEqual(user.get_full_name(), full_name)

    def test_unicode(self):
        """Verify that the model's __str__ method returns the user's full name."""
        full_name = 'Bob'
        user = G(User, full_name=full_name)
        self.assertEqual(str(user), full_name)


class PageTest(TestCase):
    """Tests for the Page model."""

    def test_allowed_emails(self):
        """Test the allowed_emails property."""
        page = G(Page, _allowed_emails="audit@example.com, Student@example.com ")
        self.assertEqual(page.allowed_emails, ["audit@example.com", "student@example.com"])

    def test_has_access(self):
        """Test that access permissions work as intended."""
        page = G(Page, _allowed_emails="audit@example.com, Student@example.com ")
        audit_user = G(User, is_staff=False, email="audit@Example.com")
        user = G(User, is_staff=False)
        staff_user = G(User, is_staff=True)
        self.assertTrue(page.has_access(audit_user))
        self.assertFalse(page.has_access(user))
        self.assertTrue(page.has_access(staff_user))
