#! /bin/bash

##################################################################################
##################################################################################

NAMESPACE="tekton-orbital"

## configs
envsubst < config/docker-creds.yaml | kubectl apply -f - -n $NAMESPACE
envsubst < config/docker-sa.yaml | kubectl apply -f - -n $NAMESPACE
envsubst < config/git-creds.yaml | kubectl apply -f - -n $NAMESPACE
envsubst < config/host-creds.yaml | kubectl apply -f - -n $NAMESPACE

## tasks
kubectl apply -f tasks/pre-build-push.yaml -n $NAMESPACE

## pipeline
kubectl apply -f pipeline.yaml -n $NAMESPACE
envsubst < pipelinerun.yaml | kubectl create -f - -n $NAMESPACE

