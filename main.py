from pyray import *
from raylib import *
import random
#Ajouter jeu circulaire + réactivité + bombe toutes les dix pommes (qui disparait après deux pommes mangées)

SIDE= 40
WIDTH = 20
HEIGHT = 20
init_window(SIDE*WIDTH,SIDE*HEIGHT,"Mon jeu")
set_target_fps(60)

#initialisation
snake=[[1,1],[2,1],[3,1]]
vitesse=[1,0]
perdu=False
fruit = [random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1)]
score =0
k=0

while not window_should_close() :

    begin_drawing() 
    clear_background(BLACK)

    # animation du serpent et du fruits
    
    k=k+1

    if k%6==0 : #On réduit la vitesse du serpent tout en gardant 60 fps pour plus de réactivité
        vx,vy=vitesse
        hx,hy=snake[-1]
        new_head=[hx+vx, hy+vy] 

        for i in (0,1): 
            if new_head[i]<0: 
                new_head[i]=WIDTH
            elif new_head[i] >= WIDTH : 
                new_head[i]= 0
        
        
        if new_head in snake : 
              perdu = True     
        
        #traitement du fruit 
        if new_head==fruit:
            fruit =[random.randint(0,WIDTH-1), random.randint(0,HEIGHT-1)]
            score=score+10
            snake=snake+[new_head] 

        


        else : 
            snake=snake[1:]
            snake=snake+[new_head] 
    
    draw_rectangle(fruit[0]*SIDE,fruit[1]*SIDE,SIDE,SIDE, RED) #fruit 
    
    for i,(x,y) in enumerate(snake): #serpent
        color=GREEN if i==len(snake)-1 else DARKGREEN
        draw_rectangle(x*SIDE,y*SIDE,SIDE-2,SIDE-2,color)  

    # Gestion des changements de direction
    if is_key_pressed(KEY_UP) and vitesse!=[0,1]:
            vitesse=[0,-1]
    if is_key_pressed(KEY_DOWN) and vitesse!=[0,-1]:
            vitesse=[0,1]
    if is_key_pressed(KEY_LEFT) and vitesse!=[1,0]:
            vitesse=[-1,0]
    if is_key_pressed(KEY_RIGHT) and vitesse!=[-1,0]:
            vitesse= [1,0]

    draw_text(f"Score {score}",0,0,50,WHITE)
        
        




    #    clear_background(BLACK)
    #   draw_text("GAME OVER", WIDTH//2, HEIGHT//2, WHITE)
    #    end_drawing()
    
    
    
    

    
    end_drawing()
