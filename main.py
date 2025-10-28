from pyray import *
SIDE = 40
WIDTH = 20 
HEIGHT = 10 

init_window(SIDE*WIDTH,SIDE*HEIGHT, 'Le serpent')
set_target_fps(5)

while not window_should_close() :

    begin_drawing()
    
    clear_background(BLACK)
    draw_text("Début du jeu ", 190,200, 20, WHITE)
    SNAKE= [[1,1],[2,1],[3,1]]
    VITESSE = [1,0]
    for i, (x,y) in enumerate(SNAKE) : 
        Vx,Vy = VITESSE
        hx,hy = SNAKE[-1]
        new_head=[hx+Vx,hy+Vy]
        SNAKE= SNAKE[1:]+new_head
        COLOR = GREEN if (i==len(SNAKE)-1) else DARKGREEN
        draw_rectangle(x*SIDE+1,y*SIDE,SIDE-2,SIDE-2,COLOR)
    i=i+10
    end_drawing()
    

    

close_window()

