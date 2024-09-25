class AutomatoQ1:

    def __init__(self):

        self.estados = {0,1,2}
        self.alfabeto = {'a','b','c'}
        self.transiçoes = {
            (0, 'a'): 1,
            (1, 'a'): 0,
            (1, 'b'): 1,
            (1, 'c'): 2,
            (2, 'a'): 1,
            (2, 'c'): 2,
        }

        self.estado_inicial = 0
        self.estados_finais = {0,1,2}

    def processar_cadeia(self, cadeia):
        estado_atual = self.estado_inicial

        cont =0
        while(cont<= (len(cadeia) -1) ):
            if((estado_atual, cadeia[cont]) in self.transiçoes):
                estado_atual = self.transiçoes[(estado_atual, cadeia[cont])]
                cont+=1
                

            else:
                return False

        return estado_atual in self.estados_finais


automato1 = AutomatoQ1()
print(automato1.processar_cadeia("abaacabbbccabcacaaabbbccabacacabcb"))