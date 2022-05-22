## modern-python
Exploring setting up a python project with virtual environment.

## Technical Stack
* Python 3.8.2
* Poetry 1.1.13

### How to run

Install project
```
poetry install
```

Run the application
```
poetry run modern-python
```

Run test case
```
poetry run pytest
```

## Things I fixed to make it work on MAC 
- Fix bashrc file
```
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init --path)"
```
- Install poetry via homebrew
- Error : no matches found: coverage[toml]
```
poetry add -D 'coverage[toml]' pytest-cov
```
- Install nox via homebrew

## Reference
[Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/#installing-python-with-pyenv)