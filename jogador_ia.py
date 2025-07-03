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
                elif self.matriz[l][c] == Tabuleiro.JOGADOR_0 and self.tipo == Tabuleiro.JOGADOR_X:
                    if c < 2 and self.matriz[l][c+1] == Tabuleiro.JOGADOR_0 and self.matriz[l][c+2] == Tabuleiro.DESCONHECIDO:
                        return (l, c+2)
                    elif c > 0 and c < 2 and self.matriz[l][c-1] == Tabuleiro.JOGADOR_0 and self.matriz[l][c+1] == Tabuleiro.DESCONHECIDO:
                        return (l, c+1)
                    elif c > 1 and self.matriz[l][c-1] == Tabuleiro.JOGADOR_0 and self.matriz[l][c-2] == Tabuleiro.DESCONHECIDO:
                        return (l, c-2)
                    elif l < 2 and self.matriz[l+1][c] == Tabuleiro.JOGADOR_0 and self.matriz[l+2][c] == Tabuleiro.DESCONHECIDO:
                        return (l+2, c)
                    elif l > 0 and l < 2 and self.matriz[l-1][c] == Tabuleiro.JOGADOR_0 and self.matriz[l+1][c] == Tabuleiro.DESCONHECIDO:
                        return (l+1, c)
                    elif l > 1 and self.matriz[l-1][c] == Tabuleiro.JOGADOR_0 and self.matriz[l-2][c] == Tabuleiro.DESCONHECIDO:
                        return (l-2, c)
                    elif l < 2 and c < 2 and self.matriz[l+1][c+1] == Tabuleiro.JOGADOR_0 and self.matriz[l+2][c+2] == Tabuleiro.DESCONHECIDO:
                        return (l+2, c+2)
                    elif l > 0 and l < 2 and c > 0 and c < 2 and self.matriz[l-1][c-1] == Tabuleiro.JOGADOR_0 and self.matriz[l+1][c+1] == Tabuleiro.DESCONHECIDO:
                        return (l+1, c+1)
                    elif l > 1 and c > 1 and self.matriz[l-1][c-1] == Tabuleiro.JOGADOR_0 and self.matriz[l-2][c-2] == Tabuleiro.DESCONHECIDO:
                        return (l-2, c-2)
                    elif l < 2 and c > 0 and self.matriz[l+1][c-1] == Tabuleiro.JOGADOR_0 and self.matriz[l+2][c-2] == Tabuleiro.DESCONHECIDO:
                        return (l+2, c-2)
                    elif l > 0 and l < 2 and c > 0 and c < 2 and self.matriz[l-1][c+1] == Tabuleiro.JOGADOR_0 and self.matriz[l+1][c-1] == Tabuleiro.DESCONHECIDO:
                        return (l+1, c-1)
                    elif l > 1 and c < 2 and self.matriz[l-1][c+1] == Tabuleiro.JOGADOR_0 and self.matriz[l-2][c-2] == Tabuleiro.DESCONHECIDO:
                        return (l-2, c-2)
                #Se houver uma jogada que crie duas sequências de duas marcações,use-a.
                elif self.matriz[l][c] == Tabuleiro.JOGADOR_X and self.tipo == Tabuleiro.JOGADOR_0:
                    if c < 2 and self.matriz[l][c+1] == Tabuleiro.JOGADOR_X and self.matriz[l][c+2] == Tabuleiro.DESCONHECIDO:
                        return (l, c+2)
                    elif c > 0 and c < 2 and self.matriz[l][c-1] == Tabuleiro.JOGADOR_X and self.matriz[l][c+1] == Tabuleiro.DESCONHECIDO:
                        return (l, c+1)
                    elif c > 1 and self.matriz[l][c-1] == Tabuleiro.JOGADOR_X and self.matriz[l][c-2] == Tabuleiro.DESCONHECIDO:
                        return (l, c-2)
                    elif l < 2 and self.matriz[l+1][c] == Tabuleiro.JOGADOR_X and self.matriz[l+2][c] == Tabuleiro.DESCONHECIDO:
                        return (l+2, c)
                    elif l > 0 and l < 2 and self.matriz[l-1][c] == Tabuleiro.JOGADOR_X and self.matriz[l+1][c] == Tabuleiro.DESCONHECIDO:
                        return (l+1, c)
                    elif l > 1 and self.matriz[l-1][c] == Tabuleiro.JOGADOR_X and self.matriz[l-2][c] == Tabuleiro.DESCONHECIDO:
                        return (l-2, c)
                    elif l < 2 and c < 2 and self.matriz[l+1][c+1] == Tabuleiro.JOGADOR_X and self.matriz[l+2][c+2] == Tabuleiro.DESCONHECIDO:
                        return (l+2, c+2)
                    elif l > 0 and l < 2 and c > 0 and c < 2 and self.matriz[l-1][c-1] == Tabuleiro.JOGADOR_X and self.matriz[l+1][c+1] == Tabuleiro.DESCONHECIDO:
                        return (l+1, c+1)
                    elif l > 1 and c > 1 and self.matriz[l-1][c-1] == Tabuleiro.JOGADOR_X and self.matriz[l-2][c-2] == Tabuleiro.DESCONHECIDO:
                        return (l-2, c-2)
                    elif l < 2 and c > 0 and self.matriz[l+1][c-1] == Tabuleiro.JOGADOR_X and self.matriz[l+2][c-2] == Tabuleiro.DESCONHECIDO:
                        return (l+2, c-2)
                    elif l > 0 and l < 2 and c > 0 and c < 2 and self.matriz[l-1][c+1] == Tabuleiro.JOGADOR_X and self.matriz[l+1][c-1] == Tabuleiro.DESCONHECIDO:
                        return (l+1, c-1)
                    elif l > 1 and c < 2 and self.matriz[l-1][c+1] == Tabuleiro.JOGADOR_X and self.matriz[l-2][c-2] == Tabuleiro.DESCONHECIDO:
                        return (l-2, c-2)
                    # R3. Se o quadrado central estiver livre, marque-o.
                    if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
                        return (1, 1)
                    # R4. Se o oponente marcou um canto, marque o canto oposto.
                    elif self.matriz[0][0] == Tabuleiro.JOGADOR_0 and self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
                        return (2, 2)
                    elif self.matriz[0][2] == Tabuleiro.JOGADOR_0 and self.matriz[2][0] == Tabuleiro.DESCONHECIDO:
                        return (2, 0)
                    elif self.matriz[2][0] == Tabuleiro.JOGADOR_0 and self.matriz[0][2] == Tabuleiro.DESCONHECIDO:
                        return (0, 2)
                    elif self.matriz[2][2] == Tabuleiro.JOGADOR_0 and self.matriz[0][0] == Tabuleiro.DESCONHECIDO:
                        return (0, 0)
                    # R5. If there is an empty corner, mark it.
                    elif self.matriz[0][0] == Tabuleiro.DESCONHECIDO:
                        return (0, 0)
                    elif self.matriz[0][2] == Tabuleiro.DESCONHECIDO:
                        return (0, 2)
                    elif self.matriz[2][0] == Tabuleiro.DESCONHECIDO:
                        return (2, 0)
                    elif self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
                        return (2, 2)
        if(len(lista) > 0):
            p = randint(0, len(lista)-1)
            return lista[p]
        else:
           return None
        