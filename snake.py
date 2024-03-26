import pygame
from sys import exit
import random
pygame.init()
# basic configuration for pygame
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")
game_clock = pygame.time.Clock()
max_frame_rate = 24
score_font = pygame.font.Font(None, 40)
#surfaces
snake_cell = pygame.Surface((20, 20))
snake_cell.fill("green")
apple = pygame.Surface((20, 20))
apple.fill("red")
def snake_died():
    gameloop()
def gameloop():
    # game variables
    score = 0
    snake = [[screen_width / 2, screen_height / 2]]
    need_to_generate_apple = True
    horizontal_movement = 0
    vertical_movement = 0
    need_to_grow = False

    while True:
        for event in pygame.event.get():
            #check if someone is trying to exit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #check which keys are being pressed

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_w:
                    vertical_movement = -20
                    horizontal_movement = 0
                    
                if event.key == pygame.K_a:
                    horizontal_movement = -20
                    vertical_movement = 0
                    
                if event.key == pygame.K_s:
                    vertical_movement = 20
                    horizontal_movement = 0
                    
                if event.key == pygame.K_d:
                    horizontal_movement = 20
                    vertical_movement = 0
        
        
        #render scoreboard
        score_surface = score_font.render(str(score), False, 'Blue')    
        screen.blit(score_surface, (0, 0))
        # move snake
        cell_counter = 0
        last_cell = snake[-1].copy()
        for cell in snake:
            if cell_counter == 0:
                last_move = cell.copy()
                snake[cell_counter][0] += horizontal_movement
                snake[cell_counter][1] += vertical_movement 
            else:
                last_move_buffer = cell.copy()
                snake[cell_counter] = last_move
                last_move = cell
            cell_counter += 1
        #append cell to snake
        if need_to_grow:
            snake.append(last_cell)
            need_to_grow = False

        print("snake is")
        print(snake)
        # render snake
        for cell in snake:
            screen.blit(snake_cell, (cell[0], cell[1]))

        # check if snake died
        if snake[0][0] > screen_width:
            snake_died()
        if snake[0][0] < 0:
            snake_died()
        if snake[0][1] > screen_height:
            snake_died()
        if snake[0][1] < 0:
            snake_died()
        for i in snake[1:]:
            if i == snake[0]:
                snake_died()
        #generate the apple
        if need_to_generate_apple == True:
            generated_apple_location_width_range = screen_width / 20
            generated_apple_location_height_range = screen_height / 20
            generated_apple_location_height = 0
            generated_apple_location_width = 0
            while True:
                generated_apple_location_height = random.randint(0, generated_apple_location_height_range - 1) * 20
                generated_apple_location_width = random.randint(0, generated_apple_location_width_range - 1) * 20
                if not snake.__contains__([generated_apple_location_width, generated_apple_location_height]):
                    break
            
            #render apple
            screen.blit(apple, (generated_apple_location_width, generated_apple_location_height))
            need_to_generate_apple = False
        
        #track apple collision
        print("apple location is " + str(generated_apple_location_width) + "," + str(generated_apple_location_height))
        print("snake 0 is " + str(snake[0]))

        if snake[0][0] == (generated_apple_location_width) and snake[0][1] == (generated_apple_location_height):
            need_to_generate_apple = True
            need_to_grow = True
            score += 1
        
        #update and clear screen
        pygame.display.update()
        screen.fill("black")
        screen.blit(apple, (generated_apple_location_width, generated_apple_location_height))

        game_clock.tick(max_frame_rate)
#start game
gameloop()