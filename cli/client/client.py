import os, sys, yaml, subprocess, argparse, platform, re
import typer, shellingham, emoji
from rich import print
from contextlib import redirect_stdout
from io import StringIO
from typing_extensions import Annotated

## ORBITAL_HOUSE_PATH=str(os.environ.get("ORBITAL_HOUSE_PATH"))

class Silent(StringIO):
	def write(self, txt):
		pass

def success_print(arg_str):
	print(str(":rocket: :rocket: [bold green] >> " + arg_str + "[/bold green]" ))

def orbital_print(arg_str): ## change this
	print(str(":rocket: :rocket: [bold green] >> " + arg_str + "[/bold green]" ))

def exception_print(arg_str):
	print(str(":heavy_exclamation_mark: :heavy_exclamation_mark: [bold red] >> " + arg_str + "[/bold red]"))

app = typer.Typer(help="Welcome to orbital! -- Build Docker images with Tekton and Kaniko!", add_completion=False, no_args_is_help=True)
build_app = typer.Typer(help="Trigger a build for a given language!", add_completion=False, no_args_is_help=True)
override_app = typer.Typer(help="Override a given config, Dockerfile or argument!", add_completion=False, no_args_is_help=True)
app.add_typer(build_app, name="build")
app.add_typer(override_app, name="override")


@app.command(help="Show all available languages that orbital can build for!")
def show_available_langs():
	orbital_print("Here are the available languages that orbital can build for!")
	orbital_print("python. java, nodejs, go, ruby, cpp, clojure")

## TODO - document this in a different area, maybe in the "override" command
@override_app.command("dockerfile", help="<path-to-dockerfile> Override the defualt Dockerfile path with your own path - run command to see examples")
def override_dockerfile(arg_path_to_dockerfile):
	## specify the location of the Dockerfile -- it must be within a git repo - and (for now) in the root directory of the repo
	## this is also not taking into account concurrency, like at all ... it's assuming that only one instance of orbita lcan override/set this env variable
	## will probably need to move away from env vars or create uuid based (and temp) env vars
	os.environ['ORBITAL_DOCKERFILE'] = str(arg_path_to_dockerfile)

## handler for which image registry to use (local, ghcr, aws, redhat, etc,)
def which_image_registry(arg_image_registry):
	match str(arg_image_registry):
		case "local": ## local filesystem (linux, docker)
			print("")
		case "quay" ## redhat - RedHat Quay
			print("")
		case "ecr":## amazon - Elastic Container Registry
			print("")
		case "acr": ## azure - Azure Container Registry
			print("")
		case "gcr": ## google - Google Container Registry
			print("")
		case "ghcr": ## github - GitHub Container Registry
			print("")
		case "dockerhub": ## DockerHub
			print("")

## handler for what type of deployment method (helm, kustomize, vanilla manifest, cdk8s, etc)
def which_deployment_method(arg_deployment_method):
	match str(arg_deployment_method):
		case "vanilla":## standard k8s yaml manifests
			print("")
		case "helm":
			print("")
		case "kustomize":
			print("")
		case "cdk8s":
			print("")

## what k8s cluster (eks, gks, vanilla, aks)
def which_cluster_type(arg_cluster_type):
	match str(arg_cluster_type):
		case "vanilla":
			print("")
		case "eks":
			print("")
		case "gks":
			print("")
		case "openshift":
			print("")
		case "aks":
			print("")

## which programming lang to use (will be used to determine Dockerfile)
def which_language(arg_language):
	match str(arg_language):
		case "python":
			print("")
		case "ruby":
			print("")
		case "clojure":
			print("")
		case "java":
			print("")
		case "javascript":
			print("")
		case "go":
			print("")
		case "cpp":
			print("")

if __name__ == "__main__":
	app()

