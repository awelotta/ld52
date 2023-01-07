import pyglet
import cocos

class PlayLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(PlayLayer, self).__init__()

        # background image
        self.background = cocos.sprite.Sprite('resources/w_pink.jpg')
        self.add(self.background)

        self.grid = FarmLayer()
        self.add(self.grid)

        self.hud = HUDLayer()
        self.add(self.hud)

class FarmLayer(cocos.layer.Layer):
    def __init__(self):
        super(FarmLayer, self).__init__()
        def do_nothing(*x):
            return

class HUDLayer(cocos.layer.Layer):
    # elements such as:
    # - season
    # - fast forward toggle
    # - toolbar to plant, harvest, dig etc (you can only harvest ready crops and dig up non ready crops,
    #   maybe don't need buttons; accidental digging is bad though)
    #   - add shortcuts for these (numbers; qwer,asdf,zxcv?, space to toggle dig)
    # - money indicator
    # - cooking/inventory button
    # - a pause button? (Non essential, will get to when necessary)

    def __init__(self):
        super(HUDLayer, self).__init__()

class CookingLayer(cocos.layer.Layer):
    # cook button
    # grid of plants harvested, and other things... maybe plants have different drops and drop rates -- TBD
    # shows salad after cooking (or maybe also things besides salads) and the price
    #   press an "ok" button to returns to cooking menu
    
    def __init__(self):
        super(CookingLayer, self).__init__()