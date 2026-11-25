
import pygame
import sys
import math
import random

pygame.init()

LARGURA = 1000
ALTURA = 650

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("THE LAST EXIT")
relogio = pygame.time.Clock()

FUNDO = (9, 10, 14)
BRANCO = (235, 235, 235)
CINZA = (145, 145, 155)
VERMELHO = (190, 35, 45)
VERMELHO_CLARO = (255, 55, 65)
PAINEL = (18, 19, 25)

fonte_titulo = pygame.font.Font(None, 82)
fonte_subtitulo = pygame.font.Font(None, 24)
fonte_botao = pygame.font.Font(None, 32)
fonte_pequena = pygame.font.Font(None, 21)
fonte_grande = pygame.font.Font(None, 48)

estado = "menu"
tempo = 0

particulas = []

for i in range(65):
    particulas.append([
        random.randint(0, LARGURA),
        random.randint(0, ALTURA),
        random.uniform(10, 35),
        random.randint(1, 3)
    ])


def texto(conteudo, fonte, cor, x, y):
    imagem = fonte.render(conteudo, True, cor)
    tela.blit(imagem, imagem.get_rect(center=(x, y)))


def desenhar_fundo():
    tela.fill(FUNDO)

    luz = 12 + int(math.sin(tempo * 0.8) * 5)
    pygame.draw.rect(
        tela, (luz + 8, 5, 10),
        (0, 0, LARGURA, ALTURA)
    )

    pygame.draw.line(
        tela, (45, 20, 25),
        (0, 0), (LARGURA, ALTURA), 1
    )
    pygame.draw.line(
        tela, (30, 25, 30),
        (LARGURA, 0), (0, ALTURA), 1
    )

    for p in particulas:
        p[1] -= p[2] * 0.016

        if p[1] < 0:
            p[1] = ALTURA
            p[0] = random.randint(0, LARGURA)

        pygame.draw.circle(
            tela, (p[3] * 35, 15, 20),
            (int(p[0]), int(p[1])), p[3]
        )


def botao(nome, x, y, largura, altura, mouse):
    retangulo = pygame.Rect(x, y, largura, altura)
    em_cima = retangulo.collidepoint(mouse)

    if em_cima:
        cor_fundo = (45, 18, 24)
        cor_borda = VERMELHO_CLARO
        cor_texto = BRANCO
    else:
        cor_fundo = PAINEL
        cor_borda = (65, 35, 40)
        cor_texto = CINZA

    pygame.draw.rect(
        tela, cor_fundo, retangulo, border_radius=4
    )
    pygame.draw.rect(
        tela, cor_borda, retangulo, 2, border_radius=4
    )
    pygame.draw.rect(
        tela, cor_borda,
        (x, y, 4, altura), border_radius=2
    )

    texto(
        nome, fonte_botao, cor_texto,
        x + largura // 2, y + altura // 2
    )

    return retangulo


def pegar_botao(x, y, largura, altura, mouse):
    return pygame.Rect(
        x, y, largura, altura
    ).collidepoint(mouse)


def menu_principal(mouse):
    desenhar_fundo()

    texto("THE LAST EXIT", fonte_titulo, BRANCO, 350, 155)
    texto(
        "AN ESCAPE ROOM EXPERIENCE",
        fonte_subtitulo, VERMELHO, 350, 205
    )

    pygame.draw.line(
        tela, VERMELHO, (175, 235), (525, 235), 2
    )

    botao("CONTINUAR", 210, 290, 280, 52, mouse)
    botao("NOVO JOGO", 210, 360, 280, 52, mouse)
    botao("CONFIGURACOES", 210, 430, 280, 52, mouse)
    botao("SAIR", 210, 500, 280, 45, mouse)

    pygame.draw.rect(
        tela, (22, 20, 25),
        (610, 270, 280, 220), border_radius=5
    )
    pygame.draw.rect(
        tela, (75, 30, 38),
        (610, 270, 280, 220), 2, border_radius=5
    )

    texto(
        "ARQUIVO 001", fonte_pequena,
        VERMELHO, 750, 300
    )
    texto("VOCE ESTA", fonte_grande, BRANCO, 750, 350)
    texto("SOZINHO.", fonte_grande, BRANCO, 750, 395)
    texto(
        "Encontre a saida.", fonte_pequena,
        CINZA, 750, 450
    )

    texto("VERSAO 0.1", fonte_pequena, CINZA, 80, 620)
    texto(
        "ESCAPE ROOM PROJECT",
        fonte_pequena, CINZA, 850, 620
    )


