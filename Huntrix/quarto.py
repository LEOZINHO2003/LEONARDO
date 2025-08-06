class Quarto:
    def __init__(self, numero, tipo, preco_diaria, disponivel):
        self.numero = numero
        self.tipo = tipo
        self.preco_diaria = preco_diaria
        self.disponivel = disponivel

    def exibir_detalhes(self):
        print(f"Quarto {self.numero}")
        print(f"Tipo: {self.tipo}")
        print(f"Preço da diária: R${self.preco_diaria:.2f}")
        print(f"Status: {'Disponível' if self.disponivel else 'Ocupado'}")

    def reservar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O quarto {self.numero} foi reservado com sucesso!")
        else:
            print(f"O quarto {self.numero} já está ocupado.")

    def liberar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O quarto {self.numero} já está disponível.")
        else:
            print(f"O quarto {self.numero} foi liberado.")

    def alterar_preco(self, novo_preco):
        self.preco_diaria = novo_preco
        print(f"Novo valor da diária do quarto {self.numero}: R${self.preco_diaria:.2f}")
