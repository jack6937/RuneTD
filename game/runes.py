from game import classes, shots

class BasicRune (classes.Rune):
    cost = 9
    shot_range = 5
    fire_speed = 1000
    
    image_name = 'Pink rune'
    shot_type = shots.StandardBullet
    
    def apply_effects(self, rune):
        rune.effects['damage'] += 1
    
    def remove_effects(self, rune):
        rune.effects['damage'] -= 1

class SlowRune (classes.Rune):
    cost = 10
    shot_range = 6
    fire_speed = 700
    
    image_name = 'Blue rune'
    shot_type = shots.SlowBullet
    
    def shoot(self):
        """Overriden to force finding of the least slowed target within range"""
        best_target = (None, 99999999)
        
        for e in self.game.enemies:
            if self.distance(e) <= self.shot_range:
                if e.slowed < best_target[1]:
                    best_target = (e, e.slowed)
        
        self.target = best_target[0]
        
        return super(SlowRune, self).shoot()
    
    def apply_effects(self, rune):
        rune.shot_range += 1
    
    def remove_effects(self, rune):
        rune.shot_range -= 1

class SplashRune (classes.Rune):
    cost = 13
    shot_range = 4
    fire_speed = 1000
    
    image_name = 'Yellow rune'
    shot_type = shots.SplashBullet
    
    def apply_effects(self, rune):
        rune.fire_speed /= 1.1
    
    def remove_effects(self, rune):
        rune.fire_speed *= 1.1

class PoisonRune (classes.Rune):
    cost = 12
    shot_range = 9
    fire_speed = 1000
    
    image_name = 'Green rune'
    shot_type = shots.PoisonBullet
    
    def apply_effects(self, rune):
        rune.effects['damage'] -= 1
        rune.fire_speed /= 1.3
    
    def remove_effects(self, rune):
        rune.effects['damage'] += 1
        rune.fire_speed *= 1.3

class CriticalRune (classes.Rune):
    cost = 30
    shot_range = 9
    fire_speed = 1000
    
    image_name = 'Red rune'
    shot_type = shots.CriticalBullet
    
    def apply_effects(self, rune):
        rune.effects['damage'] += 1
        rune.fire_speed *= 1.1
    
    def remove_effects(self, rune):
        rune.effects['damage'] -= 1
        rune.fire_speed /= 1.1

class WeakenRune (classes.Rune):
    cost = 8
    shot_range = 9
    fire_speed = 500
    
    image_name = 'Teal rune'
    shot_type = shots.WeakenBullet
    
    def apply_effects(self, rune):
        rune.shot_range += 0.5
    
    def remove_effects(self, rune):
        rune.shot_range -= 0.5
    
    def shoot(self):
        """Pick a target with the most armour left"""
        best_target = (None, None)
        
        for e in self.game.enemies:
            if self.distance(e) <= self.shot_range:
                if best_target[1] == None or e.armour > best_target[1]:
                    best_target = (e, e.armour)
        
        self.target = best_target[0]
        
        return super(WeakenRune, self).shoot()

class NuclearRune (classes.Rune):
    cost = 40
    shot_range = 15
    fire_speed = 2000
    
    image_name = 'Nuclear rune'
    shot_type = shots.NuclearBullet
    
    def apply_effects(self, rune):
        rune.effects['damage'] += 5
        rune.fire_speed *= 1.2
    
    def remove_effects(self, rune):
        rune.effects['damage'] -= 5
        rune.fire_speed /= 1.2
        rune.effects['damage'] -= 1
        rune.fire_speed /= 0.8
        
class DoumMal (classes.Rune):
    cost = 0
    shot_range = 0
    fire_speed = 0

    image_name = 'Doum rune'

