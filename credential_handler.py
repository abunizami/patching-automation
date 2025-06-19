import keyring

def store_credential(service_name, username, password):
    keyring.set_password(service_name, username, password)

def get_credential(service_name, username):
    return keyring.get_password(service_name, username)
