[![Build Status](https://travis-ci.org/annelledejager/simple-website.svg?branch=master)](https://travis-ci.org/annelledejager/simple-backend)

# Simple backend

This project is a simple backend with basic functionality. A space to experiment and play with new technologies. 

The project includes a basic Djagno application with one endpoint. The local development environment is setup using Docker. The Docker image is built and stored in Heroku's Docker registry. 

The production application is deployed to Heroku through Travis CI without being Dockerized. 

## Getting Started

Clone the repository to a location of your liking. In your shell run the following commands to run the application locally. 

```
$ cd simple_backend
$ docker-compose pull
$ docker-compose up
```

If you want to pull the latest Docker image from Heroku run the following command before the `pull` command.

```
$ docker-compose pull
```

### Prerequisites

You need to install docker and docker-compose. [Following theses](https://docs.docker.com/docker-for-mac/) instructions.

## Running the tests

```
$ cd simple_backend
$ docker-compose -f docker-compose.test.yml up
```

## Deployment

The application is deployed to Heroku using Travis CI. Pushing to Master will trigger a the build job. 

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

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
