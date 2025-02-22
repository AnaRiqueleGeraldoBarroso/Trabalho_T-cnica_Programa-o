from datetime import datetime

from execoes import UJCException, UNCException, PEException, PDException, PIException, MFPException, SIException

def gerador_id():
    id_atual = 1
    while True:
        yield id_atual
        id_atual += 1

gerador = gerador_id()

class Tweet():
    def __init__(self, usuario:str, mensagem:str):
        self.__usuario = usuario
        self.__mensagem = mensagem
        self.__data_postagem = datetime.now()
        self.__id_atual = next(gerador)

    def get_id(self):
        return self.__id_atual

    def get_usuario(self):
        return self.__usuario

    def get_mensagem(self):
        return self.__mensagem

    def get_postagem(self):
        return self.__data_postagem

class Perfil():
    def __init__(self, usuario:str):
        self.__usuario = usuario
        self.__seguidos = []
        self.__seguidores = []
        self.__tweets = []
        self.__ativo = True

    def add_seguidor(self, perfil):
        self.__seguidores.append(perfil)

    def add_seguidos(self, perfil):
        self.__seguidos.append(perfil)

    def add_tweet(self, tweet):
        self.__tweets.append(tweet)

    def get_tweets(self):
        return sorted(self.__tweets, key=lambda t: t.get_postagem(), reverse=True)

    def get_tweet(self, tweet_id):
        for tweet in self.__tweets:
            if tweet.get_id() == tweet_id:
                return tweet
        return None

    def get_timeline(self):
        timeline = self.__tweets[:]
        for perfil in self.__seguidos:
            timeline.extend(perfil.get_tweets())
        return sorted(timeline, key=lambda t: t.get_postagem())

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_usuario(self):
        return self.__usuario

    def set_ativo(self, ativo: bool):
        self.__ativo = ativo

    def is_ativo(self):
        return self.__ativo

    def get_seguidores(self):
        return self.__seguidores

    def get_seguidos(self):
        return self.__seguidos

class PessoaFisica(Perfil):
    def __init__(self, usuario, cpf):
        super().__init__(usuario)
        self.__cpf = cpf

    def get_cpf(self):
        return self.__cpf

class PessoaJuridica(Perfil):
    def __init__(self, usuario, cnpj):
        super().__init__(usuario)
        self.__cnpj = cnpj

    def get_cnpj(self):
        return self.__cnpj

class RepositorioUsuarios():
    def __init__(self):
        self.__usuarios = []

    def cadastrar(self, perfil):
        if self.buscar(perfil.get_usuario()) is not None:
            raise UJCException(perfil.get_usuario())
        self.__usuarios.append(perfil)

    def buscar(self, usuario):
        for perfil in self.__usuarios:
            if perfil.get_usuario() == usuario:
                return perfil
        return None

    def atualizar(self, perfil):
        usuario = self.buscar(perfil.get_usuario())
        if usuario is None:
            return UNCException(perfil.get_usuario())
        else:
            self.__usuarios.remove(perfil)
            self.__usuarios.append(perfil)

class MyTwitter():
    def __init__(self):
        self.__repositorios = RepositorioUsuarios()

    def criar_perfil(self, perfil):
        if self.__repositorios.buscar(perfil.get_usuario()) is not None:
            raise PEException(perfil.get_usuario())
        else:
            self.__repositorios.cadastrar(perfil)

    def cancelar_perfil(self, usuario):
        perfil = self.__repositorios.buscar(usuario)
        if perfil is not None:
            if perfil.is_ativo():
                perfil.set_ativo(False)
            else:
                raise PDException(usuario)
        else:
            raise PIException(usuario)

    def tweetar(self, usuario, texto):
        perfil = self.__repositorios.buscar(usuario)
        if perfil is not None:
            if perfil.is_ativo():
                if (len(texto) > 1) and (len(texto) < 141):
                    tweet = Tweet(usuario, texto)
                    perfil.add_tweet(tweet)
                else:
                    return MFPException(len(texto))
            else:
                raise PDException(usuario)
        else:
            raise PIException(usuario)

    def timeline(self, usuario):
        perfil = self.__repositorios.buscar(usuario)
        if perfil is not None:
            if perfil.is_ativo():
                return perfil.get_timeline()
            else:
                raise PDException(usuario)
        else:
            raise PIException(usuario)

    def tweets(self, usuario):
        perfil = self.__repositorios.buscar(usuario)
        if perfil is not None:
            if perfil.is_ativo():
                return perfil.get_tweets()
            else:
                raise PDException(usuario)
        else:
            return PIException(usuario)

    def seguir(self, seguidor, seguido):
        perfil_seguidor = self.__repositorios.buscar(seguidor)
        perfil_seguido = self.__repositorios.buscar(seguido)

        if seguidor != seguido:
            if perfil_seguidor is not None:
                if perfil_seguido is not None:
                    if perfil_seguidor.is_ativo():
                        if perfil_seguido.is_ativo():
                            perfil_seguido.add_seguidor(perfil_seguidor)
                            perfil_seguidor.add_seguidos(perfil_seguido)
                        else:
                            raise PDException(seguido)
                    else:
                        raise PDException(seguidor)
                else:
                    raise PIException(seguido)
            else:
                raise PIException(seguidor)
        else:
            raise SIException(seguidor)

    def numero_seguidor(self, usuario):
        perfil = self.__repositorios.buscar(usuario)
        if perfil is not None:
            if perfil.is_ativo():
                seguidores = 0
                for seguidor in perfil.get_seguidores():
                    if seguidor.is_ativo():
                        seguidores += 1
                return seguidores
            else:
                raise PDException(usuario)
        else:
            raise PIException(usuario)

    def seguidores(self, usuario):
        perfil = self.__repositorios.buscar(usuario)
        if perfil is not None:
            if perfil.is_ativo():
                seguidores = []
                for seguidor in perfil.get_seguidores():
                    if seguidor.is_ativo():
                        seguidores.append(seguidor)
                return seguidores
            else:
                raise PDException(usuario)
        else:
            raise PIException(usuario)

    def seguidos(self, usuario):
        perfil = self.__repositorios.buscar(usuario)
        if perfil is not None:
            if perfil.is_ativo():
                seguidos = []
                for seguidor in perfil.get_seguidos():
                    if seguidor.is_ativo():
                        seguidos.append(seguidor)
                return seguidos
            else:
                raise PDException(usuario)
        else:
            raise PIException(usuario)