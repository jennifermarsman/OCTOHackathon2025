# OCTO Hackathon 2025
This is some sample code for use at a hackathon using the Azure OpenAI o3 model.  

## Setup
This project assumes that you are using our endpoint.

Use the following commands to set up your environment with `uv`. This creates and activates a virtual environment and installs the required packages. For subsequent runs after the initial install, you will only need to activate the environment and then run the python script.

### First run
Make sure you have uv installed, see the Prerequisites below.

Linux/macOS:
```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
python responses.py
```

Windows:
```cmd
uv venv
.venv\Scripts\activate
uv pip install -r requirements.txt
python responses.py
```

### Subsequent runs

Linux/macOS:
```bash
source .venv/bin/activate
python responses.py
```

Windows:
```cmd
.venv\Scripts\activate
python responses.py
```

## Prerequisites

Before running this project, you need to have `uv` installed. Many developers may already have this installed.

Recommended installers:
- Linux: apt or your distribution's package manager
- macOS: [brew](https://brew.sh/)
- Windows: [winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/)

Install `uv`:

Linux:
```bash
sudo apt update && sudo apt install pipx
pipx ensurepath
pipx install uv
```

macOS:
```bash
brew install uv
```

Windows:
```cmd
winget install astral-sh.uv -e
```

On Windows, exit and restart your terminal after installation to ensure `uv` is available on your PATH.
