import boto3
import docker
import logging

#basic logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def read_s3(bucket_name, key, file_path):
    
    #creating a resource representing Amazon Simple Storage Service (S3) Bucket
    s3 = boto3.resource('s3')
    #ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.download_file
    s3.Bucket(bucket_name).download_file(key, file_path)
    with open(file_path) as f:
        for line in f:
            #reading each line and pulling docker image respectively
            repo, tag = (line.split(':'))
            logging.info('pulling %s with tag %s', repo, tag)
            docker_pull(repo, tag)

def docker_pull(repository, tag):
    
    try:
        #creating docker client ref:https://docker-py.readthedocs.io/en/stable/client.html#docker.client.from_env
        docker_client = docker.from_env()
        #ref: https://docker-py.readthedocs.io/en/stable/images.html#docker.models.images.ImageCollection.pull
        image = client.image.pull(repository=repository, tag=tag)
    except Exception as e:
        logging.info('error while pulling docker image with exception: %s', e)

#pass in s3 parameters        
read_s3('', '', '')
