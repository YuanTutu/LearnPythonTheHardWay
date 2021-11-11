from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):#Scene 场景

    def enter(self):
        print("this scene is not yet configured.")#configured匹配
        print("subclass it and implement enter()")#implement工具  subclass把……划入子集/亚纲
        exit(1)

class Engine(object):#Engine引擎

    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()#current现在的
        last_scene = self.scene_map.next_scene('finished')

        print("^^ before while current_scene=",current_scene,"last_scene=",last_scene)
        while current_scene != last_scene:
            print("^top of while current_scene=",current_scene,"last_scene=",last_scene)
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            print("^end of while current_scene=",current_scene,"last_scene=",last_scene,"next_scene_name=",next_scene_name)

        #be sure to print the last scene
        print("<<<< end of play:current_scene=",current_scene)
        current_scene.enter()

class Death(Scene):#死亡场景
#[]列表{}字典
    quips = [
        "you died. you kinda suck at this.",#kinda 有点有几分
        "your mom wouldbe proud...if she were smarter.",
        "Such a luser.",
        "i have a small puppy that's better at this."
        "you're worse than your dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):#中央走廊

    def enter(self):
        print(dedent("""
            the gothons of planet percal #25 have invaded your ship and
            destroyed your entire crew.you are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the weapons armory,put it in rhe bridge.and
            blow the ship up after getting into an escape pod/

            you are running down the central corridor to the weapons
            armory  when a gothon jumps out,red scaly skin,dark grimy
            teeth,and evilclown costume flowing around his hate
            filled body.he's blocking the door to the armory and
            about to pull a weapon to blast you.
            """))

        action = input("> ")

        if action == "shoot!":
            print(dedent(""""
                quick on the draw you yank out your blaster and fire
                it at the gothon.his clown costume if flowing and
                moving around his body,which throws off your aim.
                your laser hits his costume but misses him entirely.
                this completely ruins his brand new costume his mother
                bought him,which makes him fly into an insane rage
                and blast you repeatedly in the face until you are
                dead.then he eats you.
                """))
            return 'death'

        elif action == "dodge!":
            print(dedent(""""
                like a world class boxer you dodge,weave,slip and
                slide right as the gothon's blaster cranks a laser
                past your head.in the middle of your artful dodge
                your foot slips and you bang your head on the metal
                wall and pass out .you wake up shortly after only to
                die as the gothon stomps on your head and eats you.
                """))
            return 'death'

        elif action == "tell a joke":
            print(dedent(""""
                lucky for you they made you learn gothon instults in
                the academy .you tell the one gothon joke you know:
                lbhe zbs sdad ewqad dsad.adsr dsadsds/
                wad read ffga.the gothon stops,tries
                not to laugh,then busts out laughing and can't move.
                while he's laughing you run up and shoot him square in
                the head putting him down,then jump through the
                weapon armory door.
                """))
            return 'laser_weapon_armory'

        else:
            print("does not compute!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            you do a dive roll into the weapon armory,crouch and scan
            the room for more gothons that might be hiding.it's dead
            quiet,too quiet.you stand up and run to the far side of
            the room and find the neutron bomb in its container.
            there's a keypad lock on the box and you need the code to
            get the bomb out.if you get the code wrong 10 times then
            the lock closes forever and you can't get the bomb.the
            code is 3 digits.
            """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print(">>>> code=",code)
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZEDDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                the container clicks open and the seal breaks,letting
                gas out.you grab the neutron bomb and run as fast as fast as
                you can to the bridge where you must place it in the
                right spot.
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                the lock buzzes one last time and then you hear a
                sickening melting sound as the mechanism is fused
                together.you decide to sit there,and finally the
                gothons blow up the ship from their ship and you die.
                """))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            you burst onto the bridge with the netron destruct bomb
            under your atm and surprise 5 gothons who are trying to
            take control of the ship.each of them has an even uglier
            clown costume than the last.they haven't pulled their
            weapons out yet,as they see the active bomb under your
            arm and don't want to set it off.
            """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                in a panic you throw the bomb at the group of gothons
                and make a leap for the door.right as you drop it a
                gothon shoots you right in the back killing you.as
                you die you see another gothon frantically try to
                disarm the bomb.you die knowing they wll probably
                blow up when it goes off.
                """))
            return 'death'

        elif action == 'slowly place the bomb':
            print(dedent("""
                you point your blaster at the bomb under your arm and
                the gothons put their hands up and start to sweat.
                you inch backward to the door,open it,and then
                carefully place the bomb on the floor,pointing your
                blaster at it .you then jump back through the door,
                punch the close button and blast the lock so the
                gothons can't get out.now that the bomb is placed
                you run to the escape pod to get off this tin can.
                """))
            return 'escape_pod'
        else:
            print("dose not compute!")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            you rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes.it seems
            like hardly any gothons are on the ship,so your run is
            clear of interfrence.you get to the chamber with the
            escape pods,and now need to pick one to take.some of
            them could be damaged but you don't have time to look.
            there's 5 pods ,which one do you take?
            """))

        good_pod = randint(1,5)
        print(">>> good_pod=",good_pod)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                you jump into pod {guess} and hit the eject button.
                the pod escapes out into the void of space,then
                implodes as the hull ruptures,crushing your body
                into jam jelly.
                """))
            return 'death'
        else:
            print(dedent("""
                you jump into pod {guess} and hit the eject button.
                the pod easily slides out into space heading to
                the planet below.as it flies to the planet,you look
                back and see your ship implode then explode like a
                bright star ,taking out the gothon ship at the same
                time. you won!
                """))
            return 'finished'


class Finished(Scene):

    def enter(self):
        print("you won!good job.")
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor':CentralCorridor(),
        'laser_weapon_armory':LaserWeaponArmory(),
        'the_bridge':TheBridge(),
        'escape_pod':EscapePod(),
        'death':Death(),
        'finished':Finished(),
    }

    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')#corridor走廊
a_game = Engine(a_map)
a_game.play()
