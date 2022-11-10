from pytube import YouTube
from graphene import ObjectType, String, Field, Schema
import graphene
from graphql import GraphQLError


def YouTubeDownload(url):
    link = url
    if link:
        video = YouTube(link)
        stream = video.streams.get_highest_resolution()
        stream.download()
        msg = 'success'
        return msg
    else:
        msg = 'link not exists'
        return msg

    
class YouTubeVideos(ObjectType):
    url = String(required=True)
    msg = String()


class DownloadVidoes(ObjectType):
    youtube = Field(YouTubeVideos, url=String())

    def resolve_youtube(self, info, url):
        msg = YouTubeDownload(url)
        return YouTubeVideos(
            url=url,
            msg=msg
        )