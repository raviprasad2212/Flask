from graphene import ObjectType, Schema


# My webscrp module
from webscrp import WebsiteQuery
from caws import S3Query

schema = Schema(query=S3Query)