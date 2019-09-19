from paddle import Paddles


class Player:
    def __init__(self, setting, screen, image, player=True):
        self.player = player
        self.setting = setting
        self.image = image
        self.screen = screen

        self.score = 0

        # draw paddles
        if self.player:
            # set up position and paddles for player
            mid_screen = self.setting.screen_width // 2
            start_position = (self.setting.paddles_size // 2) - (mid_screen // 2)

            # top
            size = self.setting.top_bottom_size
            y = self.setting.top_position
            position = (start_position, y)
            self.player_top_paddles = Paddles(self.setting, self.screen, self.image, position, size, "top")
            # bottom
            y = self.setting.bottom_position
            position = (start_position, y)
            self.player_bottom_paddles = Paddles(self.setting, self.screen, self.image, position, size, "bottom")
            # side
            size = self.setting.side_size
            x = 0
            y = self.setting.side_position
            position = (x, y)
            self.player_side_paddles = Paddles(self.setting, self.screen, self.image, position, size, "side")

            # set up movement
            self.right = False
            self.left = False
            self.up = False
            self.down = False
        else:
            # set up position and paddles for PC
            mid_screen = self.setting.screen_width // 2
            start_position = ((self.setting.screen_width - mid_screen) // 2) + \
                             (mid_screen - (self.setting.paddles_size // 2))

            # top
            size = self.setting.top_bottom_size
            y = self.setting.top_position
            position = (start_position, y)
            self.pc_top_paddles = Paddles(self.setting, self.screen, self.image, position, size, "top")
            # bottom
            y = self.setting.bottom_position
            position = (start_position, y)
            self.pc_bottom_paddles = Paddles(self.setting, self.screen, self.image, position, size, "bottom")
            # side
            size = self.setting.side_size
            x = self.setting.screen_width - self.setting.paddles_width
            y = self.setting.side_position
            position = (x, y)
            self.pc_side_paddles = Paddles(self.setting, self.screen, self.image, position, size, "side")

    # draw and update all paddles
    def draw_paddles(self):
        self.player_top_paddles.draw_paddles()
        self.player_bottom_paddles.draw_paddles()
        self.player_side_paddles.draw_paddles()
        self.pc_top_paddles.draw_paddles()
        self.pc_bottom_paddles.draw_paddles()
        self.pc_side_paddles.draw_paddles()

    def update(self, ball=0):
        if self.player:
            move = (self.left, self.right, self.up, self.down)
            self.player_side_paddles.player_movement(move)
            self.player_bottom_paddles.player_movement(move)
            self.player_top_paddles.player_movement(move)
        else:
            self.pc_side_paddles.pc_movement(ball)
            self.pc_bottom_paddles.pc_movement(ball)
            self.pc_top_paddles.pc_movement(ball)
