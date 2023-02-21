# OpenAI Wrapper
> Simple web app to access some OpenAI endpoints

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/open-ai-wrapper?include_prereleases=&sort=semver&color=blue)](https://github.com/MichaelCurrin/open-ai-wrapper/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![dependency - openai](https://img.shields.io/badge/dependency-openai-blue?logo=openai&logoColor=white)](https://pypi.org/project/openai)
[![dependency - flask](https://img.shields.io/badge/dependency-flask-blue?logo=flask&logoColor=white)](https://pypi.org/project/flask)

A basic Flask API that uses a configured secret key and passes on requests to the OpenAI API.


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