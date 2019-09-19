import pygame, random
from setting import Setting
from pygame.sprite import Sprite


# class to manage the ball
class Ball(Sprite):
    def __init__(self, setting, screen, sound, stat, score_board):
        # super().__init__() to make your call, which is concise and does not require you to reference the parent
        # OR class names explicitly, which can be handy.
        super(Ball, self).__init__()
        # initialize the ball
        self.setting = setting
        self.screen = screen
        self.sound = sound
        self.stat = stat
        self.score_board = score_board
        self.radius = self.setting.B_radius
        self.color = self.setting.B_color
        # put the ball in the middle
        self.mid_x = self.setting.width // 2
        self.mid_y = self.setting.height // 2

        # rect
        self.rect = pygame.draw.circle(self.screen, self.color,
                                       (self.mid_x, self.mid_y), self.radius)

        # speed of the ball
        self.speed_x = self.setting.B_speed_x
        self.speed_y = self.setting.B_speed_y

    # func for draw and update the ball
    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color,
                           (self.mid_x, self.mid_y), self.radius)

    def update_ball(self, player, pc):
        # note:convert to int to fix error with move the ball
        self.x += int(self.B_speed_x)
        self.y += int(self.B_speed_y)
        self.rect.x = self.x
        self.rect.y = self.y

        # interaction with paddles and boundaries
        self.check_boundary()
        self.check_players_paddles(player, pc)

        # check the score for winner and stop the game
        self.check_winner()

    # func to rand change ball's speed and direction
    def ball_speed(self, paddles):
        paddles_size = self.setting.paddles_size

        # change in vertical
        if paddles.type == "side":
            self.ball_speed_x -= self.ball_speed_x
            change_y = self.y - (paddles_size.y + (paddles_size / 2))
            self.ball_speed_y = change_y * self.setting.velocity

        # change in horizontal
        if paddles.type == "top" or paddles.type == "bottom":
            self.ball_speed_y -= self.ball_speed_y
            change_x = self.x - (paddles.x + (paddles_size / 2))
            self.ball_speed_x = change_x * self.setting.ball_velocity

    # func for checking paddles
    def check_paddles(self, paddles):
        # check for collision
        collision = pygame.sprite.collide_rect(paddles, self)
        # make noise and rand change speed
        if collision:
            self.sound.game_sound(self.sound.collision_sound, 0)
            self.random_speed(paddles)

    # func to check collision from all players' paddles
    def check_players_paddles(self, player, pc):
        self.check_paddles(player.top)
        self.check_paddles(player.side)
        self.check_paddles(player.bottom)
        self.check_paddles(pc.top)
        self.check_paddles(pc.side)
        self.check_paddles(pc.bottom)

    # func for checking boundary
    def check_boundary(self):
        if self.x > self.setting.width or self.x < 0 or self.y > self.setting.height or self.y < 0:
            # update score
            if self.x > self.mid_x:
                self.stat.player_score += 1
                self.score_board.player_score()
            else:
                self.stat.pc_score += 1
                self.score_board.pc_score()

            # make noise
            self.sound.game_sound(self.sound.score_sound, 0)
            # reset the match
            self.reset()

    # check for winner
    def check_winner(self):
        if self.stat.player_score == 5:
            self.stat.winner = "You Win"
        elif self.stat.pc_score == 5:
            self.stat.winner == "PC Win"

        if self.stat.winner != "":
            self.stat.active = False
            self.score_board.winner_screen()
            self.sound.game_sound(self.sound.win_sound, 0)

    # reset the game/match
    def reset(self):
        self.x = self.setting.width // 2
        self.y = self.setting.height // 2
        self.ball_speed_x = self.setting.random_speed()
        self.ball_speed_y = self.setting.random_speed()


