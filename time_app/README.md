# Sample Time Application

This Flask application returns the current UTC time at `GET /time`. It is the completed application for Lab 2, Problem 2.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
curl http://127.0.0.1:8080/time
```

## Test

```bash
python -m unittest discover -s tests -v
```

## Build and run with Docker

Replace `DOCKERHUB_USERNAME` with your Docker Hub username.

```bash
docker build -t DOCKERHUB_USERNAME/sample-time-app:latest .
docker run --rm --name sample-time-app -p 8080:8080 DOCKERHUB_USERNAME/sample-time-app:latest
curl http://127.0.0.1:8080/time
```

## Push to Docker Hub

```bash
docker login
docker push DOCKERHUB_USERNAME/sample-time-app:latest
```

## Deploy to Kubernetes

Update the image name in `k8s/deployment.yaml`, then run:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl rollout status deployment/sample-time-app
kubectl get pods,services -l app=sample-time-app
```

For Minikube:

```bash
minikube service sample-time-app --url
```

For any Kubernetes cluster, port forwarding also verifies the deployment:

```bash
kubectl port-forward service/sample-time-app 8080:8080
curl http://127.0.0.1:8080/time
```

## GitHub submission

The lab requires this directory to be named `time_app`. Commit the complete directory to a GitHub repository, then place the repository URL in the report submitted through NYU Brightspace.
