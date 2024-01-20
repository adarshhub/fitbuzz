# FitBuzz REST server

The FizzBuzz Hackathon solution using Python.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop/): For compatibility and to automate the config process to setup the server.

### Installation


```
git clone https://github.com/adarshhub/fitbuzz.git
cd fitbuzz
docker build --build-arg FITBUZZ_SECRET_KEY=my-secret-key -t fitbuzz:1.0 .
```

## Usage

```
docker run -p 8000:8000 fitbuzz:1.0
```

### Documentation

Run the server and visit [localhost:8000/docs](http://localhost:8000/docs) for usage help.

## External Libraries

- [Pytest](https://pytest-django.readthedocs.io/en/latest/): For testing API endpoints
- [drf-yasg]: For API documentation