# AWS-EB-WEB-APP

A reference project for setting up a Python Web App using AWS Elastic Beanstalk

## Use AWS EB Cli to deploy
### Prepare an Application
```shell
eb init eb-app-name --tags xxx=yyy,aaa=bbb --profile poc-default --region ap-east-1 
```

### Create New Environment
```shell
eb create eb-app-name-V1 --envvars WEB_CONCURRENCY=4 --tags xxx=yyy,aaa=bbb --profile poc-default --region ap-east-1 
```

### Deploy Updates
```shell
eb use V1-staging
eb deploy V1-staging [--label 1.0.0] --region ap-east-1 --profile poc-default
```
