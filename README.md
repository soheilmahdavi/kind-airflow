### Create a kubernetes cluster of 1 control plane and 3 worker nodes
``` bash
kind create cluster --name airflow-cluster --config kind-cluster.yaml
```
### Check the cluster info
``` bash
kubectl cluster-info
```
### Check the nodes with kubectl
``` bash
kubectl get nodes -o wide
```
### Add the official repository of the Airflow Helm Chart
``` bash
helm repo add apache-airflow https://airflow.apache.org
```
### Update the repo
``` bash
helm repo update
```
### Create namespace airflow
``` bash
kubectl create namespace airflow
```
### Check the namespace 
``` bash
kubectl get namespaces
```
### Install the Airflow Helm Chart
``` bash
helm install airflow apache-airflow/airflow --namespace airflow --debug
```
### Get pods
``` bash
kubectl get pods -n airflow
```
### Check release
``` bash
helm ls -n airflow
```
### If for some reasons the release is stuck in pending-install or timed out
### Resinstall the chart
``` bash 
helm delete airflow --namespace airflow
helm install airflow apache-airflow/airflow --namespace airflow --debug —timeout 10m0s
```

### Port forward 8080:8080
``` bash
kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow --context kind-airflow-cluster

```
-------------------------------------------------------------------------------------------------------

``` bash
kind create cluster --name airflow-cluster --config kind-cluster.yaml
```

``` bash
kind delete cluster --name=kind
```

``` bash
IMAGE_TAG=1.0.3
docker build -t airflow-image:${IMAGE_TAG} .
docker tag airflow-image:${IMAGE_TAG} localhost:5000/airflow-image:${IMAGE_TAG}
docker push localhost:5000/airflow-image:${IMAGE_TAG}
```

``` bash
helm install airflow airflow/airflow --kube-context kind-kind   -f values.yaml
```

``` bash
helm upgrade airflow airflow/airflow   --kube-context kind-kind   -f values.yaml
```

``` bash
helm upgrade --install airflow airflow/airflow  --kube-context kind-kind -f values.yaml
```

``` bash
helm uninstall airflow --kube-context kind-kind
```