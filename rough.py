# import boto3

# ec2_status = boto3.client('ec2',
#                         region_name='ap-south-1',
#                         aws_access_key_id='AKIAWNSJ6X6ELKMYFRFV',
#                         aws_secret_access_key='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')

# response = ec2_status.describe_instances()
# print(response)



import boto3
# print(dir(boto3.client('ec2',region_name='ap-south-1')))
ec2 = boto3.client('ec2', 
                    region_name='ap-south-1',
                    aws_access_key_id='AKIAWNSJ6X6EADYQDQD6',
                    aws_secret_access_key='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')

instances = ec2.run_instances(
        ImageId="ami-062df10d14676e201",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="webserverhost"
    )

print(instances["Instances"][0]["InstanceId"])

