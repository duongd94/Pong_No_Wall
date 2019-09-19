import random

import pygame


class Setting:
    def __init__(self, setting):

        self.setting = setting

        # Ball
        self.B_radius = 10
        self.B_color = (225, 0, 0)

        # Paddles
        self.paddles_width = 15
        self.paddles_size = 90
        self.paddles_speed = 20
        self.top_bottom_size = self.get_top_bottom_paddles_size()
        self.side_size = self.get_side_paddles_size()
        self.top_position= self.get_top_position()
        self.bottom_position = self.get_bottom_position()
        self.side_position = self.get_side_position()
        self.paddles_image = pygame.image.load('images/paddles.png')

        # Net
        self.net_width = 5
        self.net_height = 30
        self.net_color = (0, 0, 225)
        self.net_offset = 25

        # display
        self.screen_width = 1400
        self.screen_height = 900
        self.screen_background = pygame.image.load('images/background.png')
        self.screen_padding = 20

        # Ball speed
        self.B_speed_x = self.random_generator()
        self.B_speed_y = self.random_generator()
        self.ball_velocity = 0.25

        # PC player
        self.pc_follow = 35
        self.pc_speed = 6

    # config the paddles to display correct direction
    def get_top_bottom_paddles_size(self):
        return self.setting.paddles_size, self.setting.paddles_width

    def get_side_paddles_size(self):
        return self.setting.paddles_width, self.setting.paddles_size

    @staticmethod
    def get_top_position():
        return 0

    def get_bottom_position(self):
        return self.setting.screen_height - self.setting.paddles_width

    def get_side_position(self):
        return (self.setting.screen_height // 2) - (self.setting.paddles_size // 2)

    # random generator
    @staticmethod
    def random_generator():
        return random.choice([i for i in range(-9, 9) if i not in [0, -1, -2, -3, 1, 2, 3]])



