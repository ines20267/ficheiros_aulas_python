import pygame
import random
import sys

pygame.init()

# Janela
LARGURA = 800
ALTURA = 600

ecra = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Caça ao Tesouro")

# Cores
VERDE = (34, 177, 76)
BRANCO = (255, 255, 255)

# Fontes
fonte = pygame.font.SysFont(None, 40)
fonte_titulo = pygame.font.SysFont(None, 60)

# Imagens
imagem_gato = pygame.image.load("gato.png").convert_alpha()
imagem_peixe = pygame.image.load("peixe.png").convert_alpha()
imagem_cobra = pygame.image.load("cobra.png").convert_alpha()

# Redimensionar imagens
imagem_gato = pygame.transform.scale(imagem_gato, (60, 60))
imagem_peixe = pygame.transform.scale(imagem_peixe, (40, 40))
imagem_cobra = pygame.transform.scale(imagem_cobra, (40, 40))

# Gato
gato = pygame.Rect(380, 280, 60, 60)
velocidade = 5

# Peixe
peixe = pygame.Rect(
    random.randint(0, 760),
    random.randint(80, 560),
    40,
    40
)

# Cobra
cobra = pygame.Rect(
    random.randint(0, 760),
    random.randint(80, 560),
    40,
    40
)

# Velocidades
vel_peixe_x = 3
vel_peixe_y = 3

vel_cobra_x = 3
vel_cobra_y = 3

# Pontuação
pontos = 0

# Tempo
tempo_inicio = pygame.time.get_ticks()
duracao = 60

# Estado do jogo
estado = "jogo"

clock = pygame.time.Clock()

while True:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:

            if estado == "fim":

                if evento.key == pygame.K_r:

                    pontos = 0

                    gato.x = 380
                    gato.y = 280

                    peixe.x = random.randint(0, 760)
                    peixe.y = random.randint(80, 560)

                    cobra.x = random.randint(0, 760)
                    cobra.y = random.randint(80, 560)

                    tempo_inicio = pygame.time.get_ticks()

                    estado = "jogo"

    ecra.fill(VERDE)

    if estado == "jogo":

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT]:
            gato.x -= velocidade

        if teclas[pygame.K_RIGHT]:
            gato.x += velocidade

        if teclas[pygame.K_UP]:
            gato.y -= velocidade

        if teclas[pygame.K_DOWN]:
            gato.y += velocidade

        gato.clamp_ip(ecra.get_rect())

        # Movimento do peixe
        peixe.x += vel_peixe_x
        peixe.y += vel_peixe_y

        if peixe.left <= 0 or peixe.right >= LARGURA:
            vel_peixe_x *= -1

        if peixe.top <= 80 or peixe.bottom >= ALTURA:
            vel_peixe_y *= -1

        # Movimento da cobra
        cobra.x += vel_cobra_x
        cobra.y += vel_cobra_y

        if cobra.left <= 0 or cobra.right >= LARGURA:
            vel_cobra_x *= -1

        if cobra.top <= 80 or cobra.bottom >= ALTURA:
            vel_cobra_y *= -1

        # Colisão com peixe
        if gato.colliderect(peixe):

            pontos += 10

            peixe.x = random.randint(0, 760)
            peixe.y = random.randint(80, 560)

        # Colisão com cobra
        if gato.colliderect(cobra):

            pontos -= 10

            cobra.x = random.randint(0, 760)
            cobra.y = random.randint(80, 560)

        tempo_decorrido = (
            pygame.time.get_ticks() - tempo_inicio
        ) // 1000

        tempo_restante = duracao - tempo_decorrido

        if tempo_restante <= 0:
            estado = "fim"

        # Mostrar imagens
        ecra.blit(imagem_gato, (gato.x, gato.y))
        ecra.blit(imagem_peixe, (peixe.x, peixe.y))
        ecra.blit(imagem_cobra, (cobra.x, cobra.y))

        # Informações
        texto1 = fonte.render(
            f"Pontos: {pontos}",
            True,
            BRANCO
        )

        texto2 = fonte.render(
            f"Tempo: {tempo_restante}",
            True,
            BRANCO
        )

        texto3 = fonte.render(
            "Peixe = +10 ",
            True,
            BRANCO
        )

        texto4 = fonte.render(
            "Cobra = -10 ",
            True,
            BRANCO
        )

        ecra.blit(texto1, (10, 10))
        ecra.blit(texto2, (190, 10))
        ecra.blit(texto3, (360, 10))
        ecra.blit(texto4, (560, 10))

    if estado == "fim":

        titulo = fonte_titulo.render(
            "FIM DO JOGO",
            True,
            BRANCO
        )

        if pontos >= 100:
            resultado = "Mestre da Caça ao Tesouro!"

        if pontos >= 50 and pontos < 100:
            resultado = "Excelente Desempenho!"

        if pontos < 50:
            resultado = "Continua a Treinar!"

        texto1 = fonte.render(
            f"Pontuação Final: {pontos}",
            True,
            BRANCO
        )

        texto2 = fonte.render(
            resultado,
            True,
            BRANCO
        )

        texto3 = fonte.render(
            "Pressiona R para jogar novamente",
            True,
            BRANCO
        )

        ecra.blit(titulo, (170, 150))
        ecra.blit(texto1, (220, 270))
        ecra.blit(texto2, (220, 330))
        ecra.blit(texto3, (120, 450))

    pygame.display.flip()
    clock.tick(60)