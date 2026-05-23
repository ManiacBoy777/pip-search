# Installation Instructions for pip-search-fix

This document provides instructions for installing and configuring `pip-search-fix`, an enhanced PyPI package search tool with colored/styled output, terminal hyperlinking, and description-based search capabilities.

## 1. Install the pip-search-fix Package

First, install the package directly from the repository:

```bash
pip install git+https://github.com/ManiacBoy777/pip-search
```

Or if you cloned the repository locally:

```bash
cd /path/to/pip-search && pip install -e .
```

The `-e` flag installs the package in editable mode, meaning any changes you make to the source code will be reflected immediately without needing to reinstall.

## 2. Using pip-search-fix

After installation, you can use the command directly:

```bash
pip-search-fix requests
pip-search-fix machine learning
pip-search-fix web scraping -n 20
```

## 3. Configure Fish Shell Function (Optional)

To seamlessly integrate `pip-search-fix` with your Fish shell so you can use `pip search` as usual, create a function that redirects `pip search` commands to `pip-search-fix`.

Create a file named `pip.fish` in your `~/.config/fish/functions/` directory with the following content:

```fish
function pip
    set command $argv[1]
    set -e argv[1]
    switch "$command"
        case 'search'
            pip-search-fix $argv
        case '*'
            command pip $command $argv
    end
end
```

You can create this file using:

```bash
mkdir -p ~/.config/fish/functions/
cat > ~/.config/fish/functions/pip.fish << 'EOF'
function pip
    set command $argv[1]
    set -e argv[1]
    switch "$command"
        case 'search'
            pip-search-fix $argv
        case '*'
            command pip $command $argv
    end
end
EOF
```

After creating the file, restart your Fish shell or run:

```bash
source ~/.config/fish/functions/pip.fish
```

Now you can use `pip search` as you normally would, and it will automatically use `pip-search-fix`:

```bash
pip search requests
pip search machine learning
```

## Requirements

- Python >= 3.8
- requests >= 2.25.0
