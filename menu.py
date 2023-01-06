import cocos
import pyglet

import play

# MenuLayer and BGLayer
# and a play scene

class MenuLayer(cocos.menu.Menu):
    def __init__(self):
        super(MenuLayer, self).__init__()

        choices = []
        choices.append(cocos.menu.MenuItem('Play', self.on_new_game))
        choices.append(cocos.menu.MenuItem('Quit', self.on_quit))
        self.create_menu(choices, cocos.menu.zoom_in(), cocos.menu.zoom_out())

    def on_new_game(self):
        cocos.director.director.push(cocos.scene.Scene(play.PlayLayer()))

    def on_quit(self):
        raise SystemExit # exits

class BGLayer(cocos.layer.Layer):
    # display some image
    def __init__(self):
        super(BGLayer, self).__init__()

        self.bg_sprite = cocos.sprite.Sprite('resources/w_pink.jpg', position=(600, 600))
        self.bg_sprite.scale = 1200 / max(self.bg_sprite.width, self.bg_sprite.height) # chooses the one that DOESN'T fill the whole window
        self.add(self.bg_sprite)