output "ec2_public_ip" {
  description = "Public IP of EC2 instance"
  value       = module.ec2_instance.public_ip
}

output "security_group_id" {
  description = "Security group ID"
  value       = aws_security_group.allow_ssh_http.id
}

output "s3_bucket_name" {
  description = "S3 bucket name"
  value       = aws_s3_bucket.logs.id
}
