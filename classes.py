class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 32
        self.marca = 'marca'

tv_quarto = Televisão()
tv_quarto.marca = 'samsung'
print(tv_quarto.ligada)
print(tv_quarto.canal)
print(tv_quarto.marca)

tv_sala = Televisão()
tv_sala.ligada = True
tv_sala.canal = 4
tv_sala.marca = 'TCL'
print(tv_sala.ligada)
print(tv_sala.canal)
print(tv_sala.marca)

