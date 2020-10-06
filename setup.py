"""Installation script."""

from setuptools import setup, find_packages

setup(
    name='zoho-reports',

    version='0.0.3',

    description='Simple wrapper app for embedding Zoho reports',

    author='OpenCraft GmbH',
    author_email='contact@opencraft.com',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Internet',
        'Programming Language :: Python :: 3.8',
    ],

    packages=find_packages(),
)
