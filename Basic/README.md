## Cloud Basic - Storage System Deployment 

This folder drafts the required steps for deploying a cloud storage system using Docker. It exploits features from MySQL for the database, Nextcloud for the file storage and Locust for the load testing and benchmarking. 

## Prerequisites

Docker and Docker compose must be necessarly installed on your machine. A basic understanding of containerization with Docker, then Docker Compose, YAML syntax, python and virtual environments. 

## Steps followed to build the container

1. After creating the [docker-compose.yaml](https://github.com/robonoff/Cloud-Computing-2023-2024/blob/main/Basic/docker-compose.yaml) into a specific folder with a name of your preference (in my case was cloud_base), run this command in the terminal being in this folder:

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
Open the port #http://localhost:8081/ on the your favorite browser, and the storage service will be available. To create all of the users, download [create_nextcloud_users.sh](https://github.com/robonoff/Cloud-Computing-2023-2024/blob/main/Basic/create_nextcloud_users.sh), and run the following commands:
###
###
```
sudo chmod +x ./create_nextcloud_users.sh
##
./create_nextcloud_users.sh
```

