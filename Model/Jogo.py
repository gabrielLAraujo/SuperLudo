import random
# __all__ = ['NovoJogo', 'GetVez']

class Jogo:

    def __init__(self):
        self.count = 0
        self.jogadores = []
    
    def NovoJogo(self):
        global vez
        vez = -1
        

    def LancaDado(self):
        return random.randint(1,6)
    def GetVez(self):
        global vez
        return vez
    # def TirouSeis(self):
    #     if(count == 3)
            #retornar ultimo peao pra casa inicial 
        # count = count +1

    # def TirouUm(self)

    # def ECasaFinal(self)

    # def ECasaInicial(self)

    # def ECasaDeEntrada(self)

    # def PossuiTorre(self)

    # def PossuiTodosPinosNaCasa(self)

    # def QtdCasaRestantes(self)

    # def FinalizaJogo(self)