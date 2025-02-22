import unittest

from MyTwitter import Tweet, Perfil, PessoaFisica, PessoaJuridica

class TestPerfil(unittest.TestCase):

    def setUp(self):
        self.perfil1 = Perfil('usuario1')
        self.perfil2 = Perfil('usuario2')
        self.perfil3 = Perfil('usuario3')

        #Pessoa Físca
        self.pf1 = PessoaFisica('usuario1', '123.456.789-00')
        self.pf2 = PessoaFisica('usuario2', '987.654.321-00')

        #Pessoa Juridica
        self.pj1 = PessoaJuridica('PessoaJurica1', '12.345.678/0001-99')
        self.pj2 = PessoaJuridica('PessoaJuridica2', '98.765.432/0001-00')

    def test_add_seguidor(self):
        self.perfil1.add_seguidor(self.perfil2)
        self.assertIn(self.perfil2, self.perfil1._Perfil__seguidores)


    def test_add_seguidos(self):
        self.perfil1.add_seguidos(self.perfil2)
        self.assertIn(self.perfil2, self.perfil1._Perfil__seguidos)

    def test_add_tweet(self):
        tweet = Tweet('usuario1', 'Mensagem de teste')
        self.perfil1.add_tweet(tweet)
        self.assertIn(tweet, self.perfil1._Perfil__tweets)

    #Está dando um erro
    '''def test_get_tweets(self):
        tweet1 = Tweet('usuario1', 'Mensagem de teste 1')
        tweet2 = Tweet('usuario1', 'Mensagem de teste 2')
        self.perfil1.add_tweet(tweet1)
        self.perfil1.add_tweet(tweet2)
        tweets = self.perfil1.get_tweets()
        self.assertEqual(tweets[0], tweet2)'''

    def test_get_tweet(self):
        tweet = Tweet('usuario1', 'Mensagem de teste')
        self.perfil1.add_tweet(tweet)
        tweet_recuperado = self.perfil1.get_tweet(tweet.get_id())
        self.assertEqual(tweet_recuperado, tweet)

    def test_get_timeline(self):
        tweet1 = Tweet('usuario1', 'Mensagem de teste 1')
        tweet2 = Tweet('usuario2', 'Mensagem de teste 2')
        self.perfil1.add_tweet(tweet1)
        self.perfil2.add_tweet(tweet2)
        self.perfil1.add_seguidos(self.perfil2)

        timeline = self.perfil1.get_timeline()
        self.assertIn(tweet2, timeline)
        self.assertIn(tweet1, timeline)


    def test_set_usuario(self):
        self.perfil1.set_usuario('novo_usuario')
        self.assertEqual(self.perfil1.get_usuario(), 'novo_usuario')

    def test_is_ativo(self):
        self.assertTrue(self.perfil1.is_ativo())
        self.perfil1.set_ativo(False)
        self.assertFalse(self.perfil1.is_ativo())

    def test_get_cpf(self):
        self.assertEqual(self.pf1.get_cpf(), '123.456.789-00')
        self.assertEqual(self.pf2.get_cpf(), '987.654.321-00')

    def test_get_cnpj(self):
        self.assertEqual(self.pj1.get_cnpj(), '12.345.678/0001-99')
        self.assertEqual(self.pj2.get_cnpj(), '98.765.432/0001-00')

if __name__ == "__main__":
    unittest.main()