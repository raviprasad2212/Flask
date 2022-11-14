from graphene import Field, String, ObjectType
import boto3
from botocore.exceptions import ClientError
import logging


def s3_delete(bucket_name):
    try:
        s3 = boto3.client('s3',
                        aws_access_key_id='AKIAWNSJ6X6ELKMYFRFV',
                        aws_secret_access_key='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')

        # bucket = 'my-bucketcybage'
        print(dir(bucket_name))
        resp = s3.delete_bucket(Bucket=bucket_name)
        print(dir(resp))
        
        if s3:
            msg = '{} delete in S3'.format(bucket_name)
            return msg
    except ClientError as a:
        logging.error(a)
        return False

class S3BucketDelete(ObjectType):
    bucket_name = String(required=True)


class MyS3DELETE(ObjectType):
    S3bucketdelete = Field(S3BucketDelete, bucket_name=String())


    def resolve_S3bucketdelete(self, info, bucket_name):
        delt = s3_delete(bucket_name)
        return S3BucketDelete(bucket_name = delt)
