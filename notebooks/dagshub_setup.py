import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/2003HARSH/Text-Classification-using-MLOps.mlflow')

dagshub.init(repo_owner='2003HARSH', repo_name='Text-Classification-using-MLOps', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)