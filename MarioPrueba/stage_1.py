import pygame

# Inicialización de Pygame
pygame.init()

# Pantalla - ventana
W, H = 800, 600
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mario Bros")
icono = pygame.image.load("img/icon/icono.png")
pygame.display.set_icon(icono)

# Fondo del juego
fondo = pygame.image.load("img/background/stage1.jfif")

# Musica
pygame.mixer.music.load("music/world1.ogg")
pygame.mixer.music.play(-1)

quieto = pygame.image.load("img/walk_mario/der/walk0.png")

caminaDerecha = [pygame.image.load("img/walk_mario/der/walk1.png"),
                 pygame.image.load("img/walk_mario/der/walk2.png"),
                 pygame.image.load("img/walk_mario/der/walk3.png")]

caminaIzquierda = [pygame.image.load("img/walk_mario/izq/walk1.png"),
                 pygame.image.load("img/walk_mario/izq/walk2.png"),
                 pygame.image.load("img/walk_mario/izq/walk3.png")]

# Sonido
sonido_arriba = pygame.image.load('music/controls_volume/volume_up.png')
sonido_abajo = pygame.image.load('music/controls_volume/volume_down.png')
sonido_mute = pygame.image.load('music/controls_volume/volume_muted.png')
sonido_max = pygame.image.load('music/controls_volume/volume_max.png')

x = 0
px = 50
py = 460 #416
ancho = 40 #40
velocidad = 10

# Control d FPS
reloj = pygame.time.Clock()

# Variables salto
salto = False

# Contador de salto
cuentaSalto = 10

# Variables dirección
izquierda = False
derecha = False

# Pasos
cuentaPasos = 0


# Movimiento
def recarga_pantalla():
    # Variables globales
    global cuentaPasos
    global x

    # Fondo en movimiento
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < W:
        PANTALLA.blit(fondo, (x_relativa, 0))
    x -= 2

    # Contador de pasos
    if cuentaPasos + 1 >= 3:
        cuentaPasos = 0

    # Movimiento a la izquierda
    if izquierda:
        PANTALLA.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    # Movimiento a la derecha
    elif derecha:
        PANTALLA.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    # Salto
    elif salto + 1 >= 2:
        PANTALLA.blit(salta[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    else:
        PANTALLA.blit(quieto, (int(px), int(py)))

ejecuta = True
# Bucle de acciones y controles
while ejecuta:
    # FPS
    reloj.tick(18)

    # Bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    # Opción detectar tecla pulsada
    keys = pygame.key.get_pressed()

    # Tecla A - Movimiento a la izquierda
    if keys[pygame.K_LEFT] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False

    # Flecha derecha - Movimiento a la derecha
    elif keys[pygame.K_RIGHT] and px < 900 - velocidad - ancho:
        px += velocidad
        izquierda = False
        derecha = True

    # Personaje quieto
    else:
        izquierda = False
        derecha = False
        cuentaPasos = 0

    # Tecla W - Movimiento hacia arriba
    if keys[pygame.K_w] and py > 100:
        py -= velocidad

    # Tecla S - Movimiento hacia abajo
    if keys[pygame.K_s] and py < 300:
        py += velocidad

    # Tecla SPACE - Salto
    if not salto:
        if keys[pygame.K_SPACE]:
            salto = True
            izquierda = False
            derecha = False
            cuentaPasos = 0

    else:
        if cuentaSalto >= -10:
            py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
            cuentaSalto -= 1
        else:
            cuentaSalto = 10
            salto = False

    # Control del audio
    # Baja volumen
    if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
        PANTALLA.blit(sonido_abajo, (650, 25))

    elif keys[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
        PANTALLA.blit(sonido_mute, (650, 25))

    # Sube volumen
    if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        PANTALLA.blit(sonido_arriba, (650, 25))

    elif keys[pygame.K_0] and pygame.mixer.music.get_volume() == 1.0:
        PANTALLA.blit(sonido_max, (650, 25))

    # Desactivar sonido
    elif keys[pygame.K_m]:
        pygame.mixer.music.set_volume(0.0)
        PANTALLA.blit(sonido_mute, (650, 25))

    # Reactivar sonido
    elif keys[pygame.K_COMMA]:
        pygame.mixer.music.set_volume(1.0)
        PANTALLA.blit(sonido_max, (650, 25))

    # Actualización de la ventana
    pygame.display.update()

    # Llamada a la función dqe actualización de la ventana
    recarga_pantalla()

# Salida del juego
pygame.quit()