from hashlib import blake2b

# https://docs.python.org/3/library/hashlib.html
# biblioteca para cifrar 

def cifrar(senha):
    c = blake2b()
    em_bytes = bytes(senha, encoding= 'utf-8')
    c.update(em_bytes)
    return c.hexdigest()

def valida_senha(cifrado, senha_fornecida):
    return cifrado == cifrar(senha_fornecida)