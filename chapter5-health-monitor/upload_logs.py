import boto3
import os
import glob
from datetime import datetime

# S3 bucket name
BUCKET_NAME = "sunil-devops-health-logs-2026"

def upload_logs():
    s3 = boto3.client("s3", region_name="ap-south-1")
    
    # Find all log files
    log_files = glob.glob(f"/home/{os.getenv('USER')}/logs/health_*.log")
    
    if not log_files:
        print("No log files found!")
        return
    
    for log_file in log_files:
        filename = os.path.basename(log_file)
        s3_key = f"health-logs/{filename}"
        
        try:
            s3.upload_file(log_file, BUCKET_NAME, s3_key)
            print(f"✅ Uploaded: {filename} → s3://{BUCKET_NAME}/{s3_key}")
        except Exception as e:
            print(f"❌ Failed: {filename} → {e}")

if __name__ == "__main__":
    print(f"Starting upload at {datetime.now()}")
    upload_logs()
    print("Done!")
