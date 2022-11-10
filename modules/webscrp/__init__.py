from graphene import ObjectType

from .my_app import MyWebsiteQuery
from .my_scrap import WebScrap
from .you_download import DownloadVidoes
from .test import MyTestOne

class WebsiteQuery(MyWebsiteQuery, WebScrap, DownloadVidoes, MyTestOne, ObjectType):
    pass