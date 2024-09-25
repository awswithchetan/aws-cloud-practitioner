import boto3

# Replace these with your actual access key and secret access key
ACCESS_KEY = 'your-access-key-id'
SECRET_KEY = 'your-secret-access-key'

# Replace with your desired AWS region and instance ID
REGION = 'ap-south-1'
INSTANCE_ID = 'i-1234567890abcdef0'

# Create an EC2 client using the access key and secret key
ec2_client = boto3.client(
    'ec2',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name=REGION
)

# Stop the instance
response = ec2_client.stop_instances(InstanceIds=[INSTANCE_ID])

# Print the response
print(response)
