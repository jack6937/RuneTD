import random

from game import classes

class StandardBullet (classes.Bullet):
    move_speed = 0.4
    damage = 2
    
    def __init__(self, game, position, target, rune=None):
        super(StandardBullet, self).__init__(game, position, target, rune)
        self.image = game.resources['Pink bullet']
    
    def apply_effects(self):
        pass

class SlowBullet (classes.Bullet):
    move_speed = 0.7
    damage = 0.1
    
    def __init__(self, game, position, target, rune=None):
        super(SlowBullet, self).__init__(game, position, target, rune)
        self.image = game.resources['Blue bullet']
    
    def apply_effects(self):
        self.sprite_target.slowed = 50

class SplashBullet (classes.Bullet):
    move_speed = 0.25
    damage = 1
    splash_range = 7
    seeking = False
    
    def __init__(self, game, position, target, rune=None):
        super(SplashBullet, self).__init__(game, position, target, rune)
        self.image = game.resources['Yellow bullet']
        
        # Not seeking, it'll hit and explode
        self.sprite_target = None
    
    def apply_effects(self):
        # Find all enemies withing splash reach
        within_reach = []
        
        for e in self.game.enemies:
            if self.distance(e.position) <= self.splash_range:
                within_reach.append(e)
        
        for enemy in within_reach[:]:
            enemy.damage(self.damage)

class PoisonBullet (classes.Bullet):
    move_speed = 0.7
    damage = 0
    
    def __init__(self, game, position, target, rune=None):
        super(PoisonBullet, self).__init__(game, position, target, rune)
        self.image = game.resources['Green bullet']
    
    def apply_effects(self):
        self.sprite_target.poisoned += 100

class CriticalBullet (classes.Bullet):
    move_speed = 0.7
    damage = 0
    
    def __init__(self, game, position, target, rune=None):
        super(CriticalBullet, self).__init__(game, position, target, rune)
        self.image = game.resources['Red bullet']
    
    def apply_effects(self):
        pass
    
    def hit(self):
        if random.random() > 0.2:
            self.damage = 100
        super(CriticalBullet, self).hit()

class WeakenBullet (classes.Bullet):
    move_speed = 0.7
    damage = 0
    
    def __init__(self, game, position, target, rune=None):
        super(WeakenBullet, self).__init__(game, position, target, rune)
        self.image = game.resources['Teal bullet']
    
    def apply_effects(self):
        self.sprite_target.armour -= 1

class NuclearBullet (classes.Bullet):
    move_speed = 0.7
    damage = 0
    
    def __init__(self, game, position, target, rune=None):
        super(NuclearBullet, self).__init__(game, position, target, rune)
        self.image = game.resources['Emerald bullet']
    
    def apply_effects(self):
        pass
    
    def hit(self):
        if random.random() > 0.2:
            self.damage = 200
            super(NuclearBullet, self).hit()

