#### Run Local Docker registry
docker build -t my-airflow:v1 .
docker run -d --restart=always -p "127.0.0.1:5000:5000" --name registry registry:2
docker tag my-airflow:v1 localhost:5000/my-airflow:v1
curl -s http://localhost:5000/v2/_catalog


##### Install minikube

```
brew update
brew install minikube
kubectl
minikube
```

##### Create minikube cluster

```
minikube start
kubectl get nodes
minikube status
kubectl version
```

##### Delete cluster and restart in debug mode
```
minikube delete
minikube start --alsologtostderr
minikube status
```

##### Kubectl commands

```
kubectl get nodes
kubectl get pod
kubectl get services
kubectl create deployment nginx-depl --image=nginx
kubectl get deployment
kubectl get replicaset
kubectl edit deployment nginx-depl
```

##### Debugging

```
kubectl logs "INSERT POD NAME"
kubectl exec -it "INSERT POD NAME" -- bin/bash
```

##### Create mongo deployment

```
kubectl create deployment mongo-depl --image=mongo
kubectl logs mongo-depl-"INSERT POD NAME"
kubectl describe pod mongo-depl-"INSERT POD NAME"
```

##### Delete deplyoment

```
kubectl delete deployment mongo-depl
kubectl delete deployment nginx-depl
```

##### Create or edit config file

```
vim nginx-deployment.yaml
kubectl apply -f nginx-deployment.yaml
kubectl get pod
kubectl get deployment
```

##### Delete with config

```
kubectl delete -f nginx-deployment.yaml
```

##### Metrics

```
kubectl top
``` 

The kubectl top command returns current CPU and memory usage for a cluster’s pods or nodes, or for a particular pod or node if specified.
