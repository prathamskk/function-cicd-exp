# GCP Cloud Functions with GitHub Actions CI/CD

This repository contains multiple Google Cloud Functions with automated CI/CD using GitHub Actions. Each function has its own deployment configuration and will be deployed independently based on changes.

## Functions

1. **Hello World Function**
   - Simple HTTP function that returns a greeting
   - Endpoint: `/hello_world`
   - Deployment config: `functions/hello_world/deploy.yaml`

2. **Greeting Function**
   - HTTP function that returns a friendly welcome message
   - Endpoint: `/greeting`
   - Deployment config: `functions/greeting/deploy.yaml`

## Setup

1. Enable required APIs:
   ```bash
   gcloud services enable cloudfunctions.googleapis.com
   gcloud services enable cloudbuild.googleapis.com
   ```

2. Set up GitHub Secrets:
   - `GCP_PROJECT_ID`: Your Google Cloud Project ID
   - `GCP_SA_KEY`: Your Google Cloud Service Account key (JSON format)

3. Create a Service Account with the following roles:
   - Cloud Functions Developer
   - Cloud Build Service Account
   - Service Account User

## How it Works

The GitHub Actions workflow (`/.github/workflows/deploy.yml`) automatically:
1. Detects which function's code has changed
2. Deploys only the changed function(s)
3. Uses separate deployment configurations for each function

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run functions locally:
   ```bash
   functions-framework --target hello_world --debug
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