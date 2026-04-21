#!/usr/bin/env python3
import boto3
import os
import glob
from datetime import datetime

BUCKET_NAME = "sunil-devops-health-logs-2026"

def list_ec2_instances():
    ec2 = boto3.client("ec2", region_name="ap-south-1")
    response = ec2.describe_instances()
    
    print("\n" + "="*50)
    print("EC2 INSTANCES AND THEIR STATES")
    print("="*50)
    
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            state = instance["State"]["Name"]
            instance_type = instance["InstanceType"]
            public_ip = instance.get("PublicIpAddress", "N/A")
            
            print(f"ID: {instance_id} | State: {state} | Type: {instance_type} | IP: {public_ip}")

def upload_health_logs():
    s3 = boto3.client("s3", region_name="ap-south-1")
    log_files = glob.glob(f"/home/{os.getenv('USER')}/logs/health_*.log")
    
    print("\n" + "="*50)
    print("UPLOADING HEALTH LOGS TO S3")
    print("="*50)
    
    for log_file in log_files:
        filename = os.path.basename(log_file)
        s3_key = f"health-logs/{filename}"
        try:
            s3.upload_file(log_file, BUCKET_NAME, s3_key)
            print(f"Uploaded: {filename}")
        except Exception as e:
            print(f"Failed: {filename} - {e}")

if __name__ == "__main__":
    print(f"Report Time: {datetime.now()}")
    list_ec2_instances()
    upload_health_logs()
    print("\nChapter 5 Complete!")
