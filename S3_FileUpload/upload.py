import os
import boto3

client=boto3.client('s3')

#set_variables
bucket='s3-osk-bucket-3000'
curr_path=os.getcwd()
file='test.txt'
filename=os.path.join(curr_path,'data',file)

#open the file
data=open(filename,'rb')

#load data into s3
client.upload_file(filename,bucket,file)