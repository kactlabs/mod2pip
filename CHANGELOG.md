# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.11.0] - 2025-01-29

### Added
- **New `--validate-env` flag**: Validate `.env` file values against known patterns
  - Usage: `mod2pip --validate-env`
  - Validates API keys, tokens, URLs, and other sensitive values
  - **100+ validation patterns** for popular services including:
    - AI/ML: OpenAI, Gemini, DeepSeek, Anthropic, Groq, Cohere, Hugging Face, Replicate, Stability AI, ElevenLabs, AssemblyAI, LangChain
    - Vector Databases: Pinecone, Weaviate
    - Communication: Slack, Discord, Telegram, Zoom
    - Cloud: AWS, Azure, GCP, Netlify, Vercel, Heroku, Railway, Render, Fly.io
    - Databases: MongoDB, PostgreSQL, Redis, Supabase, PlanetScale, CockroachDB, Neon, Upstash
    - CMS: Contentful, Sanity, Airtable, Notion
    - Version Control: GitHub, GitLab, Bitbucket
    - Payments: Stripe, PayPal, Square
    - Email: SendGrid, Mailgun, Twilio
    - CRM: HubSpot, Intercom, Zendesk, Freshdesk, Salesforce
    - Analytics: Amplitude, Mixpanel, Segment, LogRocket, Datadog
    - Error Tracking: Sentry, Bugsnag, Rollbar, New Relic
    - And many more...
  - Reports validation issues with helpful examples
  - Patterns defined in `mod2pip/env_patterns.json`
  - Helps catch configuration errors before deployment
  - Supports partial name matching (e.g., SLACK_TOKEN matches SLACK_BOT_TOKEN pattern)

- New helper functions for validation:
  - `_load_env_patterns()`: Loads validation patterns from JSON
  - `validate_env_values()`: Validates env values against patterns
  - `validate_env_file()`: Main validation function

- New configuration file:
  - `mod2pip/env_patterns.json`: 100+ pattern definitions for environment variable validation covering popular services (AI/ML, Cloud, Databases, CMS, Analytics, etc.)

### Fixed
- Resolved all flake8 linting issues for improved code quality
  - Fixed unused variable warnings
  - Fixed import statement formatting
  - Fixed function spacing (E302, E305)
  - Fixed bare except clauses (E722)
  - Configured `.flake8` to ignore F541 (f-strings without placeholders)
  - Excluded test data files and documentation from linting
- **Fixed package name capitalization**: Now uses correct PyPI package names from API response instead of import names (e.g., `Flask` instead of `flask`)
- **Fixed duplicate package prevention**: Enhanced deduplication logic to prevent multiple versions of the same package
- **Fixed directory creation**: Automatically creates parent directories when saving requirements.txt to nested paths (prevents "File not found" errors)

### Improved
- Code quality improvements across all Python files
- Better adherence to PEP 8 style guidelines
- Cleaner, more maintainable codebase
- More robust file handling with automatic directory creation
- Enhanced error handling for file operations
- **Comprehensive standard library filtering**: 1,785 stdlib modules to prevent false positives
- **Extensive package mapping**: 1,156 import-to-package mappings for accurate resolution
- **Graceful syntax error handling**: Falls back to regex parsing when AST parsing fails (supports legacy Python 2 code)
- **Python 3.13 support**: Fully tested and compatible with Python 3.9-3.13

### Documentation
- Updated `README.md` with `--validate-env` examples and comprehensive list of 100+ supported patterns
- Updated `CHANGELOG.md` with v0.11.0 release notes

## [0.10.0] - 2025-01-29

### Added
- **New `--generate-env` flag**: Automatically scan Python files for environment variables and generate `.env` and `.env.sample` files
  - Usage: `mod2pip --generate-env --force`
  - Scans all Python files in the project for environment variable usage
  - Detects variables accessed via `os.environ`, `os.getenv`, `environ.get`, etc.
  - Extracts default values automatically from code
  - Tracks file locations and line numbers for each variable
  - Generates smart descriptions for common variables (DATABASE_URL, API_KEY, etc.)
  - Creates both `.env` and `.env.sample` files
  - **Smart merging**: Intelligently merges with existing .env files
    - Preserves existing variable values
    - Adds newly discovered variables without duplicates
    - Keeps existing variables even if not detected in code
    - Supports both `.env.sample` and `.env.example` formats
  - Respects `--ignore` directories and standard ignore patterns
  - Perfect for project documentation and onboarding new developers

- New helper functions for environment variable detection:
  - `scan_for_env_variables()`: Main scanning function
  - `_extract_default_value()`: Extracts default values from code
  - `_infer_description()`: Generates descriptions for common env vars
  - `generate_env_files()`: Creates .env and .env.sample files with smart merging
  - `_parse_existing_env_file()`: Parses existing .env files for merging

- New configuration file:
  - `mod2pip/env_patterns.json`: Pattern definitions for environment variable validation

### Improved
- Enhanced library name matching in `--lib` flag to handle more package name variations
- Better normalization of package names (hyphens vs underscores)
- Improved error messages and logging for environment variable detection

