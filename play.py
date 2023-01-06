import cocos

class PlayLayer(cocos.layer.Layer):
    is_event_handler=True

    def __init__(self):
        super(PlayLayer, self).__init__()

        self.sample_text = cocos.text.Label("this is the play layer", position=(200, 200), font_size=12)
        self.add(self.sample_text)

    def on_key_press(self, key, modifiers): # go back to menu after pressing any button
        cocos.director.director.pop()