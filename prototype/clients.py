# clientes


# cliente
class Client:
    def __init__(
            self,
            client_id=None,
            name=None,
            email=None,
            password=None
    ):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.password = password


VALID_USER_ID = 42
VALID_USER_NAME = 'Pepe'
VALID_USER_EMAIL = 'pepe@email.com'
VALID_USER_PASSWORD = 'userpass'


# obtener un cliente
# por email y password
def get_client_by_email_password(email, password):
    # TODO conexión con BD
    if email == VALID_USER_EMAIL and password == VALID_USER_PASSWORD:
        return Client(
            client_id=VALID_USER_ID,
            name=VALID_USER_NAME,
            email=VALID_USER_EMAIL
        )
    else:
        return None
