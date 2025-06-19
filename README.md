# env-patching-automation

This project automates patching and environment setup for Windows and Linux servers using Python and PowerShell.

## Features

- OS patching via SSH (Linux) and WinRM (Windows)
- Installation of:
  - .NET 5.1+
  - Chrome browser
  - MySQL
  - Python 3.8 + Django 4.0
  - Required Python packages
- IIS configuration with CGI and wfastcgi
- Secure credential handling using keyring
- Logging and modular structure

## Usage

1. Update `inventory.yaml` with your server details.
2. Run `orchestrator.py` to initiate patching and setup.
3. Logs and results will be saved in the working directory.

## Requirements

- Python 3.8
- Required Python packages (see `requirements.txt`)
- PowerShell 5.1+ on Windows
- SSH access to Linux servers
