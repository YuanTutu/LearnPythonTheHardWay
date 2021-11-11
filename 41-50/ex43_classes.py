class Scene(object):#Scene 场景

    def enter(self):
        pass


class Engine(object):#Engine引擎

    def __init__(self,scene_map):
        pass

    def play(self):
        pass

class Death(Scene):#死亡场景

    def enter(self):
        pass

class CentralCorridor(Scene):#中央走廊

    def enter(self):
        pass

class LaserWeaponArmory(Scene):#激光武器库

    def enter(self):
        pass

class TheBridge(Scene):#主控舱

    def enter(self):
        pass

class EscapePod(Scene):#救生舱

    def enter(self):
        pass


class Map(object):

    def __init__(self,start_scene):
        pass

    def next_scene(self,scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')#corridor走廊
a_game = Engine(a_map)
a_game.play()
