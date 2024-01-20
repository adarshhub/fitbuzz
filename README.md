# FitBuzz REST server

The FizzBuzz Hackathon solution using Python.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop/): To automate the config process to setup the server.

### Installation


```
docker build --build-arg FITBUZZ_SECRET_KEY=my-secret-key -t fitbuzz:1.0 .
```

### Usage

```
docker run -p 8000:8000 fitbuzz:1.0
```