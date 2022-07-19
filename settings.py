class Settings:
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_wight = 1200
        self.screen_height = 800
        self.br_color = (230, 230, 230)
        self.ship_speed = 1.5
        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 10
        # Параметры пришельцев
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 - движение вправо, -1 - влево
        self.fleet_direction = 1

