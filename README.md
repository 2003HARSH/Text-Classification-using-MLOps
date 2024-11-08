# Text Classification using MLOps

This project demonstrates a complete MLOps pipeline for a text classification task, implementing end-to-end practices for model experimentation, tracking, and deployment. The project includes data tracking, model training, hyperparameter tuning, model registration, and automated pipeline deployment.

## Project Overview

This repository includes:
- **Experiment Tracking**: Tracks all model training runs with parameters, metrics, and artifacts in MLflow.
- **Hyperparameter Tuning**: Performs hyperparameter tuning using MLflow to log and compare performance across runs.
- **ML Pipeline with DVC**: Constructs a machine learning pipeline using DVC, tracking each stage to reproduce the best model.
- **Model Registration**: Registers the best model on MLflow, making it accessible for production.
- **Data Tracking**: Uses DVC to version and store the dataset in an Amazon S3 bucket.
- **Remote Tracking Server**: Deploys an MLflow remote tracking server on DagsHub for centralized experiment tracking.
- **Automated Pipeline Development**: Configures GitHub Actions to automate the ML pipeline, testing, and deployment processes.
- **Unit Testing**: Adds unit test cases for the Flask API, model loading, and model signature to ensure robustness.
- **Production Deployment**: Automatically promotes models to the production stage in MLflow if they pass all tests.

---

## Key Features

### 1. Experiment Tracking with MLflow
   - All experiments, including hyperparameters and metrics, are logged to an MLflow server hosted on DagsHub.
   - This helps in tracking and comparing various model runs for better reproducibility and performance analysis.

### 2. Hyperparameter Tuning
   - Used MLflow’s tracking capabilities to monitor hyperparameter tuning experiments.
   - Selected the best model configuration based on tracked metrics and stored it in the MLflow Model Registry.

### 3. ML Pipeline Creation with DVC
   - DVC (Data Version Control) is used to define and manage a structured ML pipeline.
   - Each stage, from data preprocessing to model training, is defined in DVC, ensuring reproducibility.
   - The final model is selected based on the best hyperparameter configuration and added to the DVC pipeline.

### 4. Model Registration on MLflow
   - The best-performing model from the experiments is registered in MLflow, ensuring easy access for deployment.
   - Staging and production environments are defined to manage the model lifecycle effectively.

### 5. Data Tracking with DVC and S3
   - The dataset is versioned using DVC, and files are stored in an Amazon S3 bucket.
   - This approach provides efficient data management, enabling version control and rollback if needed.

### 6. MLflow Remote Tracking Server on DagsHub
   - MLflow tracking server is deployed on DagsHub, allowing centralized and remote tracking for experiments.
   - Makes it easier to collaborate, monitor, and share experiment results.

### 7. Automated Pipeline Development with GitHub Actions
   - GitHub Actions is configured to automate the pipeline development and testing workflows.
   - Each update to the pipeline or model triggers a build-and-test process, ensuring continuous integration and delivery.

### 8. Unit Testing
   - Unit tests are added for:
     - Flask API endpoints
     - Model loading function
     - Model signature validation
   - Ensures that each component behaves as expected before deployment.

### 9. Production Deployment
   - If the model passes all test cases, it is automatically pushed to the production stage in MLflow.
   - This step automates the final promotion to production, reducing manual intervention.

---

## Project Structure

```plaintext
    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```

---

## Setup

1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/username/text-classification-mlops.git](https://github.com/2003HARSH/Text-Classification-using-MLOps.git)
   cd Text-Classification-using-MLOps.git
   ```

2. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up MLflow Remote Server** (DagsHub):
   - Follow DagsHub instructions to connect your repository and configure the MLflow server.

4. **Configure DVC with S3**:
   - Set up DVC with S3 to store and version datasets:
     ```bash
     dvc remote add -d s3remote s3://your-bucket-name/path
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

## CI/CD with GitHub Actions

GitHub Actions automates the following:

- Pipeline execution and testing
- Data tracking and artifact logging
- Model deployment to production in MLflow

**Workflow files** are stored in `.github/workflows`, where each push triggers the CI/CD pipeline.

---

## Testing

- Run unit tests locally:
  ```bash
  python -m unittest <test_file_name>.py
  ```
- GitHub Actions runs these tests automatically to ensure quality before production deployment.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

Thanks to [DagsHub](https://dagshub.com/) for remote MLflow tracking support and [Amazon S3](https://aws.amazon.com/s3/) for data storage.

---

Feel free to reach out for collaboration or to report issues!
