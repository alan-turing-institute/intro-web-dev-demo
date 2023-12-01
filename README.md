# intro-web-dev-demo
A demo for the "Introduction to web development" talk

## Deploying to Azure

For a zip-based deployment via Azure cli, first authenticate:

```
az login
```

Then select your target subscription:

```
az account set -s SUSCRIPTION_ID     
```

You can check your active suscription with:

```
az account show
```

And finally deploy the ZIP file you created:

```
az webapp deploy --name APP_SERVICE --resource-group RESOURCE_GROUP --src-path ZIP_FILE
```

