import pygame


class ScoreBoard:
    def __init__(self, setting, screen, stat):
        self.setting = setting
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stat = stat

        self.color = (0, 0, 128)
        self.style = pygame.font.SysFont(None, 60)

        # self.clear_score_board()

    def draw_net(self):
        width = self.setting.net_width
        height = self.setting.net_height
        color = self.setting.net_color
        net_offset = self.setting.net_offset

        x = (self.setting.screen_width // 2) - (width // 2)
        y = 0

        dashes = self.setting.screen_height // height

        for dash in range(dashes):
            pygame.draw.rect(self.screen, color, (x, y, width, height))
            y += (net_offset + height)


   # def clear_scoreboard(self):



