#! /bin/bash

#######################################################################################
## install tekton cli!
#######################################################################################

VERSION="v0.31.0"
sudo apt update && sudo apt install uuid ## assumption is debian/ubuntu
UUID=$(uuid)

cd /tmp && mkdir -p $UUID && cd $UUID

curl -L -O https://github.com/tektoncd/cli/releases/download/v0.31.0/tektoncd-cli-0.31.0_Linux-64bit.deb
sudo dpkg -i tektoncd-cli-0.31.0_Linux-64bit.deb
sleep 1
tkn --help && cd .. && rm -R $UUID

#######################################################################################
## spin up tekton!
#######################################################################################
kubectl apply --filename https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml
kubectl apply --filename https://storage.googleapis.com/tekton-releases/dashboard/latest/release.yaml

source ~/.bashrc

echo -e "All Done!"

