from graphene import ObjectType

from .s3_operations import MyS3status
from .ec2_descrip import MyEc2Describ


class S3Query(MyS3status, MyEc2Describ, ObjectType):
    pass