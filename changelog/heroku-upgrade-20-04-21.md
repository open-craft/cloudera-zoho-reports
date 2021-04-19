# Heroku Upgrade

Because of [Heroku-16 End-of-Life](https://help.heroku.com/0S5P41DC/heroku-16-end-of-life-faq) we had
to migrate the reports application to be hosted to the latest heroku stack (Heroku-20).

The reports application needed a simple fix for it to be ready for the upgrade: [details here.](https://stackoverflow.com/a/51580328/858913)

The steps followed were:

- Go to https://dashboard.heroku.com/teams/opencraft-cloudera/apps
- Create new app. App-Name was set to ondemand-reports-20 and region to Europe
- Configure Heroku locally with the reports repository:
  
  - `heroku login` (credentials are [in Vault](https://vault.opencraft.com:8200/ui/vault/secrets/secret/show/core/Client%20Secrets%20:%20Cloudera%20:%20Heroku%20-%20Cloudera))
  - `heroku git:remote -a ondemand-reports-20` (confirm the heroku remote is available `git remote -v`)
  - `git push heroku master`
    
- Configure the Config Variables (Environment Variables), same as the ones on the previous app (go to
  the [app settings](https://dashboard.heroku.com/apps/ondemand-reports-20/settings) and click on 
  "Reveal Config Vars")
- Configure SSL (also in the Heroku app settings, and chose ACM)
- Add domain (also in the Heroku app settings, click on "Add domain"), set it to the same as previous 
  app (`reports.ondemand.cloudera.com`), and it returned a DNS Target. Copy the DNS Target and paste it
  to the CNAME record value in our [Route53 configuration](https://console.aws.amazon.com/route53/v2/hostedzones#ListRecordSets/Z03409678WL4QTJIZTQK)
  (we manage the `ondemand.cloudera.com` domain)
- Heroku apps come with their own PG database, so a database migration is needed, run the command
  to copy the previous database to the new one:
  
      heroku pg:copy ondemand-reports::DATABASE_URL DATABASE_URL --app ondemand-reports-20

- Delete the previous app (also done from the Heroku app settings)
