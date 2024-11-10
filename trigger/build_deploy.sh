#!/bin/bash

CYAN="\e[96m"
MAGENTA="\e[95m"
ENDCOLOR="\e[0m"

BRANCH="$(git branch --show-current 2> /dev/null)"
ERRORCODE="$?"

echo -e "${CYAN}
#########################################################
>>> Welcome to Orbital! <<<
#########################################################
${ENDCOLOR}"

########################################################
## TESTS/PROTECTIONS
########################################################

if [ "$ERRORCODE" != "0" ]; then
  echo -e "${MAGENTA} !! ERROR -- You need to run orbital from a folder containing a GIT repository (.git) !! ${ENDCOLOR}"
  exit 1
fi

REPO_NAME=$(echo "${PWD##*/}")
GIT_ORIGIN="$(git remote get-url origin)"
GIT_ORIGIN_WITHOUT_DOT_GIT_SUFFIX=$(echo "$GIT_ORIGIN" | sed 's/\.git//g')
TIER="LOCAL"
PIPELINERUN_NAME="${TIER}-${REPO_NAME}-$(date +%s)"
URL="http://localhost.tekton.nip.io/?repo=$REPO_NAME&ver=$BRANCH&tier=$TIER&name=$PIPELINERUN_NAME"

echo -e "${CYAN}Do you wish to build multi-stage docker image for \"${REPO_NAME}-${TIER}\" and deploy to ${TIER^^}? ${ENDCOLOR}"

read -rp ">> Enter 'y' for yes or 'n' for no [default: n]: " answer
if [[ ${answer,,} == "y" ]]; then
  echo -e "${CYAN}Triggering pipeline run: $PIPELINERUN_NAME ${ENDCOLOR}"
  echo -e $URL
  curl $URL
  echo -e ""
  echo -e "Tiggered!"
  echo -e "${CYAN} >> Go to http://localhost.tekton.nip.io/#/namespaces/tekton-orbital/pipelineruns to view the status of your pipelineRun! ${ENDCOLOR}"
  exit 1
elif [[ ${answer,,} == "n" || -z $answer ]]; then
  echo -e "Aborting!"
  exit 1
else
  echo -e "Invalid input! -- Aborting!"
fi

