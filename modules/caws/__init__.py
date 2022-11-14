from graphene import ObjectType

from .s3_create_bucket import MyS3status
from .ec2_descrip import MyEc2Describ
from .s3_delete_bucket import MyS3DELETE
from .s3_bucketes import MyS3Bukcets

class S3Query(MyS3status, MyEc2Describ, MyS3DELETE, MyS3Bukcets, ObjectType):
    pass