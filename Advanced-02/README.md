## Cloud Advanced 01 - (MPI @ Kubernetes)

The exercise requires to run the OSU benchmark inside the containers holded by the pods that are in the nodes. The nodes talk via flannel. Two different scenarios have been performed: in the first one, the pods (launcher, worker01, worker02) are on the same node, and in the second scenario the pods are distributed between three nodes (laptophost, nodo2, nodo3). 
A benchmark to evaluate the latency has been accomplished to deliver results.
The exercise addresses the task of porting simple HPC workflows into Kubernetes by testing the student proficiency and capabilities not only in Kubernetes but also with Docker and HPC workflows. The student is required to create a container with the [OSU Benchmark](https://mvapich.cse.ohio-state.edu/benchmarks/.). The container must have a behavior as expected by the operator. 

## Prerequisites

Make sure to have any Kubernetes distribution on the machine (in this case, k3s, a light-weight version of k8s). 
Gnome Boxes, Virtual Machine Manager have been used to create the nodes and manage them. 
Basic understanding of .yaml, Docker, .xml. 

## Steps followed

After setting the entire cluster, to serve the purpose of performing benchmark tests to evaluate the latency, [MPI operator](https://github.com/kubeflow/mpi-operator) has been applied to a cluster composed by one launcher node and two workers nodes. 
For installing the MPI operator on the entire cluster, run this command: 
```
kubectl apply con il link sudo kubectl apply -f https://raw.githubusercontent.com/kubeflow/mpi-operator/v0.4.0/deploy/v2beta1/mpi-operator.yaml
```

Create or download the [DockerFile](https://github.com/robonoff/Cloud-Computing-2023-2024/blob/main/Advanced-02/Dockerfile), in which the MPI operator osu benchmark has been inserted, to build then the container image locally though the following command:
```
docker build -f Dockerfile -t osuimage .
```
In this way, there is a local image of the osu-benchmark. The next step is to create the .yaml files so that the images will be used to create the containers inside the pods on the nodes. This step needs to be done manually on every node, not only on the master, unfortunately.
The two files are:

1. [onenode.yaml](https://github.com/robonoff/Cloud-Computing-2023-2024/blob/main/Advanced-02/onenode.yaml). distributes the pods on the same node. 
2. [twonodes.yaml](https://github.com/robonoff/Cloud-Computing-2023-2024/blob/main/Advanced-02/twonodes.yaml), distributes the pods on two different nodes.

To run these two files, use this command: 

```
sudo kubectl apply -f onenode.yaml
sudo kubectl apply -f twonodes.yaml
```
To retrieve the name of the pods, it's possible to use: 
```
sudo kubectl get pods
```

Two benchmarking files with the latency results are provided: 

* [benchmark_onenode](https://github.com/robonoff/Cloud-Computing-2023-2024/blob/main/Advanced-02/benchmark_onenode.txt)
* [benchmark_twonodes](https://github.com/robonoff/Cloud-Computing-2023-2024/blob/main/Advanced-02/benchmark_twonodes.txt)

  

