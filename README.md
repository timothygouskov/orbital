# orbital

**Please note - This project is a WIP and is still undergoing testing**

## Overview

Orbital is built upon the [Tekton CI/CD framework](https://tekton.dev/).

Tekton is a lightweight and flexible framework for creating CI/CD systems.

Tekton is comprised of pipelines. A pipeline is comprised of tasks. A task is set of steps (instructions) that execute things. For example, one task can use kaniko to build a docker image and push it a specified docker registry (like ghcr, Red Hat Quay, Amazon ECR, etc), and, another task can send a script to be execute a deployment manifest via ssh on a remote machine.

A tekton pipeline specifies and dicates what tasks are to be run, and, in what order. If a task inside a pipeline fails, the entire pipeline will fail and exit.

## Pipeline
Orbital's pipeline currently conists of four tasks:

1. **fetch-source** - Runs a git-clone task to clone a source-code repo into a tekton shared workspace
2. **fetch-dockerfiles** - Runs a git-clone task to clone the centralized orbital-dockerfiles into a tekton shared workspace
3. **pre-build-push** - Runs a custom task to copy over the specified language's dockerfile from the orbital-dockerfiles repo, into the source-code repo (this is all within the shared workspace).
4. **build-push** - Runs a task to build a Docker image of the source code and if successful, push it to a desired Docker image repository

