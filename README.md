# randomNumberPod

## Deploy
### 1. Clone the repositories:
```sh
git clone https://github.com/hydrokhoos/randomNumberPod.git
```

### 2. Deploy the pod:
```sh
cd randomNumberPod
kubectl apply -f randomNumPod.yaml
```

## Usage
### Request random number:
```sh
kubectl exec -it random-number-pod -c sidecar -- ndnpeek -fp /randomNum; echo ""
```

## Undeploy
```sh
kubectl delete -f randomNumPod.yaml
```
