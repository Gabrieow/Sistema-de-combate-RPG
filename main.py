import pygame
import sys
import classesif
import defs
import os

# Configurações de FPS
FPS = 60
clock = pygame.time.Clock()

# Inicialização do Pygame
pygame.init()

info = pygame.display.Info()
tela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
largura_tela, altura_tela = info.current_w, info.current_h
linhas = 100
colunas = 100
x_fundo, y_fundo = defs.posicao_grade(0, 0, linhas, colunas, largura_tela, altura_tela)

# Carregar fundo uma única vez
fundo = pygame.image.load('background_img.jpg')
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))

# Inicializando estado
estado_atual = "menu"

# Função de menu
def menu():
    x_iniciar, y_iniciar = defs.posicao_grade(45, 40, linhas, colunas, largura_tela, altura_tela)
    botao_iniciar = classesif.Botao('start_button_active.png', 'start_button_inactive.png', x_iniciar, y_iniciar, escala=0.2)

    x_opcoes, y_opcoes = defs.posicao_grade(60, 42.6, linhas, colunas, largura_tela, altura_tela)
    botao_opcoes = classesif.Botao('options_button_active.png', 'options_button_inactive.png', x_opcoes, y_opcoes, escala=0.15)

    x_creditos, y_creditos = defs.posicao_grade(71.4, 42.6, linhas, colunas, largura_tela, altura_tela)
    botao_creditos = classesif.Botao('credits_button_active.png', 'credits_button_inactive.png', x_creditos, y_creditos, escala=0.15)

    x_sair, y_sair = defs.posicao_grade(82.8, 42.6, linhas, colunas, largura_tela, altura_tela)
    botao_sair = classesif.Botao('exit_button_active.png', 'exit_button_inactive.png', x_sair, y_sair, escala=0.15)

    # Desenhando a tela de fundo e os botões
    tela.fill((0, 0, 0))  # Preenche com preto (opcional, dependendo do estilo)
    tela.blit(fundo, (x_fundo, y_fundo))
    botao_iniciar.desenhar(tela)
    botao_opcoes.desenhar(tela)
    botao_creditos.desenhar(tela)
    botao_sair.desenhar(tela)

    return "menu"

# Função de jogo
def jogo():
    tela.fill((0, 0, 0))
    tela.blit(fundo, (x_fundo, y_fundo))

    # Lógica do jogo aqui

    return "jogo"

# Função de opções
def opcoes():
    tela.fill((0, 0, 0))
    tela.blit(fundo, (x_fundo, y_fundo))

    # Lógica de opções aqui

    return "opcoes"

# Função de créditos
def creditos():
    tela.fill((0, 0, 0))
    tela.blit(fundo, (x_fundo, y_fundo))

    # Lógica de créditos aqui

    return "creditos"

# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
    
    # Definir o estado atual
    if estado_atual == "menu":
        estado_atual = menu()
    elif estado_atual == "jogo":
        estado_atual = jogo()
    elif estado_atual == "opcoes":
        estado_atual = opcoes()
    elif estado_atual == "creditos":
        estado_atual = creditos()

    # Atualiza a tela uma vez por ciclo
    pygame.display.update()

    # Controle de FPS
    clock.tick(FPS)

pygame.quit()
