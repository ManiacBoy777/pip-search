# pip-search-fix

Search PyPI packages from the command-line with enhanced styling, hyperlinking, and description-based search.

## Installation

### pip-search-fix package

```bash
pip install git@https://github.com/ManiacBoy777/pip-search
```

Or using uv:

```bash
uv pip install -U --system git+https://github.com/ManiacBoy777/pip-search
```

### Fish pip function (optional)

To enhance your Fish shell with the custom pip function, download it to your Fish functions directory:

**Using curl:**

```bash
curl -fsSL https://raw.githubusercontent.com/ManiacBoy777/pip-search/master/functions/pip.fish -o ~/.config/fish/functions/pip.fish
```

**Using wget:**

```bash
wget https://raw.githubusercontent.com/ManiacBoy777/pip-search/master/functions/pip.fish -O ~/.config/fish/functions/pip.fish
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
