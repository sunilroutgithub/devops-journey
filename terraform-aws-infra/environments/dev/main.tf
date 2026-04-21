terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket = "sunil-terraform-state-2026"
    key    = "dev/terraform.tfstate"
    region = "ap-south-1"
  }
}

provider "aws" {
  region = var.aws_region
}

# Security Group
resource "aws_security_group" "allow_ssh_http" {
  name        = "terraform-sg-allow-ssh-http"
  description = "Allow SSH and HTTP traffic"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "terraform-sg"
  }
}

# S3 Bucket for logs
resource "aws_s3_bucket" "logs" {
  bucket = var.s3_bucket_name
}

resource "aws_s3_bucket_versioning" "logs" {
  bucket = aws_s3_bucket.logs.id
  versioning_configuration {
    status = "Enabled"
  }
}

# EC2 Instance using module
module "ec2_instance" {
  source = "../../modules/ec2"

  instance_type      = var.instance_type
  ami_id             = var.ami_id
  security_group_id  = aws_security_group.allow_ssh_http.id
  key_name           = var.key_name
}
