# AWS S3 Lab Guide - Image Storage and Public Access

## Lab Overview

1. Create an S3 bucket using AWS Console
2. Upload images and make them publicly accessible
3. Use Python SDK (boto3) to interact with S3 programmatically

## Prerequisites

- AWS Account with appropriate permissions


---

## Part 1: AWS Console (GUI) Approach

### Step 1: Create an S3 Bucket

1. **Login to AWS Console**
    
    - Go to https://aws.amazon.com/console/
    - Sign in with your AWS credentials
2. **Navigate to S3 Service**
    
    - In the AWS Console, search for "S3" in the search bar
    - Click on "S3" service
3. **Create New Bucket**
    
    - Click "Create bucket"
    - **Bucket name**: Choose a globally unique name (e.g., `student-demo-images-2025-yourname`)
    - **Region**: Select your preferred region (e.g., us-east-1)
    - **Object Ownership**: Select "ACLs enabled"
    - **Block Public Access settings**: UNCHECK "Block all public access" (⚠️ Important for public access)
    - Check the acknowledgment box
    - Click "Create bucket"

### Step 2: Configure Bucket for Public Access

1. **Open Your Bucket**
    
    - Click on your newly created bucket name
2. **Set Bucket Policy**
    
    - Go to "Permissions" tab
    - Scroll down to "Bucket policy"
    - Click "Edit"
    - Paste the following policy (replace `YOUR-BUCKET-NAME` with your actual bucket name):

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME/*"
        }
    ]
}
```

3. **Save Policy**
    - Click "Save changes"

### Step 3: Upload Images

1. **Upload Files**
    
    - Go to "Objects" tab in your bucket
    - Click "Upload"
    - Click "Add files" and select 2-3 sample images
    - Click "Upload"
2. **Make Objects Public**
    
    - After upload, select each uploaded image
    - Click "Actions" → "Make public using ACL"
    - Confirm by clicking "Make public"
3. **Get Public URLs**
    
    - Click on each image name
    - Copy the "Object URL" - this is your public link
    - Test the URL in a new browser tab