def menu_novo_jogo(mouse):
    desenhar_fundo()

    texto("NOVO JOGO", fonte_titulo, BRANCO, 500, 130)
    texto(
        "ESCOLHA SEU MODO DE JOGO",
        fonte_subtitulo, VERMELHO, 500, 185
    )

    botao("TUTORIAL", 350, 240, 300, 55, mouse)
    botao("HISTORIA", 350, 315, 300, 55, mouse)
    botao("DESAFIO", 350, 390, 300, 55, mouse)
    botao("VOLTAR", 350, 490, 300, 50, mouse)

    texto(
        "Cada modo tera sua propria experiencia.",
        fonte_pequena, CINZA, 500, 570
    )


def desenhar_pagina(titulo_pagina, descricao, mouse):
    desenhar_fundo()

    texto(
        titulo_pagina, fonte_grande,
        BRANCO, 500, 180
    )
    texto(
        descricao, fonte_subtitulo,
        CINZA, 500, 245
    )

    botao("VOLTAR AO MENU", 350, 470, 300, 60, mouse)


while True:
    tempo += 0.016
    mouse = pygame.mouse.get_pos()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                if estado == "novo_jogo":
                    estado = "menu"
                elif estado != "menu":
                    estado = "menu"

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:

                if estado == "menu":
                    if pegar_botao(210, 290, 280, 52, mouse):
                        estado = "continuar"

                    elif pegar_botao(210, 360, 280, 52, mouse):
                        estado = "novo_jogo"

                    elif pegar_botao(210, 430, 280, 52, mouse):
                        estado = "configuracoes"

                    elif pegar_botao(210, 500, 280, 45, mouse):
                        pygame.quit()
                        sys.exit()

                elif estado == "novo_jogo":
                    if pegar_botao(350, 240, 300, 55, mouse):
                        estado = "tutorial"

                    elif pegar_botao(350, 315, 300, 55, mouse):
                        estado = "historia"

                    elif pegar_botao(350, 390, 300, 55, mouse):
                        estado = "desafio"

                    elif pegar_botao(350, 490, 300, 50, mouse):
                        estado = "menu"

                elif estado in (
                    "continuar", "configuracoes",
                    "tutorial", "historia", "desafio"
                ):
                    if pegar_botao(350, 470, 300, 60, mouse):
                        estado = (
                            "novo_jogo"
                            if estado in (
                                "tutorial", "historia", "desafio"
                            )
                            else "menu"
                        )

    if estado == "menu":
        menu_principal(mouse)

    elif estado == "novo_jogo":
        menu_novo_jogo(mouse)

    elif estado == "continuar":
        desenhar_pagina(
            "CONTINUAR",
            "Ainda nao existe um salvamento.",
            mouse
        )

    elif estado == "configuracoes":
        desenhar_pagina(
            "CONFIGURACOES",
            "Personalizacao em breve.",
            mouse
        )

    elif estado == "tutorial":
        desenhar_pagina(
            "TUTORIAL",
            "Aprenda as mecanicas do jogo.",
            mouse
        )

    elif estado == "historia":
        desenhar_pagina(
            "HISTORIA",
            "Descubra o que aconteceu neste lugar.",
            mouse
        )

    elif estado == "desafio":
        desenhar_pagina(
            "DESAFIO",
            "Resolva os enigmas contra o tempo.",
            mouse
        )

    pygame.display.flip()
    relogio.tick(60)
