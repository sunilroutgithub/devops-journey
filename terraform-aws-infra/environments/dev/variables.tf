variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "ami_id" {
  description = "AMI ID for Ubuntu"
  type        = string
  default     = "ami-0ad21ae1d0696ad58"
}

variable "key_name" {
  description = "SSH key pair name"
  type        = string
  default     = "devops-key-v3"
}

variable "s3_bucket_name" {
  description = "S3 bucket name for logs"
  type        = string
  default     = "sunil-terraform-logs-2026"
}
