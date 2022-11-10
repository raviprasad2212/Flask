from graphene import Field, String, ObjectType
import boto3
from botocore.exceptions import ClientError
import logging

def ec2_describ():
    try:
        ec2_status = boto3.client('ec2',
                            region_name='ap-south-1',
                            aws_access_key_id='AKIAWNSJ6X6ELKMYFRFV',
                            aws_secret_access_key='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')

        response = ec2_status.describe_instances()
        return response
    except ClientError as a:
        logging.error(a)
        return False

class Ec2Describ(ObjectType):
    data = String()

class MyEc2Describ(ObjectType):
    ec2describ = Field(Ec2Describ)

    def resolve_ec2describ(self, info):
        result = ec2_describ()
        return Ec2Describ(
            data = result
        )

