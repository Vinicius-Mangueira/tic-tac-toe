# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            

    def getJogada(self) -> (int, int):
        lista = []
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))
                # Se você ou seu oponente tiver duas marcações em sequência, marque o quadrado restante. 
                if self.matriz[l][c] == self.tipo:
                    # Verifica linhas
                    if c < 2 and self.matriz[l][c+1] == self.tipo:
                        if c == 0 and self.matriz[l][c+2] == Tabuleiro.DESCONHECIDO:
                            return (l, c+2)
                        elif c == 1 and self.matriz[l][c-1] == Tabuleiro.DESCONHECIDO:
                            return (l, c-1)
                    # Verifica colunas
                    if l < 2 and self.matriz[l+1][c] == self.tipo:
                        if l == 0 and self.matriz[l+2][c] == Tabuleiro.DESCONHECIDO:
                            return (l+2, c)
                        elif l == 1 and self.matriz[l-1][c] == Tabuleiro.DESCONHECIDO:
                            return (l-1, c)
                    # Verifica diagonal principal
                    if l < 2 and c < 2 and self.matriz[l+1][c+1] == self.tipo:
                        if l == 0 and c == 0 and self.matriz[l+2][c+2] == Tabuleiro.DESCONHECIDO:
                            return (l+2, c+2)
                        elif l == 1 and c == 1 and self.matriz[l-1][c-1] == Tabuleiro.DESCONHECIDO:
                            return (l-1, c-1)
                    # Verifica diagonal secundária
                    if l < 2 and c > 0 and self.matriz[l+1][c-1] == self.tipo:
                        if l == 0 and c == 2 and self.matriz[l+2][c-2] == Tabuleiro.DESCONHECIDO:
                            return (l+2, c-2)
                        elif l == 1 and c == 1 and self.matriz[l-1][c+1] == Tabuleiro.DESCONHECIDO:
                            return (l-1, c+1)

        if(len(lista) > 0):
            p = randint(0, len(lista)-1)
            return lista[p]
        else:
           return None
        