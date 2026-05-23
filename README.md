# pip-search

Search PyPI packages from the command-line with enhanced styling like the old `pip search`

## Installation
**Using pip:**

```bash
pip install git@https://github.com/ManiacBoy777/pip-search
```

**Using uv (Recommended):**

```bash
uv pip install -U --system git+https://github.com/ManiacBoy777/pip-search
```

### Shell pip functions (optional but recommended for ease of use)

To use it like normal `pip search` worked in the past, download the shell function to your shell's functions directory:

#### Fish

**Using curl:**

```bash
curl -fsSL https://raw.githubusercontent.com/ManiacBoy777/pip-search/master/functions/pip.fish -o ~/.config/fish/functions/pip.fish
```

**Using wget:**

```bash
wget https://raw.githubusercontent.com/ManiacBoy777/pip-search/master/functions/pip.fish -O ~/.config/fish/functions/pip.fish
```

#### Bash

**Using curl:**

```bash
curl -fsSL https://raw.githubusercontent.com/ManiacBoy777/pip-search/master/functions/pip.bash -o ~/.bash_functions
```

Then add the following to your `~/.bashrc`:

```bash
if [ -f ~/.bash_functions ]; then
    source ~/.bash_functions
fi
```

**Using wget:**

```bash
wget https://raw.githubusercontent.com/ManiacBoy777/pip-search/master/functions/pip.bash -O ~/.bash_functions
```

#### Zsh

**Using curl:**

```bash
curl -fsSL https://raw.githubusercontent.com/ManiacBoy777/pip-search/master/functions/pip.zsh -o ~/.zsh_functions
```

Then add the following to your `~/.zshrc`:

```bash
if [ -f ~/.zsh_functions ]; then
    source ~/.zsh_functions
fi
```

**Using wget:**

```bash
wget https://raw.githubusercontent.com/ManiacBoy777/pip-search/master/functions/pip.zsh -O ~/.zsh_functions
```

## Usage

```bash
pip-search-fix requests
pip-search-fix machine learning
```

## Features

- 🎨 Colorized and styled output
- 🔗 Terminal hyperlinks to PyPI packages
- 🔍 Smart search ranking by name and description
- ⚡ Concurrent package info fetching
- 📝 Detailed package information and versions
