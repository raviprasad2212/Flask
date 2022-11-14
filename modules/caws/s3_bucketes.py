from graphene import Field, String, ObjectType
import boto3
import logging
from botocore.exceptions import ClientError


def show_buckets():
    try:
        s3 = boto3.client('s3',
                        aws_access_key_id='AKIAWNSJ6X6ELE5LTI63',
                        aws_secret_access_key='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')

        
        response = s3.list_buckets()
        print (response)
        for bucket in response['Buckets']:
            print(bucket['Name'])
    except ClientError as a:
        logging.error(a)
        return False


class ListS3Buckets(ObjectType):
    data = String()


class MyS3Bukcets(ObjectType):
    lists3buckets = Field(ListS3Buckets)
    def resolve_lists3buckets(self, info):
        res = show_buckets()

        return ListS3Buckets(data=res)