import pygame

class Botao:
    def __init__(self, imagem_ativa, imagem_inativa, x, y, escala=1, acao=None):
        self.imagem_ativa = pygame.image.load(imagem_ativa)
        self.imagem_inativa = pygame.image.load(imagem_inativa)
        self.imagem_ativa = pygame.transform.scale(self.imagem_ativa, (int(self.imagem_ativa.get_width() * escala), int(self.imagem_ativa.get_height() * escala)))
        self.imagem_inativa = pygame.transform.scale(self.imagem_inativa, (int(self.imagem_inativa.get_width() * escala), int(self.imagem_inativa.get_height() * escala)))
        self.x = x
        self.y = y
        self.largura = self.imagem_inativa.get_width()
        self.altura = self.imagem_inativa.get_height()
        self.acao = acao

    def desenhar(self, tela):
        mouse = pygame.mouse.get_pos()
        clique = pygame.mouse.get_pressed()

        retangulo_botao = pygame.Rect(self.x - self.largura // 2, self.y - self.altura // 2, self.largura, self.altura)

        if self.x + self.largura > mouse[0] > self.x and self.y + self.altura > mouse[1] > self.y:
            tela.blit(self.imagem_ativa, (self.x, self.y))
            if clique[0] == 1 and self.acao is not None:
                self.acao()
        else:
            tela.blit(self.imagem_inativa, (self.x, self.y))

    def verificar_clique(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  
            mouse = pygame.mouse.get_pos()
            if self.x + self.largura > mouse[0] > self.x and self.y + self.altura > mouse[1] > self.y:
                if self.acao is not None:
                    self.acao()
