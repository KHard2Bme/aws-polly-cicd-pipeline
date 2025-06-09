# AWS Polly CI/CD Pipeline

This project converts text to speech using Amazon Polly and uploads the result to S3 using GitHub Actions.

## 🔧 Setup

1. Create an S3 bucket, a folder as an object within and the necessary bucket policy
2. Create an IAM user with both Polly + S3 permissions
3. Use environment variables for all sensitive info required in python code(no hardcoded secrets).
   Added these to GitHub secrets:
   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_REGION
   - S3_BUCKET_NAME

## 📝 Modify Text

- Edit the "speech.txt" file with the content you want Polly to speak. 
- Once done, select "Commit changes"

## 🔁 Trigger Workflows

  [ on_pull_request ]

 After selecting "Commit changes":
- Create a commit message and then select "Create a new branch for this commit and start a pull request":
  a branch name will be auto-generated.
- Next select "Propose changes"
- Now select "Create pull request"; you should see message "Convert Text to Speech - Beta/synthesize-and-upload-beta (pull_request) successful.

 [ on_merge ]

- This is setup for manual approval.
- You can check the "Merge without waiting for requirements to be met (bypass rules)"
- Select "Bypass rules and merge pull request" 
- Select "Confirm bypass rules and merge
- You should see a "Pull request successfully merged and closed."


## ✅ Check Output

- Go to Amazon S3 and select general purpose buckets.
- Within listing, select S3 bucket "pixel-learning-polly-s3".
- You will next see folder named polly-audio/, within this folder you will see both beta.mp3 and prod.mp3 files.
- You can download the .mp3 files to your local computer and play them to hear audio.



