from sys import exit
from random import randint

class Scene(object):
	
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)

class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
	def play(self):
		current_scene = self.scene_map.opening_scene() #?????
		
		while True:
			print "\n--------"
			next_scene_name = current_scene.enter() #?????
			
class Death(Scene):
	
	quips = [
		"You died. You kinda stuck at this.",
		"Your mom would be pround... if she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better at this."
	]
	
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
		
class CentralCorridor(Scene):
	def enter(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission is to get the neutron destruct bomb from the Weapons Armotry,"
		print "put it in the bridge, and blow the ship up after geeting into an"
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armotry when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hate filled body. He's blocking the door to the"
		print "Armotry and about to pull a weapon to blast you."
	
		action = raw_input("> ")
	
		if action == "shoot!":
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim. Your laser hits his costume but misses him entiely. This"
			print "makes him fly into a rage and blast you repeatedly in the face until"
			print "you are dead. Then he eats you"
			return 'death'
		
		elif action == "dodge":
			print "Like a world class boxer you dodge,weave,slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on "
			print "your head and eats you."
			return 'death'
		
		elif action == "tell a joke":
			print "Lucky for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print ""
			print ""
			print "While he is laughing you run up and shoot him square in the head"
			print "putting him down, they jump through the Weapons Armotry door."
			return 'laser_weapon_armory'
		
		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'
		
		
		
class Map(object):
	
	scenes = {'central_corridor':CentralCorridor()}
	
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		return self.scenes.get(scene_name)
	
	def opening_scene(self):
		return self.next_scene(self.start_scene)
	
	
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
		
		
		