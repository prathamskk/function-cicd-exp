# GCP Cloud Functions with GitHub Actions CI/CD

This repository contains multiple Google Cloud Functions with automated CI/CD using GitHub Actions. Each function has its own deployment configuration and will be deployed independently based on changes.

## Functions

1. **Hello World Function**
   - Simple HTTP function that returns a greeting
   - Endpoint: `/hello_world`
   - Deployment config: `functions/hello_world/deploy.yaml`
   - Runtime: Python 3.11

2. **Greeting Function**
   - HTTP function that returns a friendly welcome message
   - Endpoint: `/greeting`
   - Deployment config: `functions/greeting/deploy.yaml`
   - Runtime: Python 3.11

## Setup

1. Enable required APIs:
   ```bash
   gcloud services enable cloudfunctions.googleapis.com
   gcloud services enable cloudbuild.googleapis.com
   ```

2. Create a Service Account and download the key:
   ```bash
   # Create a service account
   gcloud iam service-accounts create github-actions-deployer \
     --display-name="GitHub Actions Deployer"

   # Grant necessary roles
   gcloud projects add-iam-policy-binding $PROJECT_ID \
     --member="serviceAccount:github-actions-deployer@$PROJECT_ID.iam.gserviceaccount.com" \
     --role="roles/cloudfunctions.developer"
   
   gcloud projects add-iam-policy-binding $PROJECT_ID \
     --member="serviceAccount:github-actions-deployer@$PROJECT_ID.iam.gserviceaccount.com" \
     --role="roles/cloudbuild.builds.builder"

   gcloud projects add-iam-policy-binding $PROJECT_ID \
     --member="serviceAccount:github-actions-deployer@$PROJECT_ID.iam.gserviceaccount.com" \
     --role="roles/logging.logWriter"

   # Create and download the key
   gcloud iam service-accounts keys create key.json \
     --iam-account=github-actions-deployer@$PROJECT_ID.iam.gserviceaccount.com
   ```

3. Set up GitHub Secrets:
   - `GCP_PROJECT_ID`: Your Google Cloud Project ID
   - `GCP_SA_KEY`: The entire contents of the `key.json` file you downloaded

## How it Works

The GitHub Actions workflow (`/.github/workflows/deploy.yml`) automatically:
1. Detects which function's code has changed
2. Deploys only the changed function(s)
3. Uses separate deployment configurations for each function

## Local Development

1. Install dependencies for each function:
   ```bash
   # For hello_world function
   cd functions/hello_world
   pip install -r requirements.txt

   # For greeting function
   cd functions/greeting
   pip install -r requirements.txt
   ```

2. Run functions locally:
   ```bash
   # For hello_world function
   cd functions/hello_world
   functions-framework --target hello_world --debug

   # For greeting function
   cd functions/greeting
   functions-framework --target greeting --debug
   ```

## Testing

To test the functions locally:

1. Hello World:
   ```bash
   curl http://localhost:8080
   ```

2. Greeting:
   ```bash
   curl http://localhost:8080
   ```

## Deployment

Functions are automatically deployed when changes are pushed to the main branch. The deployment is selective:
- Changes to `functions/hello_world/**` will only deploy the hello world function
- Changes to `functions/greeting/**` will only deploy the greeting function
- Changes to shared files (like `requirements.txt`) will trigger deployment of all functions 