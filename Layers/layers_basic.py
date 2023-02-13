import cocos
from subject.personage.evil import Evil
from subject.personage.hero import Hero
from cocos.director import director

KEY_W = 119
KEY_A = 97
KEY_D = 100
KEY_S = 115
KEY_Q = 113
KEY_SPACE = 32


class FirstLayer(cocos.layer.ColorLayer):
    def __init__(self):
        sprite_hero = Hero(
            image='a829bf0ef4118649b7e5bc008093c6d4.png',
            scale=0.3,
            x=250,
            y=150
        )
        self.is_event_handler = True
        super(FirstLayer, self).__init__(360, 0, 0, 255)
        sprite_hero.is_fliped = False
        self.add(sprite_hero, z=1)

        sprite_evil = Evil(
            image='a829bf0ef4118649b7e5bc008093c6d4.png',
            scale=0.3,
            x=550,
            y=150
        )
        sprite_evil.is_fliped = False
        self.add(sprite_evil, z=1)
        hero_health = sprite_hero.health

    def on_key_release(self, key, mod):
        pawn = self.children[0][1]
        if key == KEY_W:
            pawn.stop_up()
        elif key == KEY_A:
            pawn.stop_left()
        elif key == KEY_D:
            pawn.stop_right()
        elif key == KEY_S:
            pawn.stop_down()
        elif key == KEY_Q:
            pawn.stop_attack()

    def on_key_press(self, key, mod):
        pawn = self.children[0][1]
        if key == KEY_W:
            pawn.to_up()
        elif key == KEY_A:
            pawn.to_left()
        elif key == KEY_D:
            pawn.to_right()
        elif key == KEY_S:
            pawn.to_down()
        elif key == KEY_SPACE:
            pawn.jump()
            print(self.children)
        elif key == KEY_Q:
            pawn.attack()

    def on_draw(self):
        pawn_1 = self.children[0][1]
        pawn_2 = self.children[1][1]
        rect_1 = pawn_1.get_rect()
        rect_2 = pawn_2.get_rect()
        print(pawn_1.health, pawn_2.health)
        # print(rect_1.get_top(), rect_2.get_top())
        if rect_1.get_bottom() <= rect_2.get_top() and rect_1.get_right() >= rect_2.get_left():
            if pawn_1.actions:
                pawn_1.remove_action(pawn_1.actions[0])
            if pawn_1.is_attacked:
                pawn_2.health -= 1
            else:
                pawn_1.health -= 1
        if pawn_1.health == -1:
            director.pop()
        if pawn_2.health == -1:
            self.remove(pawn_2)






