from graphene import ObjectType

from .s3_operations import MyS3status


class S3Query(MyS3status, ObjectType):
    pass