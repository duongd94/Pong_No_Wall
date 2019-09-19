import pygame


class Button:
    def __init__(self, screen, button_color):
        # initialize the button
        self.width = 300
        self.height = 100
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # draw the button n put it in the middle
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

    def draw_button(self):
        self.screen.fill((225, 225, 225), self.rect)