import pygame, sys, os


class Sound:
    def __init__(self):
        # initializing
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
        pygame.mixer.init()

        self.win_sound = pygame.mixer.Sound('sound/win.wav')
        self.score_sound = pygame.mixer.Sound('sound/score.wav')
        self.collision_sound = pygame.mixer.Sound('sound/collision.wav')

    @staticmethod
    def game_sound(sound_effect, loop):
        channel = pygame.mixer.find_channel()
        if channel:
            channel.play(sound_effect, loop)



















