# AWS-EB-WEB-APP

A reference project for setting up a Python Web App using AWS Elastic Beanstalk

## Use AWS EB Cli to deploy
### Prepare an Application
```shell
eb init eb-app-name --tags xxx=yyy --profile poc-default --region ap-east-1 
```

### Create New Environment
```shell
eb create eb-app-name-V1 --tags xxx=yyy --profile poc-default --region ap-east-1 
```

### Deploy Updates
```shell
eb deploy --region ap-east-1 --profile poc-default
```