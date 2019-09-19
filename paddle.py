import pygame
from setting import Setting
from pygame.sprite import Sprite


class Paddles(Sprite):
    def __init__(self, setting, screen, image, type , size, position):
        super(Paddles, self).__init__()
        # initialize the ball
        self.setting = setting
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = image
        self.type = type
        self.width = size
        self.height = size
        self.x = position
        self.y = position

        # rect
        self.rect = pygame.draw.rect(self.screen, self.image, (self.x, self.y, self.width, self.height))

    # draw the paddles
    def draw_paddles(self):
        pygame.draw.rect(self.screen, self.image, (self.x, self.y, self.width, self.height))

    # fuct for moving player paddles
    def player_movement(self, move):
        left, right, up, down = move

        # side paddles
        if self.type == "side":
            if up and self.rect.top > 0:
                self.y -= self.setting.paddles_speed
            if down and self.rect.bottom < self.screen_rect.bottom:
                self.y += self.setting.paddles_speed
        # top n bottom paddles
        else:
            if left and self.rect.left > 0:
                self.x -= self.setting.paddles_speed
            if right and self.rect.right < (self.setting.screen_width // 2) - (self.setting.net_width // 2):
                self.x += self.setting.paddles_speed

        self.rect.x = self.x
        self.rect.y = self.y

    # func for moving pc paddles just follow the ball
    def pc_movement(self, ball):
        if self.type == "side":
            self.pc_side_move(ball.y)
        else:
            self.pc_top_bottom_move(ball.x)

    # assist func for pc paddles to follow the ball
    def pc_side_move(self, ball):
        position = self.y + (self.height // 2)

        if position < (ball - self.setting.pc_follow):
            self.y += self.setting.pc_speed
        elif position > (ball + self.setting.pc_follow):
            self.y -= self.setting.pc_speed

        self.rect.y = self.y

    def pc_top_bottom_move(self, ball):
        position = self.x + (self.width // 2)

        if position < (ball - self.setting.pc_follow):
            self.x += self.setting.pc_speed
        elif position > (ball + self.setting.pc_follow):
            self.x -= self.setting.pc_speed

        # horizontal limiter
        net = (self.setting.screen_width // 2) + (self.setting.net_width // 2)
        if self.x <= net:
            self.x = net
        if self.rect.right > self.setting.screen_width:
            self.x = self.setting.screen_width - (self.width // 2)

        self.rect.x = self.x







