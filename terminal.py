from execoes import UJCException, UNCException, PEException, PDException, PIException, MFPException, SIException
from MyTwitter import MyTwitter, PessoaFisica, PessoaJuridica

class MyTwitterTerminal:
    def __init__(self):
        self.my_twitter = MyTwitter()

    def menu(self):
        while True:
            print("\n--- Menu MyTwitter ---")
            print("1. Criar Perfil")
            print("2. Cancelar Perfil")
            print("3. Postar Tweet")
            print("4. Ver Timeline")
            print("5. Ver Tweets")
            print("6. Seguir Perfil")
            print("7. Ver Número de Seguidores")
            print("8. Ver Seguidores")
            print("9. Ver Seguidos")
            print("0. Sair")
            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.criar_perfil()
            elif choice == "2":
                self.cancelar_perfil()
            elif choice == "3":
                self.tweetar()
            elif choice == "4":
                self.ver_timeline()
            elif choice == "5":
                self.ver_tweets()
            elif choice == "6":
                self.seguir()
            elif choice == "7":
                self.ver_numero_seguidores()
            elif choice == "8":
                self.ver_seguidores()
            elif choice == "9":
                self.ver_seguidos()
            elif choice == "0":
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def criar_perfil(self):
        usuario = input("Digite o nome de usuário: ")
        tipo_perfil = input("Tipo de perfil (F: Pessoa Física, J: Pessoa Jurídica): ")
        if tipo_perfil == 'F':
            cpf = input("Digite o CPF: ")
            perfil = PessoaFisica(usuario, cpf)
        elif tipo_perfil == 'J':
            cnpj = input("Digite o CNPJ: ")
            perfil = PessoaJuridica(usuario, cnpj)
        else:
            print("Tipo de perfil inválido!")
            return
        try:
            self.my_twitter.criar_perfil(perfil)
            print(f"Perfil de {usuario} criado com sucesso!")
        except PEException as e:
            print(f"Erro: Perfil {e.get_usuario()} já existe.")

    def cancelar_perfil(self):
        usuario = input("Digite o nome de usuário para cancelar: ")
        try:
            self.my_twitter.cancelar_perfil(usuario)
            print(f"Perfil {usuario} desativado com sucesso!")
        except (PDException, PIException) as e:
            print(f"Erro: {str(e)}")

    def tweetar(self):
        usuario = input("Digite o nome de usuário: ")
        texto = input("Digite o texto do tweet (max. 140 caracteres): ")
        try:
            self.my_twitter.tweetar(usuario, texto)
            print("Tweet postado com sucesso!")
        except (PDException, PIException, MFPException) as e:
            print(f"Erro: {str(e)}")

    def ver_timeline(self):
        usuario = input("Digite o nome de usuário para ver a timeline: ")
        try:
            timeline = self.my_twitter.timeline(usuario)
            for tweet in timeline:
                print(f"{tweet.get_usuario()} ({tweet.get_postagem()}): {tweet.get_mensagem()}")
        except (PDException, PIException) as e:
            print(f"Erro: {str(e)}")

    def ver_tweets(self):
        usuario = input("Digite o nome de usuário para ver os tweets: ")
        try:
            tweets = self.my_twitter.tweets(usuario)
            for tweet in tweets:
                print(f"{tweet.get_usuario()} ({tweet.get_postagem()}): {tweet.get_mensagem()}")
        except (PDException, PIException) as e:
            print(f"Erro: {str(e)}")

    def seguir(self):
        seguidor = input("Digite o nome de usuário do seguidor: ")
        seguido = input("Digite o nome de usuário do seguido: ")
        try:
            self.my_twitter.seguir(seguidor, seguido)
            print(f"{seguidor} agora segue {seguido}!")
        except (PDException, PIException, SIException) as e:
            print(f"Erro: {str(e)}")

    def ver_numero_seguidores(self):
        usuario = input("Digite o nome de usuário para ver o número de seguidores: ")
        try:
            num_seguidores = self.my_twitter.numero_seguidor(usuario)
            print(f"{usuario} tem {num_seguidores} seguidores.")
        except (PDException, PIException) as e:
            print(f"Erro: {str(e)}")

    def ver_seguidores(self):
        usuario = input("Digite o nome de usuário para ver seus seguidores: ")
        try:
            seguidores = self.my_twitter.seguidores(usuario)
            print(f"Seguidores de {usuario}:")
            for seguidor in seguidores:
                print(seguidor.get_usuario())
        except (PDException, PIException) as e:
            print(f"Erro: {str(e)}")

    def ver_seguidos(self):
        usuario = input("Digite o nome de usuário para ver os seguidos: ")
        try:
            seguidos = self.my_twitter.seguidos(usuario)
            print(f"Seguidos de {usuario}:")
            for seguido in seguidos:
                print(seguido.get_usuario())
        except (PDException, PIException) as e:
            print(f"Erro: {str(e)}")


if __name__ == "__main__":
    terminal = MyTwitterTerminal()
    terminal.menu()
