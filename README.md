# GUIDE THROUGH

In this repo, it's possible to find three different directories. Each of them represents the exercises for the two modules of Cloud Computing exam, course held by professors Giuliano Taffoni and Ruggero Lot. 
The repo is constituted by three folders:


1. __Basic__, for the first Module of Cloud Computing exam. The assignment requires the student to identify, deploy and implement a cloud-based file storage system. The system should allow users to upload, download, and delete files. Each user should have a private storage space. The system should be scalable, secure, and cost-efficient. As suggested, Nextcloud has been used to approach this problem.


2. __Advanced01__ is the directory containing the first part of the Assignment for the second module of Cloud Computing exam. The exercise intends to test the comprehension of Kubernetes environment and its resources, requiring the student to replicate the deployment performed in the Basic assignment but using Helmchart (this is the chosen option) or writing custom manifests. 


3. __Advanced02__ consists of all the files needed  to build a cluster with K3s, a light-weight version of K8s. The exercise requires to run the OSU benchmark inside the containers held by the pods that are in the nodes. The nodes talk via flannel. Two different scenarios have been performed: in the first one, the pods (launcher, worker01, worker02) are on the same node, and in the second scenario the pods are distributed between three nodes (laptophost, nodo2, nodo3).
A benchmark to evaluate the latency has been accomplished to deliver results.
