import cocos
from cocos.actions import ScaleBy, Repeat, Reverse


class OverLayer(cocos.layer.ColorLayer):
    def __init__(self):
        self.is_event_handler = True
        super(OverLayer, self).__init__(360, 0, 0, 255)
        label_1 = cocos.text.Label(
            text="Game over",
            position=(320, 340),
            font_name="",
            font_size=60,
            anchor_x="center",
            anchor_y="center")
        self.add(label_1)
        scale = ScaleBy(1.5, duration=1.5)
        label_1.do(Repeat(scale + Reverse(scale)))