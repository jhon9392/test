## This module helps to pull docker image from docker registry specified by user by reading image tag from txt file in s3 bucket

Pre-requisites:

1. Create IAM user and create credentials and save them as environment variables ref: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#environment-variables
2. IAM user should have necessary access to the bucket and its objects.
3. Python and Docker Desktop installed on the machine
4. Install boto3 and docker packages

## Steps to run:

1. Start Docker Desktop and login to registry using `docker login` command
2. run the module using command `python docker_pull.py <bucket_name> <key> <filepath>`
