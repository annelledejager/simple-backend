[![Build Status](https://travis-ci.org/annelledejager/simple-website.svg?branch=master)](https://travis-ci.org/annelledejager/simple-backend)

# Simple backend

This project is a simple Django backend application with basic functionality. A space to experiment and play with new technologies. 

The local development environment is setup using Docker. The Docker image is built, uploaded and stored in Heroku's Docker registry. 

The production application is deployed to Heroku through Travis CI without being Dockerized. 

## Demo

Follow [this](https://simple-backend.herokuapp.com/colors/) link.

## Getting Started

Clone the repository to a location of your liking. In your shell run the following commands to run the application locally. 

```
$ cd simple_backend
$ docker-compose up
```

If you want to pull the latest Docker image from Heroku run the following command before the `up` command.

```
$ docker-compose pull
```

Then visit `http://localhost:8000/` to view your application.

### Prerequisites

You need to install docker and docker-compose. Follow [theses](https://docs.docker.com/docker-for-mac/) instructions.

## Running the tests

```
$ cd simple_backend
$ docker-compose -f docker-compose.test.yml up
```

## Deployment

The application is deployed to Heroku using Travis CI. Pushing the master branch will trigger a build job. 

The build job includes
* build docker image
* unit tests against latest docker image
* deploy application to production
* test production

## Built With

* [Django](https://www.djangoproject.com/) - High-level Python Web framework
* [Django REST Framework](http://www.django-rest-framework.org/) - A powerful and flexible toolkit for building Web APIs.
* [Docker](https://www.docker.com/) - Software containerization platform
* [Travis](https://travis-ci.org/) - Distributed continuous integration service

## Authors

* **Annelle de Jager** 

See also the list of [contributors](https://github.com/annelledejager/simple-backend/graphs/contributors) who participated in this project.
