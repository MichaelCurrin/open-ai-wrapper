# OpenAI Wrapper
> Simple web app to access some OpenAI endpoints

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/open-ai-wrapper?include_prereleases=&sort=semver&color=blue)](https://github.com/MichaelCurrin/open-ai-wrapper/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
[![dependency - flask](https://img.shields.io/badge/dependency-flask-blue?logo=flask&logoColor=white)](https://pypi.org/project/flask)
[![dependency - openai](https://img.shields.io/badge/dependency-openai-blue?logo=openai&logoColor=white)](https://pypi.org/project/openai)

If you want to build a web app that requests the OpenAI API but don't want to make requests in JS (exposing your credentials on requests), you can use a backend server instead. So requests go from frontend to backend to OpenAI and then passed back to show on the frontend.

This implementation is in Python with a basic Flask API. You must sign up for OpenAI API and configure your secret value in your local config file in this repo.


## Installation

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

```sh
$ make all
```

## Configuration

1. Signup for an account at https://openai.com
1. Create your API key.
1. Create `.local.env` in a local copy of this repo. e.g.
    ```sh
    OPENAI_API_KEY='sk-abcdef123'
    ```
1. Start the app.


## Usage

```sh
$ make run
```


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
