from game import classes, shots

class PinkRune (classes.Rune):
    cost = 10
    shot_range = 10
    
    image_name = 'Pink rune'
    shot_type = shots.PinkBullet
    
    def __init__(self, game, position):
        super(PinkRune, self).__init__(game, position)