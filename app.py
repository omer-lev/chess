import pygame

pygame.init()

win_width = 800
win_height = 800

win = pygame.display.set_mode((win_width, win_height))
title = pygame.display.set_caption("Chess")

clock = pygame.time.Clock()

cursor_img = pygame.image.load('img/pointer.png')

# pawns
blackPawnImg = pygame.image.load('img/black_pawn.png')
whitePawnImg = pygame.image.load('img/white_pawn.png')

# rooks
whiteRookImg = pygame.image.load('img/white_rook.png')
blackRookImg = pygame.image.load('img/black_rook.png')

# pygame.mouse.set_visible(False)
# cursor_img_rect = cursor_img.get_rect()

class Pawn():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def move(self, side, capture=False):
        if side == "white":
            if capture:
                if move[1] <= self.y - 25:
                    if move[0] <= self.x - 25:
                        self.x -= step
                        self.y -= step
                    
                    elif move[0] >= self.x + 75:
                        self.x += step
                        self.y -= step
            
            else:
                if move[1] >= self.y - 200 and move[1] < self.y - 25:
                    if move[0] > self.x - 25 and move[0] < self.x + 75:
                        if move[1] < self.y - 150 and self.y >= 600:
                            self.y -= step*2
                        
                        else:
                            self.y -= step
                

        if side == "black":
            if capture:
                if move[1] >= self.y + 75:
                    if move[0] <= self.x - 25:
                        self.x -= step
                        self.y += step
                    
                    elif move[0] >= self.x + 75:
                        self.x += step
                        self.y += step

            else:
                if move[1] <= self.y + 250 and move[1] > self.y + 75:
                    if move[0] > self.x - 25 and move[0] < self.x + 75:
                        if move[1] > self.y + 150 and self.y <= 200:
                            self.y += step*2
                    
                        else:
                            self.y += step
  

    def draw(self, win, side):
        if side == "white":
            win.blit(whitePawnImg, (self.x - 10, self.y - 5))
        
        if side == "black":
            win.blit(blackPawnImg, (self.x - 10, self.y - 5))
    


class Rook():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, side, capture=False):
        if side == "white":
            for i in range(7):
                if round(move[0] / step) == i:
                    self.x += step*i - self.x

                if round(move[1] / step) == i:
                    self.y -= self.y - step*i - 25

        if side == "black":
            for i in range(7):
                if round(move[1] / step) == i:
                    self.y += step*i - self.y
                

    def draw(self, win, side):
        if side == "white":
            win.blit(whiteRookImg, (self.x - 3, self.y - 5))

        if side == "black":
            win.blit(blackRookImg, (self.x + 3, self.y + 7))
            



def drawBoard():
    for j in range(9):
        for i in range(9):
            if j % 2 == 0:
                if i % 2 == 0:
                    pygame.draw.rect(win, (255, 255, 255), (i*100, j*100, 100, 100))
                
                else:
                    pygame.draw.rect(win, (118, 150, 86), (i*100, j*100, 100, 100))
            
            else:
                if i % 2 == 0:
                    pygame.draw.rect(win, (118, 150, 86), (i*100, j*100, 100, 100))
                
                else:
                    pygame.draw.rect(win, (255, 255, 255), (i*100, j*100, 100, 100))


def redraw():
    drawBoard()
            
    for pawn in pawnsWhite:
        pawn.draw(win, "white")
    
    for pawn in pawnsBlack:
        pawn.draw(win, "black")

    for rook in rooksWhite:
        rook.draw(win, "white")
    
    for rook in rooksBlack:
        rook.draw(win, "black")

    
    # cursor_img_rect.center = pygame.mouse.get_pos()
    # win.blit(cursor_img, cursor_img_rect)
    

    pygame.display.update()


pawnsWhite = []
pawnsBlack = []

rooksWhite = []
rooksBlack = []


# pawn init
for i in range(9):
    pawn = Pawn(i*100 + 25, win_height - 175, 50, 50)
    pawnsWhite.append(pawn)


for i in range(9):
    pawn = Pawn(i*100 + 25, 125, 50, 50)
    pawnsBlack.append(pawn)


# rook init
rook = Rook(0, win_height - 75, 50, 50)
rooksWhite.append(rook)

rook = Rook(win_width - 100, win_height - 75, 50, 50)
rooksWhite.append(rook)

rook = Rook(0, 0, 50, 50)
rooksBlack.append(rook)

rook = Rook(win_width - 100, 0, 50, 50)
rooksBlack.append(rook)



selection = ()
move = ()
moveCount = 0
step = 100
run = True

while run:
    clock.tick(60)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

        if event.type == pygame.MOUSEBUTTONUP:
            if moveCount == 0:
                selection = pygame.mouse.get_pos()
                moveCount += 1
            
            elif moveCount == 1:
                move = pygame.mouse.get_pos()
                
                # PAWN MOVEMENT
                #---------------
                # white movement
                for pawn in pawnsWhite:
                    if pawn.y - 25 <= selection[1] and pawn.y + 75 >= selection[1]:
                        if pawn.x - 25 <= selection[0] and pawn.x + 75 >= selection[0]:
                            pawn.move("white")
                
                # black movement
                for pawn in pawnsBlack:
                    if pawn.x - 25 <= selection[0] and pawn.x + 75 >= selection[0]:
                        if pawn.y - 25 <= selection[1] and pawn.y + 75 >= selection[1]:
                            pawn.move("black")                

                # white captures
                for pawn in pawnsWhite:
                    for bPawn in pawnsBlack:
                        if pawn.y - 100 == bPawn.y and (pawn.x - 100 == bPawn.x or pawn.x + 100 == bPawn.x):
                            if pawn.y - 25 <= selection[1] and pawn.y + 75 >= selection[1]:
                                if pawn.x - 25 <= selection[0] and pawn.x + 75 >= selection[0]:
                                    pawn.move("white", True)
                                    pawnsBlack.pop(pawnsBlack.index(bPawn))
                
                # black captures
                for pawn in pawnsBlack:
                    for wPawn in pawnsWhite:
                        if pawn.y + 100 == wPawn.y and (pawn.x - 100 == wPawn.x or pawn.x + 100 == wPawn.x):
                            if pawn.y + 75 >= selection[1] and pawn.y - 25 <= selection[1]:
                                if pawn.x - 25 <= selection[0] and pawn.x + 75 >= selection[0]:
                                    pawn.move("black", True)
                                    pawnsWhite.pop(pawnsWhite.index(wPawn))
                

                # ROOK MOVEMENT
                # --------------
                # white movement
                for rook in rooksWhite:
                    if rook.y - 25 <= selection[1] and rook.y + 75 >= selection[1]:
                        if rook.x - 25 <= selection[0] and rook.x + 75 >= selection[0]:
                            rook.move("white")

                # black movement
                for rook in rooksBlack:
                    if rook.y - 25 <= selection[1] and rook.y + 75 >= selection[1]:
                        if rook.x - 25 <= selection[0] and rook.x + 75 >= selection[0]:
                            rook.move("black")
                
                # white captures
                for rook in rooksWhite:
                    for pawn in pawnsBlack:
                        if rook.y == pawn.y and rook.x == pawn.x - 25:
                            pawnsBlack.pop(pawnsBlack.index(pawn))

                moveCount = 0

    redraw()


pygame.quit()