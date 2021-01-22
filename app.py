import pygame
from setup import *

pygame.init()

win_width = 800
win_height = 900

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
        self.name = "pawn"
    
    def move(self, pos):
        for i in range(len(squares)):
            key = list(squares[i].keys())[0]
            x = squares[i][key][0]
            y = squares[i][key][1]

            if y <= pos[1] and y + 100 >= pos[1]:
                if x <= pos[0] and x + 100 >= pos[0]:
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
        self.name = "bishop"
    
    def move(self, pos):
        for i in range(len(squares)):
            key = list(squares[i].keys())[0]
            x = squares[i][key][0]
            y = squares[i][key][1]

            if y <= pos[1] and y + 100 >= pos[1]:
                if x <= pos[0] and x + 100 >= pos[0]:
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
        self.name = "knight"
    
    def move(self, pos):
        for i in range(len(squares)):
            key = list(squares[i].keys())[0]
            x = squares[i][key][0]
            y = squares[i][key][1]

            if y <= pos[1] and y + 100 >= pos[1]:
                if x <= pos[0] and x + 100 >= pos[0]:
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
        self.name = "rook"
    
    def move(self, pos):
        for i in range(len(squares)):
            key = list(squares[i].keys())[0]
            x = squares[i][key][0]
            y = squares[i][key][1]

            if y <= pos[1] and y + 100 >= pos[1]:
                if x <= pos[0] and x + 100 >= pos[0]:
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
        self.name = "queen"
    
    def move(self, pos):
        for i in range(len(squares)):
            key = list(squares[i].keys())[0]
            x = squares[i][key][0]
            y = squares[i][key][1]

            if y <= pos[1] and y + 100 >= pos[1]:
                if x <= pos[0] and x + 100 >= pos[0]:
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
        self.name = "king"
    
    def move(self, pos):
        for i in range(len(squares)):
            key = list(squares[i].keys())[0]
            x = squares[i][key][0]
            y = squares[i][key][1]

            if y <= pos[1] and y + 100 >= pos[1]:
                if x <= pos[0] and x + 100 >= pos[0]:
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
        if y == 600 and len(whitePawns) <= 7:
            whitePawns.append(Pawn(x, y))

        elif y == 100 and len(blackPawns) <= 7:
            blackPawns.append(Pawn(x, y))

        
        # white pieces
        elif y == 700:
            # bishops
            if (x == 200 or x == 500) and len(whiteBishops) <= 1:
                whiteBishops.append(Bishop(x, y))

            # knights
            if (x == 100 or x == 600) and len(whiteKnights) <= 1:
                whiteKnights.append(Knight(x, y))

            # rooks
            if (x == 0 or x == 700) and len(whiteRooks) <= 1:
                whiteRooks.append(Rook(x, y))

            # queen
            if x == 300 and len(whiteQueen) <= 0:
                whiteQueen.append(Queen(x, y))

            # king
            if x == 400 and len(whiteKing) <= 0:
                whiteKing.append(King(x, y))

        
         # black pieces
        if y == 0:
            # bishops
            if (x == 200 or x == 500) and len(blackBishops) <= 1:
                blackBishops.append(Bishop(x, y))
            
            # knights
            if (x == 100 or x == 600) and len(blackKnights) <= 1:
                blackKnights.append(Knight(x, y))

            # rooks
            if (x == 0 or x == 700) and len(blackRooks) <= 1:
                blackRooks.append(Rook(x, y))

            # queen
            if x == 300 and len(blackQueen) <= 0:
                blackQueen.append(Queen(x, y))

            # king
            if x == 400 and len(blackKing) <= 0:
                blackKing.append(King(x, y))



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
    pygame.draw.rect(win, (255, 255, 255), (0, 0, win_width, win_height))
    pygame.draw.rect(win, (255, 0, 0), (0, 800, win_width, 100), 4)
    boardSetup()
    pieceSetup()

    pygame.display.update()


whiteTurn = True
move = False
run = True

while run:
    clock.tick(60)
    redraw()

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            # MOVEMENT
            if not(move):
                selection = pygame.mouse.get_pos()
                move = True
            
            elif move:
                movePos = pygame.mouse.get_pos()

                # white pieces
                for arr in whitePieces:
                    for piece in arr:
                        if piece.y <= selection[1] and piece.y + 100 >= selection[1] and whiteTurn:
                            if piece.x <= selection[0] and piece.x + 100 >= selection[0]:
                                if movePos[1] > 800:
                                    arr.pop(arr.index(piece))
                                else:
                                    piece.move(movePos)
                                    whiteTurn = False

                # black pieces
                for arr in blackPieces:
                    for piece in arr:
                        if piece.y <= selection[1] and piece.y + 100 >= selection[1] and not(whiteTurn):
                            if piece.x <= selection[0] and piece.x + 100 >= selection[0]:
                                if movePos[1] > 800:
                                    arr.pop(arr.index(piece))
                                else:
                                    piece.move(movePos)
                                    whiteTurn = True
                
                move = False
    


    # CAPTURES
    for arr in whitePieces:
        for piece in arr:
            for bArr in blackPieces:
                for bPiece in bArr:
                    if piece.x == bPiece.x and piece.y == bPiece.y:
                        if whiteTurn:
                            arr.pop(arr.index(piece))
                        
                        elif not(whiteTurn):
                            bArr.pop(bArr.index(bPiece))

                        print("capture")
    

pygame.quit()