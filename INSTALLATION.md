# Installation Instructions for Enhanced `pip-search-two`

This document provides instructions for installing the enhanced `pip-search-two` command-line tool, which offers colored/styled output, terminal hyperlinking, and description-based search capabilities. It also includes steps to integrate it with the Fish shell using a custom function.

## 1. Install the `pip-search-two` Python Package

First, you need to install the `pip-search-two` package. This can be done directly from the cloned repository. Navigate to the directory where you cloned the repository and run the following command:

```bash
cd /home/ubuntu/pip-search-two && sudo pip3 install -e .
```

This command installs the package in editable mode, meaning any changes you make to the source code in the `/home/ubuntu/pip-search-two` directory will be reflected immediately without needing to reinstall.

## 2. Configure Fish Shell Function

To seamlessly integrate `pip-search-two` with your Fish shell, you can create a function that redirects `pip search` commands to `pip-search-two`. This allows you to use `pip search` as usual, but with the enhanced functionality.

Create a file named `pip.fish` in your `~/.config/fish/functions/` directory with the following content:

```fish
function pip
    set command $argv[1]
    set -e argv[1]
    switch "$command"
        case 'search'
            pip-search-two $argv
        case '*'
            command pip $command $argv
    end
end
```

You can create this file and add the content using the following commands:

```bash
mkdir -p ~/.config/fish/functions/
printf 'function pip\n    set command $argv[1]\n    set -e argv[1]\n    switch "$command"\n        case \'search\'\n            pip-search-two $argv\n        case \'*\'\n            command pip $command $argv\n    end\nend\n' > ~/.config/fish/functions/pip.fish
```

After creating the file, restart your Fish shell or run `source ~/.config/fish/functions/pip.fish` for the changes to take effect.

Now, when you run `pip search <your_query>`, it will automatically use the enhanced `pip-search-two` tool.