### Documentation
- Updated `README.md` with `--generate-env` examples and usage
- Updated `DEVELOPMENT.md` with new feature information and test scripts
- Updated `CHANGELOG.md` with comprehensive v0.10.0 release notes
- Created `demo_project.py` - comprehensive demo file for testing all features
- Created `test_mod2pip_features.py` - comprehensive test suite for all features

## [0.9.0] - 2025-01-25

### Added
- **New `--append` flag**: Append libraries to existing requirements.txt instead of overwriting
  - Usage: `mod2pip --append --lib package1,package2`
  - Preserves existing entries in requirements.txt
  - Works with `--lib` flag to add new libraries without removing existing ones

### Fixed
- Fixed `--force` flag with `--lib` to properly overwrite instead of always appending
- Improved error messages to guide users between `--force` and `--append` options

## [0.8.0] - 2025-01-25

### Added
- **New `--lib` flag**: Add specific libraries with their installed versions to requirements.txt
  - Usage: `mod2pip --force --lib langchain,langchain-core`
  - Supports comma-separated library names
  - Automatically detects installed versions from the current environment
  - Works with all existing flags (`--force`, `--print`, `--mode`, etc.)
  - Enhanced library name matching to handle hyphens vs underscores (e.g., `langchain-core` vs `langchain_core`)
- **New `--append` flag**: Append libraries to existing requirements.txt instead of overwriting
  - Usage: `mod2pip --append --lib package1,package2`
  - Preserves existing entries in requirements.txt
  - Works with `--lib` flag to add new libraries without removing existing ones

### Fixed
- Fixed `--print` flag behavior when used with `--lib` to correctly output to stdout without checking for existing requirements.txt
- Fixed `--force` flag with `--lib` to properly overwrite instead of always appending
- Improved library name normalization for better package detection
- Fixed flake8 linting issues for better code quality
- Corrected publish.sh script (was referencing wrong project name)

### Changed
- Updated version from 0.6.0 to 0.8.0
- Added `.flake8` configuration file for consistent code style
- Improved code formatting to meet PEP 8 standards
- Enhanced error messages and logging for better user experience

## [0.7.0] - 2025-01-25

### Note
- Version 0.7.0 was skipped in favor of 0.8.0 to include additional fixes

## [0.6.0] - 2024

### Added
- Enhanced import detection for dynamic imports
- Support for conda packages
- Transitive dependency resolution with `--include-transitive` flag
- `--transitive-depth` option to control dependency resolution depth
- `--enhanced-detection` flag for advanced import detection
- Support for detecting imports in various patterns:
  - `__import__()` calls
  - `importlib.import_module()` calls
  - Dynamic imports in exec/eval statements
  - Conditional imports in try/except blocks
  - Late imports inside functions

### Improved
- Better handling of editable packages
- Enhanced namespace package detection
- Improved conda environment integration
- More robust package metadata parsing

## [0.5.x and earlier]

See [HISTORY.rst](HISTORY.rst) for earlier version history.

---

## Release Notes

### How to use the new features (v0.10.0)

#### Generate Environment Variable Files

```bash
# Scan project and generate .env and .env.sample files
mod2pip --generate-env --force

# Scan specific directory
mod2pip --generate-env --force /path/to/project

# Use with --ignore to skip directories
mod2pip --generate-env --force --ignore tests,docs
```

**Example output:**
```bash
INFO: Scanning for environment variables in /home/project
INFO: Found 15 environment variables
INFO:   API_KEY: found in 2 location(s)
INFO:   DATABASE_URL: found in 3 location(s)
INFO: Successfully created /home/project/.env
INFO: Successfully created /home/project/.env.sample
```

**Generated .env file:**
```bash
# Environment Variables
# Generated by mod2pip --generate-env

# API authentication key
# Used in: config.py:12, app.py:5
API_KEY=

# Database connection URL
# Used in: config.py:8
DATABASE_URL=postgresql://localhost/mydb

# Debug mode flag (True/False)
# Used in: config.py:15
DEBUG=False
```

See README.md for more examples and detailed usage.

### How to use the --lib flag (v0.9.0)

```bash
# Add specific libraries with their versions (overwrites file)
mod2pip --force --lib langchain,langchain-core

# Append libraries to existing requirements.txt (preserves existing entries)
mod2pip --append --lib langchain,langchain-core

# Preview without creating file
mod2pip --print --lib requests,numpy,pandas

# Use with version schemes
mod2pip --append --lib flask,django --mode compat  # Uses ~=
mod2pip --append --lib flask,django --mode gt      # Uses >=
mod2pip --append --lib flask,django --mode no-pin  # No version

# Save to custom file
mod2pip --force --lib langchain --savepath my-requirements.txt
```

[0.11.0]: https://github.com/kactlabs/mod2pip/compare/v0.10.0...v0.11.0
[0.10.0]: https://github.com/kactlabs/mod2pip/compare/v0.9.0...v0.10.0
[0.9.0]: https://github.com/kactlabs/mod2pip/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/kactlabs/mod2pip/compare/v0.6.0...v0.8.0
[0.7.0]: https://github.com/kactlabs/mod2pip/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/kactlabs/mod2pip/releases/tag/v0.6.0
