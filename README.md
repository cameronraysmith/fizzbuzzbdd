# fizzbuzzbdd

[![PyPI - Version](https://img.shields.io/pypi/v/fizzbuzzbdd.svg)](https://pypi.org/project/fizzbuzzbdd)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fizzbuzzbdd.svg)](https://pypi.org/project/fizzbuzzbdd)

-----

**Table of Contents**

- [fizzbuzzbdd](#fizzbuzzbdd)
  - [Installation](#installation)
  - [Development](#development)
    - [Specification](#specification)
    - [Setup environment](#setup-environment)
    - [Run unit tests](#run-unit-tests)
    - [Format the code](#format-the-code)
    - [Publish a new version](#publish-a-new-version)
  - [License](#license)

## Installation

```console
python -m pip install "fizzbuzzbdd @ git+https://github.com/cameronraysmith/fizzbuzzbdd.git@main"
```

## Development

### Specification

See [SPECIFICATION.md](./SPECIFICATION.md).

### Setup environment

We use [Hatch](https://hatch.pypa.io/latest/install/) to manage the development environment and production build. Ensure it's installed on your system. It is often convenient to do this with [pipx](https://pypa.github.io/pipx/installation/).

You can print the environments and script commands supported by the current content of [pyproject.toml](./pyproject.toml) with:

```bash
hatch env show
```

### Run unit tests

You can run all the tests with:

```bash
hatch run test
```

### Format the code

Execute the following command to apply linting and check typing:

```bash
hatch run lint:fmt
```

### Publish a new version

You can bump the version, create a commit and associated tag with one command:

```bash
hatch version patch
```

```bash
hatch version minor
```

```bash
hatch version major
```

Your default Git text editor will open so you can add information about the release.

## License

`fizzbuzzbdd` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
