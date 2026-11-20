import pygame
import sys

pygame.init()

# Configurações
LARGURA = 800
ALTURA = 600
ECRA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("MissãoBlocos")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 100, 255)
VERMELHO = (255, 50, 50)

# Barra
barra = pygame.Rect(350, 550, 100, 15)
vel_barra = 7

# Bola
bola = pygame.Rect(390, 300, 20, 20)
vel_x = 4
vel_y = -4

# Pontuação
pontos = 0
fonte = pygame.font.SysFont(None, 36)

# Blocos
blocos = []

for linha in range(5):
    for coluna in range(10):
        bloco = pygame.Rect(
            coluna * 75 + 25,
            linha * 35 + 40,
            70,
            25
        )
        blocos.append(bloco)

clock = pygame.time.Clock()

while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Teclas
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        barra.x -= vel_barra

    if teclas[pygame.K_RIGHT]:
        barra.x += vel_barra

    barra.clamp_ip(ECRA.get_rect())

    # Movimento da bola
    bola.x += vel_x
    bola.y += vel_y

    # Colisão com paredes
    if bola.left <= 0 or bola.right >= LARGURA:
        vel_x *= -1

    if bola.top <= 0:
        vel_y *= -1

    # Colisão com a barra
    if bola.colliderect(barra):
        vel_y *= -1

    # Colisão com blocos
    for bloco in blocos[:]:
        if bola.colliderect(bloco):
            blocos.remove(bloco)
            pontos += 5
            vel_y *= -1
            break

    # Perdeu
    if bola.bottom >= ALTURA:
        print("GAME OVER")
        pontos = 0
        bola.x = 390
        bola.y = 300
        vel_y = -4

    # Ganhou
    if len(blocos) == 0:
        print("VENCESTE!")

        blocos = []

        for linha in range(5):
            for coluna in range(10):
                bloco = pygame.Rect(
                    coluna * 75 + 25,
                    linha * 35 + 40,
                    70,
                    25
                )
                blocos.append(bloco)

        pontos = 0

    # Desenhar
    ECRA.fill(PRETO)

    pygame.draw.rect(ECRA, AZUL, barra)
    pygame.draw.ellipse(ECRA, BRANCO, bola)

    for bloco in blocos:
        pygame.draw.rect(ECRA, VERMELHO, bloco)

    texto = fonte.render(
        f"Pontos: {pontos}",
        True,
        BRANCO
    )

    ECRA.blit(texto, (10, 10))

    pygame.display.flip()
    clock.tick(60)