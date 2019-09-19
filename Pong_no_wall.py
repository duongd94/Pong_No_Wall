import pygame, sys, time, random

from setting import Setting
from ball import Ball
from player import Player
from paddle import Paddles
from sound import Sound
from button import Button
from homedisplay import HomeScreen
from playerscore import PlayerScore
from scoreboard import ScoreBoard
from pygame.locals import *

# set up Pygame


class Pong:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Pong with No Walls')

        self.setting = Setting()

        # display
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))

        # sound
        self.sound = Sound()

        # homedisplay
        ## self.home_screen = display_home_screen(self.setting, self.screen)
        # game stats and score board
        ## self.stat = Stat()
        # self.score_board = score_board(self.setting, self.screen, self.stat)
        # game object
        self.initializing()

    # initialize game object
    def initializing(self):
        self.ball = Ball(self.setting, self.screen, self.sound, self.stat, self.score_board)
        self.player = Player(self.setting, self.screen, self.setting.paddles_image)
        self.pc = Player(self.setting,self.screen, self.setting.paddles_image)

    # check input
    def pong_input(self):
        for inputs in pygame.event.get():
            if inputs.type == pygame.event.get():
                sys.exit()
            elif inputs.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.click_play(mouse_x, mouse_y)
            elif inputs.type == pygame.KEYDOWN:
                self.keydown_input(inputs)
            elif inputs.type == pygame.KEYUP:
                self.keyup_input(inputs)

    # check key input
    def keydown_input(self, inputs):
        if inputs.key == pygame.K_q:
            sys.exit()
        elif inputs.key == pygame.K_RIGHT:
            self.player.right = True
        elif inputs.key == pygame.K_LEFT:
            self.player.left = True
        elif inputs.key == pygame.K_UP:
            self.player.up = True
        elif inputs.key == pygame.K_DOWN:
            self.player.down = True

    def keyup_input(self, inputs):
        if inputs.key == pygame.K_RIGHT:
            self.player.right = False
        elif inputs.key == pygame.K_LEFT:
            self.player.left = False
        elif inputs.key == pygame.K_UP:
            self.player.up = False
        elif inputs.key == pygame.K_DOWN:
            self.player.down = False

    # check play button
    def click_play(self, mouse_x, mouse_y):
        # test if a point is inside a rectangle
        clicked = self.start_game.button.rect.collidepoint(mouse_x, mouse_y)
        # if game not started, set everything to default setting
        if clicked and not self.stat.active:
            self.setting.initialize_setting()
            self.ball.rest()
            # self.score_board.clear_score_board()
            self.stat.clear_stat()
            self.stat.active = True

    # starting the game
    def game_begin(self):
        # set back ground
        self.screen.fill(self.setting.screen_background)
        # set all game object
        if self.stat.active:
            self.stat.start_screen = False

            self.ball.draw_ball()
            self.player.draw_paddles()
            self.pc.draw_paddles()

            self.score_board.draw_net()

        elif self.stat.winner != "":
            self.score_board.display_score()
            self.home_screen.button.draw_button()
        else:
            self.home_screen.display_home_screen()
        # Update the full display Surface to the screen
        pygame.display.flip()

    # run the game
    def run(self):
        while True:
            self.pong_input()
            if self.stat.active:
                self.ball.update_ball(self.player, self.pc)
                self.player.update()
                self.pc.update(self.ball)


# call main fucn to run game
if __name__=="__main__":
    Pong().run()