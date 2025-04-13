import pygame as pg
from os import path
import engine as eng

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = WIDTH // 8
MAX_FPS = 15

# initialized in load_images()
IMAGES = {}


def load_images():
    images_path = "assets/images/default_pieces"

    pieces = ["bR", "bN", "bB", "bQ", "bK", "bp", "wR", "wN", "wB", "wQ", "wK", "wp"]

    for p in pieces:
        IMAGES[p] = pg.transform.scale(
            pg.image.load(path.join(images_path, p + ".png")), (SQ_SIZE, SQ_SIZE)
        )


def main():
    # initial pygame setup
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    gs = eng.GameState()

    # one-time load of piece pngs.
    load_images()

    running = True
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                running = False
        clock.tick(MAX_FPS)
        pg.display.flip()
        draw_game_state(screen, gs)

    # exit if no longer running
    pg.quit()


def draw_game_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)


def draw_board(screen):
    colors = (pg.Color("white"), pg.Color("darkgreen"))

    for r in range(DIMENSION):
        for c in range(DIMENSION):
            sq_color = colors[(r + c) % 2]
            pg.draw.rect(
                screen, sq_color, pg.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE)
            )


def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(
                    IMAGES[piece], pg.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                )


if __name__ == "__main__":
    main()
