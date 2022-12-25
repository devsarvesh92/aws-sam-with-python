import sys
import subprocess
import boto3


def handler(event, context):
    text = "abc"
    print(event,context)

    with open('/tmp/abc.txt','w') as f:
        f.write('Hello from AWS Lambda using Python')

    r = subprocess.run("gpg --encrypt --batch --trust-model always --recipient qa /tmp/abc.txt",shell=True)
    print(f"Result of encryption {r}")

    s3_client = boto3.client('s3')
    
    with open("/tmp/abc.txt.gpg", "rb") as f:
        s3_client.upload_fileobj(f, "test-lamb148", "abc.gpg")
    
    return 'Hello from AWS Lambda using Python' + sys.version + '!'        