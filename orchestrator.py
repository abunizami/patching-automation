import yaml
from linux_setup import setup_linux_server
from windows_setup import setup_windows_server
from utils.logger import get_logger

logger = get_logger()

def load_inventory(file_path="inventory.yaml"):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def main():
    inventory = load_inventory()
    for server in inventory.get("servers", []):
        os_type = server.get("os")
        logger.info(f"Processing {server['name']} ({os_type})")
        try:
            if os_type == "linux":
                setup_linux_server(server)
            elif os_type == "windows":
                setup_windows_server(server)
            else:
                logger.warning(f"Unsupported OS type: {os_type}")
        except Exception as e:
            logger.error(f"Error processing {server['name']}: {e}")

if __name__ == "__main__":
    main()
