"""
responsible for user inout and maintaining current game state
"""
import pygame as p
from chess import chessEngine
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 18
IMAGES = { }

# Loading images need to be done one time only , function loadimages will initialise a global dict of images
# and this will be called once

def loadImages():
    pieces = ['wp','wR','wN','wB','wK','wQ','bp','bR','bN','bB','bK','bQ']
    for piece in pieces :
          IMAGES[piece] = p.transform.scale(p.image.load("images/"+piece+".png"),(SQ_SIZE,SQ_SIZE))


# MAIN Driver handling user inputs and updating graphics

def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessEngine.GameState()
    loadImages()
    running = True
    while running :
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

def drawGameState(screen , gs):
    drawBoard(screen)
    drawPieces(screen , gs.board)


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]

    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Draw the pieces on the board using the current GameState.board

def drawPieces(screen, board):
    for r in range(len(board)):  # r is the row index
        for c in range(DIMENSION):  # c is the column index
            piece = board[r][c]
            if piece != "--":  # not empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()

