class UJCException(Exception):
    def __init__(self, usuario, *args):
        self.__usuario = usuario
        self.__mensagem = f'Usuário "{usuario}" já cadastrado'
        super().__init__(self.__mensagem, *args)


class UNCException(Exception):
    def __init__(self, usuario, *args):
        self.__usuario = usuario
        self.__mensagem = f'Usuário "{usuario}" não cadastrado'
        super().__init__(self.__mensagem, *args)

class PEException(Exception):
    def __init__(self, usuario, *args):
        self.__usuario = usuario
        self.__mensagem = f'Perfil "{usuario}" já existe'
        super().__init__(self.__mensagem, *args)

class PIException(Exception):
    def __init__(self, usuario, *args):
        self.__usuario = usuario
        self.__mensagem = f'Perfil "{usuario}" inexistente'
        super().__init__(self.__mensagem, *args)

class PDException(Exception):
    def __init__(self, usuario, *args):
        self.__usuario = usuario
        self.__mensagem = f'Perfil "{usuario}" está desativado'
        super().__init__(self.__mensagem, *args)

class MFPException(Exception):
    def __init__(self, *args):
        self.__mensagem =  'A mensagem do tweet deve ter entre 1 e 140 caracteres'
        super().__init__(self.__mensagem, *args)

class SIException(Exception):
    def __init__(self, usuario, *args):
        self.__usuario = usuario
        self.__mensagem = f'Usuário "{usuario}" não pode seguir a si mesmo'
        super().__init__(self.__mensagem, *args)