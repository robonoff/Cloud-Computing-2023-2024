# Cloud Basic - Storage System Deployment w/ Docker

This directory drafts the required steps for deploying a cloud storage system using Docker. It exploits features from MySQL for the database, Nextcloud for the file storage and Locust for the load testing and benchmarking. 

## Prerequisites

Docker and Docker compose. A basic understanding of containerization with Docker, then Docker Compose, YAML syntax, python and virtual environments. 

## Steps followed to build the container

1. After creating the [docker-compose.yaml](https://github.com/robonoff/Cloud-Computing-2023-2024/blob/main/Basic/docker-compose.yaml) into a specific directory with a name of your preference (in my case was cloud_base), run this command in the terminal while in this directory:

###
###
```

docker-compose up

```
###
###
This is going to deploy containers using Docker Compose. To check the status of your containers, run the command:
###
###
```

docker ps -a

```
###
###
###
Open the page `http://localhost:8081` on your favorite browser, and the storage service will be available. To create all of the users, download [create_nextcloud_users.sh](https://github.com/robonoff/Cloud-Computing-2023-2024/blob/main/Basic/create_nextcloud_users.sh), and run the following commands in the terminal:
###
###
```
sudo chmod +x ./create_nextcloud_users.sh
./create_nextcloud_users.sh
```
###
###
###

After creating the users, create another directory, calling it locust, and then install `locust` in a virtual environment. After creating or downloading the [test.py](https://github.com/robonoff/Cloud-Computing-2023-2024/blob/main/Basic/locust/test.py), and also all the files used for the test (inej.jpg, UnderstandingDeepLearning.pdf, largefile), run this command in the terminal (make sure the virtual environment is activated):

```
locust -f test.py
```

In this way, the locust can be opened on the browser on the page `http://localhost:8089/`, where the benchmarking to check the latency and the load testing will be shown. 

