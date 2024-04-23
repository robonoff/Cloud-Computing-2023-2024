# Cloud Advanced 01 -  Storage System Deployment w/ K3S

This folder contains all the required files for deploying a cloud storage system using K3s, a light-weight version of K8s, 

## Prerequisites

It's necessary to have installed k3s on the machine and helmchart. 

##Steps followed to build the container

After installing k3s and helm chart - follow this [tutorial](https://helm.sh/docs/intro/install/) for helm -, run this command to pull the nexcloud helmchart:

```
helm install -f values.yaml ex1 nextcloud/nextcloud
```

This is the file with the values needed for building a cloud storage system. Modifying the options inside the [values.yaml](https://github.com/robonoff/Cloud-Computing-2023-2024/blob/main/Advanced-01/values.yaml) and enabling mariadb from false to true. The cloud storage system is deployed on Nextcloud on the page `http://localhost:8080`. 
