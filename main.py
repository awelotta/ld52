import cocos
import pyglet
import sys
import os

from constants import W_LEN
import play

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
        # raise SystemExit ??? not work on awelotta's device
        os._exit(0) # exits

class StartingLayer(cocos.layer.Layer):
    def __init__(self):
        super(StartingLayer, self).__init__()

        self.bg_sprite = cocos.sprite.Sprite('resources/w_pink.jpg', position=(W_LEN*0.5, W_LEN*0.5))
        self.bg_sprite.scale = W_LEN / max(self.bg_sprite.width, self.bg_sprite.height) # chooses the one that DOESN'T fill the whole window
        self.add(self.bg_sprite)

        self.menu = MenuLayer()
        self.add(self.menu)
        
cocos.director.director.init(height=W_LEN, width=W_LEN, resizable=True)
cocos.director.director.run(cocos.scene.Scene(StartingLayer()))