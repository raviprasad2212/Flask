import extraction
import requests
from graphene import ObjectType, String, Field, Schema
import graphene
from graphql import GraphQLError


class MyWebsite(ObjectType):
    url = String()
    title = String()
    description = String()
    image = String()


class WebScrap(graphene.ObjectType):
    webscrp = Field(MyWebsite)

    def resolve_webscrp(self, info):
        data = {'url': 'www.mp4.org', 'title': 'myname', 'description': 'Nothing', 'image': 'image'}
        return MyWebsite(url=data['url'],
                       title=data['title'],
                       description=data['description'],
                       image=data['image'])