import pygame
import sys
from settings import *
from car import Car
from obs import Obstacle
from text_obj import Text_Obj
from text_ob import Text_Ob
# создание объектов
pygame.init()
screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
clock = pygame.time.Clock()


#groops
all_sprites = pygame.sprite.Group()
items = pygame.sprite.Group() 

car = Car(PLAYER_Y, PLAYER_X, 'zane.png', pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN)
all_sprites.add(car)


for i in range(5):
    obs = Obstacle('flower.png', True)
    all_sprites.add(obs)
    items.add(obs)
for i in range(2):
    obs = Obstacle('fire.png', False)
    all_sprites.add(obs)
    items.add(obs)


#peremenn

score = 0
health = 100
score_text = Text_Obj(10,10, str(score), screen)
health_text = Text_Ob(745, 10, str(health), screen)
# главный цикл
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # изменение объектов, update
    car.update()
    all_sprites.update()
    score_text.update(score)
    health_text.update(health)



    #пересечение объектов, collisions
    eats = pygame.sprite.spritecollide(car, items, True)
    for eat in eats:
        if eat.get_edible() == True:
            score += 1
            obs = Obstacle('flower.png', True)
            all_sprites.add(obs)
            items.add(obs)

        if eat.get_edible() == False:
            health -= 10
            obs = Obstacle('fire.png', False)
            all_sprites.add(obs)
            items.add(obs)

        if health == 0:
            pygame.quit()
            sys.exit()


    # обновление экрана
    screen.fill(BLACK)
    car.draw(screen)
    all_sprites.draw(screen)
    score_text.draw()
    health_text.draw()
    

    
    pygame.display.update()

