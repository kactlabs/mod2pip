# mod2pip - Generate requirements.txt file for any project based on imports

[![Tests](https://github.com/kactlabs/mod2pip/actions/workflows/tests.yml/badge.svg)](https://github.com/kactlabs/mod2pip/actions/workflows/tests.yml)
[![PyPI version](https://img.shields.io/pypi/v/mod2pip.svg)](https://pypi.python.org/pypi/mod2pip)
[![codecov](https://codecov.io/gh/kactlabs/mod2pip/branch/master/graph/badge.svg?token=0rfPfUZEAX)](https://codecov.io/gh/kactlabs/mod2pip)
[![License](https://img.shields.io/pypi/l/mod2pip.svg)](https://pypi.python.org/pypi/mod2pip)

## About This Fork

This repository is forked from [mod2pip - https://github.com/kactlabs/mod2pip](https://github.com/kactlabs/mod2pip) with additional bugfixes and improvements.

## Installation

```sh
pip install mod2pip
```

**Note:** If you don't want support for jupyter notebooks, you can install mod2pip without the dependencies that give support to it:

```sh
pip install --no-deps mod2pip
pip install yarg==0.1.9 docopt==0.6.2
```

## Testing

To run the comprehensive test suite:

```sh
# Install in development mode first
pip install -e .

# Run tests
python test_mod2pip_features.py
```

## Usage

```
Usage:
    mod2pip [options] [<path>]

Arguments:
    <path>                The path to the directory containing the application files for which a requirements file
                          should be generated (defaults to the current working directory)

Options:
    --use-local           Use ONLY local package info instead of querying PyPI
    --pypi-server <url>   Use custom PyPi server
    --proxy <url>         Use Proxy, parameter will be passed to requests library. You can also just set the
                          environments parameter in your terminal:
                          $ export HTTP_PROXY="http://10.10.1.10:3128"
                          $ export HTTPS_PROXY="https://10.10.1.10:1080"
    --debug               Print debug information
    --ignore <dirs>...    Ignore extra directories, each separated by a comma
    --no-follow-links     Do not follow symbolic links in the project
    --encoding <charset>  Use encoding parameter for file open
    --savepath <file>     Save the list of requirements in the given file
    --print               Output the list of requirements in the standard output
    --force               Overwrite existing requirements.txt
    --append              Append to existing requirements.txt (use with --lib)
    --diff <file>         Compare modules in requirements.txt to project imports
    --clean <file>        Clean up requirements.txt by removing modules that are not imported in project
    --mode <scheme>       Enables dynamic versioning with <compat>, <gt> or <non-pin> schemes
                          <compat> | e.g. Flask~=1.1.2
                          <gt>     | e.g. Flask>=1.1.2
                          <no-pin> | e.g. Flask
    --scan-notebooks      Look for imports in jupyter notebook files.
    --lib <packages>...   Add specific libraries with their installed versions (comma-separated)
    --generate-env        Scan Python files for environment variables and generate .env and .env.sample files
    --validate-env        Validate .env file values against known patterns (API keys, tokens, URLs, etc.)
```

## Examples

### Scan Project for Imports

```sh
$ mod2pip /home/project/location
Successfully saved requirements file in /home/project/location/requirements.txt
```

Contents of requirements.txt:

```
wheel==0.23.0
Yarg==0.1.9
docopt==0.6.2
```

### Add Specific Libraries (New in v0.9.0)

Add specific libraries with their installed versions without scanning the project:

```sh
# Overwrite requirements.txt with specific libraries
$ mod2pip --force --lib langchain,langchain-core,numpy
Successfully saved requirements file in requirements.txt
```

```sh
# Append libraries to existing requirements.txt (skips duplicates)
$ mod2pip --append --lib requests,flask,django
Skipped 1 package(s) already in requirements.txt
Successfully appended to requirements file requirements.txt
```

```sh
# Preview libraries without writing to file
$ mod2pip --print --lib pandas,numpy,scipy
pandas==2.0.3
numpy==1.24.3
scipy==1.11.1
```

```sh
# Use different version schemes
$ mod2pip --force --lib flask,django --mode compat
flask~=2.0.1
django~=4.2.0

$ mod2pip --force --lib flask,django --mode gt
flask>=2.0.1
django>=4.2.0

$ mod2pip --force --lib flask,django --mode no-pin
flask
django
```

### Generate Environment Variable Files (New in v0.10.0)

Automatically scan your Python project for environment variables and generate `.env` and `.env.sample` files:

```sh
$ mod2pip --generate-env --force
INFO: Scanning for environment variables in /home/project
INFO: Found 15 environment variables
INFO:   API_KEY: found in 2 location(s)
INFO:   DATABASE_URL: found in 3 location(s)
INFO:   DEBUG: found in 1 location(s)
INFO: Successfully created /home/project/.env
INFO: Successfully created /home/project/.env.sample
INFO: Environment files generated successfully!
```

**Smart Merging**: If `.env` or `.env.sample` files already exist, mod2pip will intelligently merge new variables with existing ones:
- Preserves existing variable values
- Adds newly discovered variables
- Avoids duplicates
- Keeps existing variables even if not detected in code
- Supports both `.env.sample` and `.env.example` formats

```sh
$ mod2pip --generate-env --force
INFO: Successfully merged 5 new variable(s) with 3 existing in /home/project/.env
INFO: Successfully merged 5 new variable(s) with 3 existing in /home/project/.env.sample
```

Example generated `.env` file:

```bash
# Environment Variables
# Generated by mod2pip --generate-env
# Merged with 3 existing variable(s), added 5 new variable(s)

# API authentication key
# Used in: config.py:12, app.py:5
API_KEY=

# Database connection URL
# Used in: config.py:8, models.py:3, database.py:10
DATABASE_URL=postgresql://localhost/mydb

# Debug mode flag (True/False)
# Used in: config.py:15
DEBUG=False

# Secret key for encryption/signing
# Used in: config.py:20
SECRET_KEY=dev-secret-key
```

For more examples, see the `demo_project.py` file.

### Validate Environment Variable Values (New in v0.11.0)

Validate your `.env` file to ensure API keys, tokens, and other sensitive values match expected patterns:

    $ mod2pip --validate-env
    INFO: Validating /home/project/.env...
    ✓ All 15 environment variable(s) validated successfully!

If validation issues are found:

    $ mod2pip --validate-env
    INFO: Validating /home/project/.env...
    ERROR: ✗ Found 2 validation issue(s):
    
      Variable: SLACK_BOT_TOKEN
      Current value: abc123...
      Expected: Slack Bot Token (starts with xoxb-)
      Example: xoxb-YOUR-BOT-TOKEN-HERE
    
      Variable: OPENAI_API_KEY
      Current value: test-key...
      Expected: OpenAI API Key (starts with sk-)
      Example: sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

**Supported Patterns:**
- **AI/ML Services**: OpenAI, Gemini, DeepSeek, Anthropic, Groq, Cohere, Hugging Face, Replicate, Stability AI, ElevenLabs, AssemblyAI, LangChain
- **Vector Databases**: Pinecone, Weaviate
- **Communication**: Slack, Discord, Telegram, Zoom
- **Cloud Platforms**: AWS, Azure, Google Cloud Platform
- **Hosting/Deployment**: Netlify, Vercel, Heroku, Railway, Render, Fly.io, DigitalOcean, Cloudflare
- **Databases**: MongoDB, PostgreSQL, Redis, Supabase, PlanetScale, CockroachDB, Neon, Upstash, MongoDB Atlas
- **CMS/Content**: Contentful, Sanity, Airtable, Notion
- **Version Control**: GitHub, GitLab, Bitbucket
- **Payment Processing**: Stripe, PayPal, Square
- **Email Services**: SendGrid, Mailgun, Twilio
- **CRM/Support**: HubSpot, Intercom, Zendesk, Freshdesk, Salesforce
- **Analytics**: Amplitude, Mixpanel, Segment, LogRocket, Datadog
- **Error Tracking**: Sentry, Bugsnag, Rollbar, New Relic
- **Search/Logging**: Algolia, Elasticsearch
- **Maps**: Mapbox, Google Maps
- **Real-time**: Pusher
- **Project Management**: Linear, Asana, Jira
- **Other**: Firebase, JWT secrets, and more

**Total: 100+ validation patterns** covering the most popular services and APIs.

Patterns are defined in `mod2pip/env_patterns.json` and can be customized.

## Why not pip freeze?

- `pip freeze` only saves the packages that are installed with `pip install` in your environment.
- `pip freeze` saves all packages in the environment including those that you don't use in your current project (if you don't have `virtualenv`).
- Sometimes you just need to create `requirements.txt` for a new project without installing modules.
- With `--lib` flag, you can selectively add specific packages with their versions.

## Citing mod2pip

If you find mod2pip useful in your research and wish to cite it, please use the following BibTex entry:

```bibtex
@software{mod2pip2025,
   author = {Raja CSP Raman},
   title = {mod2pip: Generate requirements.txt file for any project based on imports},
   url = {https://github.com/kactlabs/mod2pip/},
   version = {0.9.0},
   year = {2025},
}
```