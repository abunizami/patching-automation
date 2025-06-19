import paramiko
from utils.logger import get_logger

logger = get_logger()

def setup_linux_server(server):
    ip = server["ip"]
    username = server["username"]
    key_file = server["key_file"]

    logger.info(f"Connecting to Linux server {ip}")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, key_filename=key_file)

    commands = [
        "sudo apt update && sudo apt upgrade -y",
        "sudo apt install -y mysql-server python3.8 python3-pip",
        "pip3 install virtualenv django==4.0 mysqlclient keyring passlib paramiko requests cryptography bootstrapmodalforms widget_tweaks pymysql"
    ]

    for cmd in commands:
        logger.info(f"Executing: {cmd}")
        stdin, stdout, stderr = ssh.exec_command(cmd)
        logger.info(stdout.read().decode())
        logger.error(stderr.read().decode())

    ssh.close()
