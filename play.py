import cocos

from constants import W_LEN
import toolbar

class PlayLayer(cocos.layer.Layer):
    # elements such as:
    # - season
    # - toolbar to plant, harvest, dig etc (you can only harvest ready crops and dig up non ready crops,
    #   maybe don't need buttons; accidental digging is bad though)
    #   - add shortcuts for these (numbers; qwer,asdf,zxcv?, space to toggle dig)
    # - money indicator
    # - cooking/inventory button
    # - a pause button? (Non essential, will get to when necessary)

    is_event_handler = True

    def __init__(self):
        super(PlayLayer, self).__init__()

        # background image
        self.background = cocos.sprite.Sprite('resources/sample_background.png', position=(W_LEN*0.5, W_LEN*0.5))
        self.add(self.background)

        # farm
        self.farm = cocos.sprite.Sprite('resources/sample_farm.png', position=(W_LEN*0.5, W_LEN*0.6))
        self.add(self.farm)

        # fast-forward
        self.ff_button = cocos.sprite.Sprite('resources/ff_button.png', position=(W_LEN*0.9, W_LEN*0.9))
        self.add(self.ff_button)

        # season
        self.season_indicator = cocos.sprite.Sprite('resources/season_indicator.png', position=(W_LEN*0.05, W_LEN*0.9))
        self.add(self.season_indicator)

        # toolbar

        # money
        self.money = 1000
        self.money_display = cocos.text.Label('$%d' % self.money, position=(W_LEN*0.05, W_LEN*0.05), font_size=48, color=(0, 0, 0, 255))
        self.add(self.money_display)
        
        # cooking
        self.is_cooking_menu_open = False
        self.cooking_button = cocos.sprite.Sprite('resources/cooking_button.png', position=(W_LEN*0.9, W_LEN*0.05))
        self.add(self.cooking_button)

    def on_mouse_press(self, x, y, button, modifiers):
        # NOTE: button==1 if left-click

        if not self.is_cooking_menu_open:
            # farm

            # fast-forward
            if self.ff_button.contains(x, y) and button==1:
                print("fast-forward pressed")

            # toolbar

            # cooking
            if self.cooking_button.contains(x, y) and button==1:
                self.is_cooking_menu_open = True
                cooking_menu = CookingLayer()
                self.add(cooking_menu)
                print("live!")

class CookingLayer(cocos.layer.Layer):
    # grid showing inv; grid of plants harvested, and other things... maybe plants have different drops and drop rates -- TBD
    # cook button
    # -> shows salad after cooking (or maybe also things besides salads) and the price
    #    press an "ok" button to returns to cooking menu

    is_event_handler = True
    
    def __init__(self):
        super(CookingLayer, self).__init__()
        self.inventory = cocos.sprite.Sprite('resources/cooking_menu.png', position=(W_LEN*0.5, W_LEN*0.5))
        self.add(self.inventory)

        self.cooking_button = cocos.sprite.Sprite('resources/ff_button.png', position=(W_LEN*0.5, W_LEN*0.05))
        self.add(self.cooking_button)

        print()

    def on_mouse_press(self, x, y, button, modifiers):
        if not self.cooking_button.contains(x, y) and not self.inventory.contains(x, y) and button==1:
            self.parent.is_cooking_menu_open = False
            self.kill()
            print("killed")