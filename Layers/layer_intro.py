import cocos
from cocos.actions import ScaleBy, Repeat, Reverse, MoveBy
from cocos.director import director


class IntroLayer(cocos.layer.ColorLayer):
    def __init__(self):
        self.is_event_handler = True
        super(IntroLayer, self).__init__(360, 0, 0, 255)
        label_1 = cocos.text.Label(
            text="Нажмите enter для продолжения",
            position=(320,40),
            font_name="Times New Roman",
            font_size=10,
            anchor_x="center",
            anchor_y="center")
        label_2 = cocos.text.Label(
            text="Poputka game",
            position=(320, 340),
            font_name="",
            font_size=60,
            anchor_x="center",
            anchor_y="center")
        self.add(label_1)
        self.add(label_2)
        scale = ScaleBy(1.5, duration=1.5)
        label_1.do(Repeat(scale + Reverse(scale)))

    def on_key_press(self, key, mod):
        if key == 65293:
            director.pop()
