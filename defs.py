import pygame
import sys

TAMANHO_GRADE = 100

def posicao_grade(linha, coluna, linhas, colunas, largura_tela, altura_tela):
    largura_celula = largura_tela // colunas
    altura_celula = altura_tela // linhas
    x = coluna * largura_celula
    y = linha * altura_celula
    return (x, y)

def sair_jogo():
    pygame.quit()
    sys.exit()