# Python sample app using pipenv package manager

## Building

`pack build run-sample --buildpack paketo-buildpacks/python`

## Running

`docker run --interactive --tty --env PORT=8080 --publish 8080:8080 run-sample`

## Viewing

`curl http://localhost:8080`
