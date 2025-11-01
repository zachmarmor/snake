from pyray import *
from raylib import *
import random
# bombe toutes les dix pommes (qui disparait après deux pommes mangées)

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
loc_s_fruit= [random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1)] #position super fruit
super_fruit=False
score =0
k=0
i= 0
tps = 0 
while not window_should_close() :

    begin_drawing() 
    clear_background(BLACK)

    # animation du serpent et du fruits
    
    k=k+1

    if k%6==0 and not perdu: #On réduit la vitesse du serpent tout en gardant 60 fps pour plus de réactivité
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
        
        #traitement des fruits
        if new_head==fruit:
            score=score+10
            snake=snake+[new_head]
            fruit =[random.randint(0,WIDTH-1), random.randint(0,HEIGHT-1)]
            while fruit in snake : # on empêche le fruit de se créer sur le serpent 
                 fruit =[random.randint(0,WIDTH-1), random.randint(0,HEIGHT-1)]


        if super_fruit and new_head==loc_s_fruit: 
            score=score+100
            snake=snake+[new_head]
            super_fruit = False
            tps=0
            loc_s_fruits_fruit =[random.randint(0,WIDTH-1), random.randint(0,HEIGHT-1)]
            while loc_s_fruit in snake : # on empêche le fruit de se créer sur le serpent 
                 loc_s_fruit =[random.randint(0,WIDTH-1), random.randint(0,HEIGHT-1)]

        
        else : 
            snake=snake[1:]
            snake=snake+[new_head]
    

    if not perdu : 

        draw_rectangle(fruit[0]*SIDE,fruit[1]*SIDE,SIDE,SIDE, RED) #fruit 
        
        if super_fruit : 
             tps+=1
             draw_rectangle(loc_s_fruit[0]*SIDE,loc_s_fruit[1]*SIDE,SIDE,SIDE, YELLOW)

             if tps>= 300 : # On limite le temps pendant lequel reste le super fruit 
                  super_fruit = False
                  tps=0

        if k%1500==0 : # On fait apparaître un super fruit de temps en temps 
             super_fruit = True 
             tps=0

        for i,(x,y) in enumerate(snake): #serpent
            color=GREEN if i==len(snake)-1 else DARKGREEN
            draw_rectangle(x*SIDE,y*SIDE,SIDE-2,SIDE-2,color)  
        draw_text(f"Score {score}",0,0,50,WHITE)

    # Gestion des changements de direction
    if is_key_pressed(KEY_UP) and vitesse!=[0,1]:
            vitesse=[0,-1]
    if is_key_pressed(KEY_DOWN) and vitesse!=[0,-1]:
            vitesse=[0,1]
    if is_key_pressed(KEY_LEFT) and vitesse!=[1,0]:
            vitesse=[-1,0]
    if is_key_pressed(KEY_RIGHT) and vitesse!=[-1,0]:
            vitesse= [1,0]

        
    if perdu : 
        draw_text(f"game over \n votre score était de : {score} \n appuyez sur entrer pour recommencer", 10, HEIGHT*HEIGHT//2, 30,WHITE)

        if is_key_pressed(KEY_ENTER): 
            # réinitialisation
            snake=[[1,1],[2,1],[3,1]]
            vitesse=[1,0]
            perdu= False
            fruit = [random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1)]
            score =0
            k=0    

        

    
    end_drawing()
