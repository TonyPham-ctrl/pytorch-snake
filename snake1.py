import pygame, sys, random
from pygame.math import Vector2

    

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block=False
    def draw_snake(self):
        for block in self.body:
            #create a rectangle
            block_rect = pygame.Rect(block.x * cellSize,block.y*cellSize,cellSize,cellSize)
            #draw rect
            pygame.draw.rect(screen, pygame.Color('blue'),block_rect)
    def move_snake(self):
        if self.new_block==True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]
    def grow_snake(self):
        self.new_block = True
    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]





class Fruit:
    def __init__(self):
        self.randomize()
    def draw_fruit(self):
        fruit = pygame.Rect(self.pos.x*cellSize,self.pos.y*cellSize,cellSize,cellSize)
        pygame.draw.rect(screen, pygame.Color('red'), fruit)
    def randomize(self):
        self.x = random.randint(0, cellNum - 1)
        self.y = random.randint(0, cellNum - 1)
        self.pos = Vector2(self.x, self.y)



class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_element(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        #if collision occured
        if self.fruit.pos == self.snake.body[0]:
            print("Nom")
            #reposition fruit
            self.fruit.randomize()
            #add another block
            self.snake.grow_snake()
            #increment score

    def check_fail(self):
        if not 0 <=self.snake.body[0].x <= cellNum or not 0<=self.snake.body[0].y <= cellNum:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x=int(cellSize*cellNum - 60)
        score_y=int(cellSize*cellNum - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))

        screen.blit(score_surface,score_rect)
        screen.blit(apple, apple_rect)


pygame.init()


#initialise variables
cellSize = 40
cellNum = 20

screen=pygame.display.set_mode((cellNum * cellSize, cellNum*cellSize))
clock = pygame.time.Clock()
SCREEN_UPDATE = pygame.USEREVENT
apple = pygame.image.load('icon/apple.png').convert_alpha()
pygame.time.set_timer(SCREEN_UPDATE,150)
game_font = pygame.font.Font(None,25)

main_game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and main_game.snake.direction!=Vector2(0,1):
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_d and main_game.snake.direction!=Vector2(-1,0):
                main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_s and main_game.snake.direction!=Vector2(0,-1):
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_a and main_game.snake.direction!=Vector2(1,0):
                main_game.snake.direction = Vector2(-1,0)
    screen.fill((175, 215, 70))
    main_game.draw_element()
    pygame.display.update()
    clock.tick(60)
    