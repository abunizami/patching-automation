import winrm
from utils.logger import get_logger

logger = get_logger()

def setup_windows_server(server):
    ip = server["ip"]
    username = server["username"]
    password = server["password"]

    logger.info(f"Connecting to Windows server {ip}")
    session = winrm.Session(ip, auth=(username, password))

    commands = [
        "Install-WindowsFeature -Name Web-Server,Web-CGI",
        "choco install googlechrome -y",
        "choco install mysql -y",
        "choco install python --version=3.8.10 -y",
        "pip install virtualenv django==4.0 mysqlclient keyring passlib paramiko requests cryptography bootstrapmodalforms widget_tweaks pymysql",
        "Install-Module -Name CredentialManager -Force",
        "Install-Module -Name MySQLCmdlets -Force",
        "Install-Module -Name VMware.PowerCLI -RequiredVersion 12.1 -Force"
    ]

    for cmd in commands:
        logger.info(f"Executing: {cmd}")
        result = session.run_ps(cmd)
        logger.info(result.std_out.decode())
        logger.error(result.std_err.decode())
