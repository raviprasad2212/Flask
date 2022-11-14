import boto3
from botocore.exceptions import ClientError
import graphene
from graphene import Field, Schema, String, ObjectType
import logging

def s3_status():
    try:
        s3 = boto3.client('s3',
                        aws_access_key_id='AKIAWNSJ6X6ELKMYFRFV',
                        aws_secret_access_key='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')

        bucket = 'my-bucketcybage'
        s3.create_bucket(Bucket=bucket)
        if s3:
            msg = '{} Created in S3'.format(bucket)
            return msg
    except ClientError as a:
        logging.error(a)
        return False

class S3status(ObjectType):
    status = String()


class MyS3status(ObjectType):
    s3status = Field(S3status)

    def resolve_s3status(self, info):
        result = s3_status()
        print('-----------------------------',result)
        return S3status(status=result)