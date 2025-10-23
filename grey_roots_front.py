import pygame
import sys
from grey_roots_backend import GameState, Tela, QTEType

# --- CONFIGURAÇÕES ---
SCREEN_WIDTH, SCREEN_HEIGHT = 816, 624
FONT_COLOR = (240, 240, 240)
BG_COLOR = (24, 24, 24)
BUTTON_BG = (50, 50, 50)
BUTTON_FG = (220, 220, 220)
BUTTON_SELECTED = (120, 180, 220)

# --- INIT PYGAME ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Grey Roots")
font = pygame.font.SysFont("arial", 30)
clock = pygame.time.Clock()

def draw_text(surface, text, x, y, color=FONT_COLOR, center=False, max_width=None):
    lines = []
    if max_width:
        # Word wrap
        words = text.split(" ")
        line = ""
        for w in words:
            test = line + w + " "
            if font.size(test)[0] > max_width:
                lines.append(line)
                line = w + " "
            else:
                line = test
        lines.append(line)
    else:
        lines = text.split('\n')
    for line in lines:
        txt = font.render(line, True, color)
        rect = txt.get_rect()
        if center:
            rect.centerx = x
        else:
            rect.x = x
        rect.y = y
        surface.blit(txt, rect)
        y += 20 + 4

def draw_button(surface, text, rect, selected=False):
    color = BUTTON_SELECTED if selected else BUTTON_BG
    pygame.draw.rect(surface, color, rect, border_radius=5)
    txt = font.render(text, True, BUTTON_FG)
    trect = txt.get_rect(center=rect.center)
    surface.blit(txt, trect)

def input_box(surface, prompt, value, active, box_rect):
    pygame.draw.rect(surface, (40, 40, 60), box_rect, border_radius=5)
    draw_text(surface, prompt, box_rect.x + 8, box_rect.y + 8, BUTTON_FG)
    valtxt = font.render(value, True, (220, 220, 220))
    surface.blit(valtxt, (box_rect.x + 8, box_rect.y + 48))
    if active:
        pygame.draw.rect(surface, BUTTON_SELECTED, box_rect, 2, border_radius=5)

def main():
    background_img = pygame.image.load("img/tela_menu.png").convert()
    background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    game = GameState()
    game.start()
    running = True
    selected = 0
    user_input = ""
    input_active = False

    while running and not game.is_finished():
        screen.fill(BG_COLOR)
        textos = game.get_textos()
        escolhas = game.get_escolhas()
        tela = game.tela_atual
        # --- Display Text ---
        y = 40
        for t in textos[:6]:
            draw_text(screen, t, 60, y, FONT_COLOR, max_width=SCREEN_WIDTH-120)
            y += 20 + 10

        # --- Input / Buttons ---
        btns = []
        if escolhas:
            if escolhas[0] == "input":
                # Input box
                box_rect = pygame.Rect(60, y+10, SCREEN_WIDTH-120, 80)
                input_box(screen, "Digite e pressione ENTER:", user_input, input_active, box_rect)
            elif escolhas[0] == "qte":
                # QTE: mostre instrução na tela e aguarde tecla
                draw_text(screen, "QTE: Pressione a tecla correta!", 60, y+10, (200,160,60))
            else:
                # Botões de escolha
                spacing = 20
                btn_width = 350
                btn_height = 50
                bx = (SCREEN_WIDTH - btn_width) // 2
                by = y + 10
                for i, e in enumerate(escolhas):
                    rect = pygame.Rect(bx, by + i*(btn_height+spacing), btn_width, btn_height)
                    btns.append(rect)
                    draw_button(screen, e, rect, i == selected)
        pygame.display.flip()

        # --- Handle Events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if escolhas:
                    if escolhas[0] == "input":
                        input_active = True
                        if event.key == pygame.K_RETURN:
                            input_active = False
                            game.process_action("input", user_input)
                            user_input = ""
                        elif event.key == pygame.K_BACKSPACE:
                            user_input = user_input[:-1]
                        else:
                            c = event.unicode
                            if c.isprintable():
                                user_input += c
                    elif escolhas[0] == "qte":
                        # Simule QTE: pressione a tecla correta!
                        qte_config = game.last_qte_config
                        if qte_config and event.unicode == qte_config["key"]:
                            game.process_action("qte", "SUCESSO")
                        else:
                            game.process_action("qte", "FALHA")
                    else:
                        # Botões de escolha
                        if event.key in [pygame.K_UP, pygame.K_w]:
                            selected = (selected - 1) % len(escolhas)
                        elif event.key in [pygame.K_DOWN, pygame.K_s]:
                            selected = (selected + 1) % len(escolhas)
                        elif event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                            game.process_action("escolha", escolhas[selected])
                            selected = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btns:
                    for i, rect in enumerate(btns):
                        if rect.collidepoint(event.pos):
                            game.process_action("escolha", escolhas[i])
                            selected = 0

        clock.tick(30)

    # --- Tela de fim ---
    screen.fill(BG_COLOR)
    draw_text(screen, "Obrigado por jogar!", SCREEN_WIDTH//2, SCREEN_HEIGHT//2-50, FONT_COLOR, center=True)
    pygame.display.flip()
    pygame.time.wait(3500)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()