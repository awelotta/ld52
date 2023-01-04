import cocos

class Menu(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(Menu, self).__init__()

        play_label = cocos.text.Label(
            'Play',
            position = (320, 300), # these will need to be dynamic resizing
            font_name = 'Times New Roman',
            font_size = 32,
            anchor_x = 'center', anchor_y = 'center'
        )
        settings_label = cocos.text.Label(
            'Settings',
            position = (320, 240),
            font_name = 'Times New Roman',
            font_size = 32,
            anchor_x = 'center', anchor_y = 'center'
        )
        quit_label = cocos.text.Label(
            'Quit',
            position = (320, 180),
            font_name = 'Times New Roman',
            font_size = 32,
            anchor_x = 'center', anchor_y = 'center'
        )

        self.add(play_label)
        self.add(settings_label)
        self.add(quit_label)

    def on_mouse_press(self, x, y, buttons, modifiers):
        # if inside each...
        quit_x, quit_y = cocos.director.director.get_virtual_coordinates(x, y)
        if x > quit_x - self.quit_label.width / 2 and x < quit_x + self.quit_label.width / 2 and y > quit_y - self.quit_label.height / 2 and y < quit_y + self.quit_label.height / 2:
            raise SystemExit


cocos.director.director.init(resizable=True)
cocos.director.director.run(cocos.scene.Scene(Menu()))