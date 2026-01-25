# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

### How to use the new features (v0.9.0)

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

[0.9.0]: https://github.com/kactlabs/mod2pip/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/kactlabs/mod2pip/compare/v0.6.0...v0.8.0
[0.7.0]: https://github.com/kactlabs/mod2pip/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/kactlabs/mod2pip/releases/tag/v0.6.0
