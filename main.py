import cocos
import menu

class StartingLayer(cocos.layer.Layer):
    def __init__(self):
        super(StartingLayer, self).__init__()
        
        self.bg_layer = menu.BGLayer()
        self.menu = menu.MenuLayer()

        self.add(self.bg_layer)
        self.add(self.menu)
        
cocos.director.director.init()
cocos.director.director.run(cocos.scene.Scene(StartingLayer()))