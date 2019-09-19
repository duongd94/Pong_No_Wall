import pygame


class PlayerScore:
    def __init__(self):
        self.clear_stat()

        self.active = False

    def clear_stat(self):
        self.player_score = 0
        self.pc_score = 0
        self.winner = ""
        self.active = False
        self.display_home_screen = False