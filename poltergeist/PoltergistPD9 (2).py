#Matrix Gaming
#Polergeist
#James,Sara,Sherissa
#two sentence explanation of the game's objective

from gamelib import*

#objects and initial settings
game = Game (800,600,"kon")
bk = Image("bk.jpg",game)
bk = Image("bk.jfif",game)
bk.resizeTo(game.width, game.height)
kon = Animation("kon.png",16,game,1841/4,2400/4,3)
sp = Image("sp.png",game)
de = Animation("de.png",16,game,320/4,320/4,3)
sp.resizeTo(180,150)
sp.moveTo(200, 500)
kon.resizeTo (95, 95)
kon.moveTo (400, 500)
de.resizeTo(180, 150)
de.moveTo(100, 500)

#Level 1 - game loop


while not game.over:
    game.processInput()
    #game.scrollBackground("left",2)
    bk.draw()
    sp.draw()
    kon.draw()
    de.draw()
    game.update(30)

game.over = False
#Level 2 - game loop
while not game.over:
    game.processInput()
    #game.scrollBackground("left",2)
    bk.draw()
    #kon.draw()
    game.update(30)

game.quit()
