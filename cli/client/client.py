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
app.add_typer(build_app, name="build")

@app.command(help="Show all available languages that orbital can build for!")
def show_available_langs():
	orbital_print("Here are the available languages that orbital can build for!")
	orbital_print("python. java, nodejs, go, ruby, cpp, clojure")

@build_app.command("python")
def build_python():
	print("Building for python!")

@build_app.command("ruby")
def build_ruby():
	print("Building for ruby!")

@build_app.command("clojure")
def build_clojure():
	print("Building for clojure!")

@build_app.command("java")
def build_java():
	print("Building for java!")

@build_app.command("javascript")
def build_javascript():
	print("Building for javascript!")

@build_app.command("cpp")
def build_cpp():
	print("Building for cpp!")

@build_app.command("go")
def build_go():
	print("Building for go!")

if __name__ == "__main__":
	app()

