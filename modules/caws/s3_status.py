# from graphene import ObjectType, String, Field, Schema
# import graphene
# from graphql import GraphQLError
# import boto3

# s3 = boto3.resource('s3',
#     aws_access_key_id='AKIAWNSJ6X6ELKMYFRFV',
#     aws_secret_access_key='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'
# )
# p = boto3.client('s3')
# rs = p.list_objects(
#     Bucket='string',
#     Delimiter='string',
#     EncodingType='url',
#     Marker='string',
#     MaxKeys=123,
#     Prefix='string',
#     RequestPayer='requester'
# )
# print(rs)
# # for bucket in s3.buckets.all():
# #     print(bucket.name)
# # https://project1cy.s3.ap-south-1.amazonaws.com/Flask/



import boto3

s3 = boto3.client('s3',
                aws_access_key_id='AKIAWNSJ6X6ELKMYFRFV',
                aws_secret_access_key='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')

print(s3)
s3.create_bucket(Bucket='my-bucketcybage')