#! /bin/bash

NAMESPACE="tekton-orbital"

kubectl create namespace $NAMESPACE
kubectl delete namespace $NAMESPACE
sleep 5

#########################################################
## spin up tekton!
#########################################################
kubectl create namespace $NAMESPACE
kubectl apply -f https://api.hub.tekton.dev/v1/resource/tekton/task/git-clone/0.9/raw -n $NAMESPACE
kubectl apply -f https://api.hub.tekton.dev/v1/resource/tekton/task/kaniko/0.6/raw -n $NAMESPACE

kubectl create secret docker-registry ghcr --docker-username=$ORBITAL_DOCKER_USERNAME --docker-password=$ORBITAL_DOCKER_PASSWORD --docker-server=$ORBITAL_DOCKER_SERVER
kubectl apply -f config/docker-sa.yaml

