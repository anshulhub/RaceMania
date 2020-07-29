import random
from time import sleep

import pygame


class CarRacing:
    def __init__(self):

        pygame.init()
        self.display_width = 800
        self.display_height = 600
        self.black = (20, 20, 20)
        # self.black = pygame.image.load("bcg.jpg")
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.gameDisplay = None

        self.initialize()

    def initialize(self):

        self.crashed = False

        self.carImg = pygame.image.load('images/car.png')
        self.car_x_coordinate = (self.display_width * 0.45)
        self.car_y_coordinate = (self.display_height * 0.8)
        self.car_width = 49

        # enemy_car
        self.enemy_car1 = pygame.image.load('images/enemy_car_1.png')
        self.enemy_car2 = pygame.image.load('images/enemy_car_2.png')
        self.enemy_car3 = pygame.image.load('images/enemy_car_3.png')
        #self.enemy_car3 = pygame.image.load('enemy_car_3.png')
        self.imag=[self.enemy_car1,self.enemy_car2,self.enemy_car3]
        self.enemy_car=random.choice(self.imag)
#        self.enemy_car=random.choice(self.imag)
        self.enemy_car_startx = random.randrange(310, 450)
        self.enemy_car_starty = -600
        self.enemy_car_speed = 5
        self.enemy_car_width = 46
        self.enemy_car_height = 90

        # Background
        self.bgImg = pygame.image.load("images/back_ground.jpg")
        self.bg_x1 = (self.display_width / 2) - (360 / 2)
        self.bg_x2 = (self.display_width / 2) - (360 / 2)
        self.bg_y1 = 0
        self.bg_y2 = -600
        self.bg_speed = 3
        self.count = 0

    def car(self, car_x_coordinate, car_y_coordinate):
        self.gameDisplay.blit(self.carImg, (car_x_coordinate, car_y_coordinate))

    def racing_window(self):
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Car Game')
        self.run_car()

    def run_car(self):

        while not self.crashed:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True
                # print(event)

                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_LEFT):
                        self.car_x_coordinate -= 35
                        # print ("CAR X COORDINATES: %s" % self.car_x_coordinate)
                    if (event.key == pygame.K_RIGHT):
                        self.car_x_coordinate += 35
                        # print ("CAR X COORDINATES: %s" % self.car_x_coordinate)
                    # print ("x: {x}, y: {y}".format(x=self.car_x_coordinate, y=self.car_y_coordinate))

            self.gameDisplay.fill(self.black)
            #self.gameDisplay.fill(pygame.image.load("bcg.jpg"))
            self.back_ground_raod()
            self.run_enemy_car(self.enemy_car_startx, self.enemy_car_starty)
            self.enemy_car_starty += self.enemy_car_speed

            if self.enemy_car_starty > self.display_height:
                self.enemy_car_starty = 0 - self.enemy_car_height
                self.enemy_car_startx = random.randrange(280, 480)

            self.car(self.car_x_coordinate, self.car_y_coordinate)
            self.highscore(self.count)
            self.count += 1
            if (self.count % 100 == 0):
                self.enemy_car_speed += 0.25
                self.bg_speed += 0.25

            if self.car_y_coordinate < self.enemy_car_starty + self.enemy_car_height:
                if self.car_x_coordinate > self.enemy_car_startx and self.car_x_coordinate < self.enemy_car_startx + self.enemy_car_width or self.car_x_coordinate + self.car_width > self.enemy_car_startx and self.car_x_coordinate + self.car_width < self.enemy_car_startx + self.enemy_car_width:
                    self.crashed = True
                    self.display_message("Game Over !!!")

            if self.car_x_coordinate < 250 or self.car_x_coordinate > 500:
                self.crashed = True
                self.display_message("Game Over !!!")

            pygame.display.update()
            self.clock.tick(60)

    def display_message(self, msg):
        font = pygame.font.SysFont("comicsansms", 72, True)
        text = font.render(msg, True, (255, 255, 255))
        self.gameDisplay.blit(text, (400 - text.get_width() // 2, 240 - text.get_height() // 2))
        self.display_credit()
        pygame.display.update()
        self.clock.tick(60)
        sleep(3.5)
        car_racing.initialize()
        car_racing.racing_window()

    def back_ground_raod(self):
        self.gameDisplay.blit(self.bgImg, (self.bg_x1, self.bg_y1))
        self.gameDisplay.blit(self.bgImg, (self.bg_x2, self.bg_y2))

        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        if self.bg_y1 >= self.display_height:
            self.bg_y1 = -600

        if self.bg_y2 >= self.display_height:
            self.bg_y2 = -600

    def run_enemy_car(self, thingx, thingy):
        self.gameDisplay.blit(self.enemy_car, (thingx, thingy))

    def highscore(self, count):
        font = pygame.font.SysFont("lucidaconsole", 18)
        text = font.render("Score : " + str(count), True, self.white)
        self.gameDisplay.blit(text, (85, 80))
        font = pygame.font.SysFont("lucidaconsole", 34)
        text = font.render(" CAR MANIA ", True, self.white)
        self.gameDisplay.blit(text, (5, 10))

    def display_credit(self):
        
        font = pygame.font.SysFont("lucidaconsole", 17)
        text = font.render("Made Possible by:", True, self.white)
        self.gameDisplay.blit(text, (590, 400))
        text = font.render("Anshul", True, self.white)
        self.gameDisplay.blit(text, (590, 420))
        text = font.render("Powered by:", True, self.white)
        self.gameDisplay.blit(text, (590, 440))
        text = font.render("AG Gaming.com", True, self.white)
        self.gameDisplay.blit(text, (590, 460))


if __name__ == '__main__':
    car_racing = CarRacing()
    car_racing.racing_window()
