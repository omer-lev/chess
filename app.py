import pygame
from setup import *

pygame.init()

win_width = 800
win_height = 800

win = pygame.display.set_mode((win_width, win_height))
title = pygame.display.set_caption("Chess")

clock = pygame.time.Clock()

cursor_img = pygame.image.load('img/pointer.png')

# pawns
whitePawnImg = pygame.image.load('img/white_pawn.png')
blackPawnImg = pygame.image.load('img/black_pawn.png')

# bishops
whiteBishopImg = pygame.image.load('img/white_bishop.png')
blackBishopImg = pygame.image.load('img/black_bishop.png')

# knights
whiteKnightImg = pygame.image.load('img/white_knight.png')
blackKnightImg = pygame.image.load('img/black_knight.png')

# rooks
whiteRookImg = pygame.image.load('img/white_rook.png')
blackRookImg = pygame.image.load('img/black_rook.png')

# queens
whiteQueenImg = pygame.image.load('img/white_queen.png')
blackQueenImg = pygame.image.load('img/black_queen.png')

# kings
whiteKingImg = pygame.image.load('img/white_king.png')
blackKingImg = pygame.image.load('img/black_king.png')


class Pawn(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win, color):
        if color:
            win.blit(whitePawnImg, (self.x, self.y))
        
        else:
            win.blit(blackPawnImg, (self.x, self.y))


class Bishop(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win, color):
        if color:
            win.blit(whiteBishopImg, (self.x, self.y))
        
        else:
            win.blit(blackBishopImg, (self.x, self.y))


class Knight(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win, color):
        if color:
            win.blit(whiteKnightImg, (self.x, self.y))
        
        else:
            win.blit(blackKnightImg, (self.x, self.y))


class Rook(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win, color):
        if color:
            win.blit(whiteRookImg, (self.x, self.y))
        
        else:
            win.blit(blackRookImg, (self.x, self.y))


class Queen(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win, color):
        if color:
            win.blit(whiteQueenImg, (self.x, self.y))
        
        else:
            win.blit(blackQueenImg, (self.x, self.y))


class King(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win, color):
        if color:
            win.blit(whiteKingImg, (self.x, self.y))
        
        else:
            win.blit(blackKingImg, (self.x, self.y))


def boardSetup():
    height = 0

    for i in range(len(squares)):
        key = list(squares[i].keys())[0]
        x = squares[i][key][0]
        y = squares[i][key][1]

        # board
        if i % 8 == 0 and i != 0:
            height += 1

        if (i+height) % 2 == 0:
            pygame.draw.rect(win, (179, 208, 255), (x, y, 100, 100))
        
        else:
            pygame.draw.rect(win, (66, 135, 245), (x, y, 100, 100))

        # pawns
        if y == 100 and len(blackPawns) <= 7:
            blackPawns.append(Pawn(x + 15, y + 15))
        
        elif y == 600 and len(whitePawns) <= 7:
            whitePawns.append(Pawn(x + 15, y + 15))

        
        # white pieces
        elif y == 700:
            # bishops
            if (x == 200 or x == 500) and len(whiteBishops) <= 1:
                whiteBishops.append(Bishop(x + 4, y + 3))

            # knights
            if (x == 100 or x == 600) and len(whiteKnights) <= 1:
                whiteKnights.append(Knight(x + 4, y + 3))

            # rooks
            if (x == 0 or x == 700) and len(whiteRooks) <= 1:
                whiteRooks.append(Rook(x - 3, y + 15))

            # queen
            if x == 300 and len(whiteQueen) <= 0:
                whiteQueen.append(Queen(x + 4, y + 6))

            # king
            if x == 400 and len(whiteKing) <= 0:
                whiteKing.append(King(x + 4, y + 6))

        
         # black pieces
        if y == 0:
            # bishops
            if (x == 200 or x == 500) and len(blackBishops) <= 1:
                blackBishops.append(Bishop(x + 1, y + 3))
            
            # knights
            if (x == 100 or x == 600) and len(blackKnights) <= 1:
                blackKnights.append(Knight(x + 4, y + 3))

            # rooks
            if (x == 0 or x == 700) and len(blackRooks) <= 1:
                blackRooks.append(Rook(x + 3, y + 5))

            # queen
            if x == 300 and len(blackQueen) <= 0:
                blackQueen.append(Queen(x + 5, y + 5))

            # king
            if x == 400 and len(blackKing) <= 0:
                blackKing.append(King(x + 5, y + 5))



def pieceSetup():
    # pawns
    for pawn in whitePawns:
        pawn.draw(win, True)
    
    for pawn in blackPawns:
        pawn.draw(win, False)

    # bishops
    for bishop in whiteBishops:
        bishop.draw(win, True)
    
    for bishop in blackBishops:
        bishop.draw(win, False)

    # knights
    for knight in whiteKnights:
        knight.draw(win, True)
    
    for knight in blackKnights:
        knight.draw(win, False)

    # rooks
    for rook in whiteRooks:
        rook.draw(win, True)
    
    for rook in blackRooks:
        rook.draw(win, False)

    # queens
    for queen in whiteQueen:
        queen.draw(win, True)
    
    for queen in blackQueen:
        queen.draw(win, False)

    # kings
    for king in whiteKing:
        king.draw(win, True)
    
    for king in blackKing:
        king.draw(win, False)


def redraw():
    boardSetup()
    pieceSetup()

    pygame.display.update()


run = True
while run:
    clock.tick(60)
    redraw()

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    
    # testing
    for pawn in whitePawns:
        pawn.y -= 1

    for pawn in blackPawns:
        pawn.y += 1

    for pawn in whiteRooks:
        pawn.y -= 1

    for pawn in blackRooks:
        pawn.y += 1

    for pawn in whiteBishops:
        pawn.y -= 1

    for pawn in blackBishops:
        pawn.y += 1

    for pawn in whiteKnights:
        pawn.y -= 1

    for pawn in blackKnights:
        pawn.y += 1

    for pawn in whiteQueen:
        pawn.y -= 1

    for pawn in blackQueen:
        pawn.y += 1

    for pawn in whiteKing:
        pawn.y -= 1

    for pawn in blackKing:
        pawn.y += 1
    

pygame.quit()