### Create a kubernetes cluster of 1 control plane and 3 worker nodes
  kind create cluster --name airflow-cluster --config kind-cluster.yaml

### Check the cluster info
  kubectl cluster-info

### Check the nodes with kubectl
  kubectl get nodes -o wide

### Add the official repository of the Airflow Helm Chart
  helm repo add apache-airflow https://airflow.apache.org

### Update the repo
  helm repo update

### Create namespace airflow
  kubectl create namespace airflow

### Check the namespace 
  kubectl get namespaces

### Install the Airflow Helm Chart
  helm install airflow apache-airflow/airflow --namespace airflow --debug

### Get pods
  kubectl get pods -n airflow

### Check release
  helm ls -n airflow

### If for some reasons the release is stuck in pending-install or timed out
### Resinstall the chart
``` bash 
helm delete airflow --namespace airflow
helm install airflow apache-airflow/airflow --namespace airflow --debug —timeout 10m0s
```

### Port forward 8080:8080
kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow --context kind-airflow-cluster
-------------------------------------------------------------------------------------------------------


kind create cluster --name airflow-cluster --config kind-cluster.yaml

kind delete cluster --name=kind


IMAGE_TAG=1.0.3
docker build -t airflow-image:${IMAGE_TAG} .
docker tag airflow-image:${IMAGE_TAG} localhost:5000/airflow-image:${IMAGE_TAG}
docker push localhost:5000/airflow-image:${IMAGE_TAG}

helm install airflow airflow/airflow --kube-context kind-kind   -f values.yaml
helm upgrade airflow airflow/airflow   --kube-context kind-kind   -f values.yaml
helm upgrade --install airflow airflow/airflow  --kube-context kind-kind -f values.yaml

helm uninstall airflow --kube-context kind-kind