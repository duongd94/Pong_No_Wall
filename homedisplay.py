import pygame
from button import Button


# create and display home screen
class HomeScreen:
    def __init__(self, setting, screen):

        # initialize home screen
        self.setting = setting
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # initialize the button
        self.button = Button(self.screen, "Start")

    # display home screen
    def display_home_screen(self):

        self.button.draw_button()
