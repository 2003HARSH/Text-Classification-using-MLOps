# Text Classification using MLOps

This project demonstrates a complete MLOps pipeline for a text classification task, implementing end-to-end practices for model experimentation, tracking, packaging, and deployment. The project incorporates advanced features such as AWS CodeDeploy for automated blue-green deployment and AWS Elastic Container Registry (ECR) for model storage. To ensure scalability, reliability, and fault tolerance, it also utilizes **AWS Auto Scaling Groups (ASGs)**, **Load Balancers**, and **Launch Templates**.

---

## Project Overview

This repository includes:
- **Experiment Tracking**: Logs all training runs with parameters, metrics, and artifacts in MLflow.
- **Hyperparameter Tuning**: Uses MLflow to log and compare performance during hyperparameter optimization.
- **ML Pipeline with DVC**: Structures and manages machine learning pipelines, ensuring reproducibility.
- **Model Registration**: Registers the best-performing models for deployment using MLflow.
- **Data Versioning**: Tracks and versions datasets with DVC, storing them in Amazon S3.
- **Remote Experiment Tracking**: Hosts a centralized MLflow tracking server on DagsHub.
- **Automated CI/CD Pipelines**: Leverages GitHub Actions to automate testing, pipeline execution, and deployment.
- **Unit Testing**: Validates API endpoints, model loading, and configurations to ensure robust deployments.
- **AWS CodeDeploy with Blue-Green Deployment**: Deploys the application using AWS CodeDeploy to minimize downtime.
- **AWS ECR Integration**: Stores and retrieves Docker images for deployment.
- **Production Deployment**: Automates testing and model promotion to production, ensuring deployment readiness.
- **Scalability Features**:
  - **Auto Scaling Groups (ASGs)**: Automatically adjusts the number of EC2 instances based on traffic and system load.
  - **Load Balancers**: Distributes traffic evenly across instances to ensure high availability and fault tolerance.
  - **Launch Templates**: Defines instance configurations for easy scaling and reproducibility.

---

## Key Features

### 1. **Experiment Tracking with MLflow**
   - Logs all experiments, hyperparameters, metrics, and artifacts to an MLflow server hosted on DagsHub.
   - Simplifies comparison and selection of the best-performing models.

### 2. **Hyperparameter Tuning**
   - Uses MLflow’s tracking capabilities for hyperparameter tuning.
   - Tracks each experiment run and selects the best configuration for deployment.

### 3. **Structured ML Pipeline with DVC**
   - Employs DVC to define and manage an end-to-end ML pipeline from data ingestion to model training.
   - Tracks all pipeline stages, ensuring reproducibility and efficient updates.

### 4. **Model Registration in MLflow**
   - Registers the best-performing models to MLflow Model Registry.
   - Supports staging and production environments for model lifecycle management.

### 5. **Data Versioning with DVC and S3**
   - Tracks data changes and stores datasets securely in an Amazon S3 bucket.
   - Allows easy rollback and version comparison for datasets.

### 6. **Scalable Deployment with AWS**
   - **Auto Scaling Groups (ASGs)**:
     - Dynamically adjusts the number of EC2 instances based on predefined scaling policies (e.g., CPU usage, memory usage).
     - Ensures cost efficiency by scaling down during low traffic and scaling up during peak traffic.
   - **Load Balancers**:
     - Elastic Load Balancer (ELB) ensures that incoming traffic is evenly distributed across all running instances.
     - Provides fault tolerance by automatically routing traffic away from unhealthy instances.
   - **Launch Templates**:
     - Predefined configurations for EC2 instances, including AMIs, instance types, security groups, and networking settings.
     - Simplifies instance management and ensures consistency across scaling operations.

### 7. **Automated Deployment with AWS CodeDeploy**
   - Implements blue-green deployment for seamless updates to Auto Scaling Groups (ASGs) behind a load balancer.
   - Ensures minimal downtime and safe transitions between application versions.

### 8. **Integration with AWS ECR**
   - After passing all tests, Docker images are built and pushed to AWS Elastic Container Registry (ECR).
   - CodeDeploy pulls these images for deployment to ASGs.

### 9. **CI/CD with GitHub Actions**
   - Automates the workflow for testing, building, and deploying updates.
   - Triggers deployment only after passing all unit tests and validations.

### 10. **Unit Testing**
   - Comprehensive unit tests for:
     - Flask API endpoints
     - Model loading
     - Model signature validation
   - Ensures reliability before deployment.

---

## Deployment Workflow

1. **Build and Push to AWS ECR**:
   - After successful testing, the application is containerized using Docker.
   - The Docker image is pushed to AWS ECR for centralized storage.

2. **Automated Deployment**:
   - AWS CodeDeploy retrieves the Docker image from ECR.
   - Deploys the application to ASGs using blue-green deployment to minimize downtime.
   - Load balancers ensure high availability, routing traffic only to healthy instances.

3. **Scaling and Traffic Management**:
   - ASGs adjust the number of instances based on traffic patterns.
   - Load balancers handle incoming requests and distribute them to available instances, ensuring optimal performance.

4. **Continuous Integration/Delivery**:
   - GitHub Actions automatically trigger the deployment pipeline on new commits.

---

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/2003HARSH/Text-Classification-using-MLOps.git
   cd Text-Classification-using-MLOps
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up AWS Services**:
   - **Auto Scaling Groups (ASGs)**: Define scaling policies for EC2 instances.
   - **Load Balancers**: Configure ELB to distribute traffic across instances.
   - **Launch Templates**: Create templates for consistent instance configurations.

4. **Configure AWS CodeDeploy**:
   - Set up a CodeDeploy application with blue-green deployment using ASGs and a load balancer.

5. **Push Docker Image to ECR**:
   ```bash
   aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account_id>.dkr.ecr.<region>.amazonaws.com
   docker build -t text-classification .
   docker tag text-classification:latest <account_id>.dkr.ecr.<region>.amazonaws.com/text-classification:latest
   docker push <account_id>.dkr.ecr.<region>.amazonaws.com/text-classification:latest
   ```

---

## Usage

1. **Run the ML Pipeline**:
   - Execute the pipeline defined in `dvc.yaml`:
     ```bash
     dvc repro
     ```

2. **Experiment Tracking**:
   - Start and track experiments using MLflow:
     ```python
     import mlflow
     mlflow.start_run()
     ```

3. **Hyperparameter Tuning**:
   - Use hyperparameter tuning code within `mlflow_experiment/` to find the best model.

4. **Deploy Model**:
   - Deploy the final model after passing all tests:
     ```bash
     dvc push  # Pushes tracked data to S3
     ```

---

## Testing

- Run unit tests locally:
  ```bash
  python -m unittest <test_file_name>.py
  ```
- CI/CD workflows execute these tests automatically.

---

## Future Enhancements

1. **Enhanced Deployment**:
   - Deployment of the application using AWS Elastic Container Service (ECS) for scaling and fault tolerance.
   - Further integration with AWS CodePipeline to orchestrate the end-to-end deployment process.

2. **Model Monitoring**:
   - Integration of tools for monitoring model performance in production and detecting drift.

---

## Contact

Feel free to reach out at [harshnkgupta@gmail.com](harshnkgupta@gmail.com) or create an issue in the repository for questions or collaboration opportunities!
