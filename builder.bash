#TODO This bash script needs a refactor.
# Make sure you docker login before using the push functions.
# https://devhints.io/bash

prefix="docker.io/danielfmorine/template"
if [[ "$1" == "buildall" ]]; then
	docker build --target prod -t "$prefix:frontend-latest" ./frontend
	docker build --target prod -t "$prefix:backend-latest" ./backend
	docker build -t "$prefix:database-latest" ./database
	exit 0
fi

if [[ "$1" == "pushall" ]]; then
	docker push "$prefix:frontend-latest"
	docker push "$prefix:backend-latest"
	docker push "$prefix:database-latest"
	exit 0
fi

if [[ -z "$1" || -z "$2" ]]; then
	echo "Two arguments required, usage: 
	./builder.bash <context [frontend,backend,database]> <operation [build, push, buildall]> 
	The build operation also tags with your third arg, optionally, or as <service>-template.
	Also, you can one arg, buildall or one arg pushall to push/build all images.
	"
	exit 1
fi

if [[ "$1" != "database" && "$1" != "backend" && "$1" != "frontend" ]]; then
	echo "Image tag not valid, use [frontend,backend,database]"
	exit 1
fi

if [[ "$2" != "build" && "$2" != "push" ]]; then
	echo "Operation not valid, use [build, push]."
	exit 1
fi

context="./$1"
operation="$2"
tag="${3:-docker.io/danielfmorine/template:$1-latest}"
target="prod"

build() {
	docker build --target $target -t $tag $context
}

push() {
	docker push $tag
}
# call the function
$operation
exit 0

