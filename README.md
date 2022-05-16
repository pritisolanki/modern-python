## modern-python
Exploring setting up a python project with virtual environment.

## Technical Stack
* Python 3.8.2
* Poetry 1.1.13

## Things I fixed to make it work on MAC 
- Fix bashrc file
```
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init --path)"
```
- Install poetry via homebrew

## Reference
[Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/#installing-python-with-pyenv)