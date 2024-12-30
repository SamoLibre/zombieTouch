import pgzero
import random
tile = Actor('tilecastle')
tile.width = 66
tile.height = 120
WIDTH = tile.width * 10
HEIGHT = tile.height * 5
TITLE = "Zombie Touch"
mod = "menu"
map = [[0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0]]

class Character:
    def __init__(self, images, pos):
        self.images = images
        self.index = 0
        self.actor = Actor(self.images[self.index], pos)
        self.pos = pos
        self.moving = False

    def draw(self):
        self.actor.draw()

    def update(self):
        if self.moving:
            self.index = (self.index + 1) % len(self.images)
            self.actor.image = self.images[self.index]
karakter = Character(["karakterwalk1", "karakterwalk2"], (90, 100))
class Eye:
    def __init__(self, images, pos):
        self.images = images  
        self.index = 0
        self.animtime = 0
        self.movetime = 0  
        self.actor = Actor(images[self.index], self.random_position())

    def random_position(self):
        xrand = [90 + 60 * i for i in range(6)]
        yrand = [120 + 60 * i for i in range(4)]
        x = random.choice(xrand)
        y = random.choice(yrand)
        return x, y
    
    def reset_position(self):  
        self.actor.x, self.actor.y = self.random_position()

    def update(self):
        self.animtime += 1
        if self.animtime > 10: 
            self.animtime = 0
            self.index = (self.index + 1) % len(self.images)
            self.actor.image = self.images[self.index]

        self.movetime += 1
        if self.movetime > 10:  
            self.movetime = 0
            self.move()

    def move(self):
        directions = [(0, -60), (0, 60), (-60, 0), (60, 0)]
        randx, randy = random.choice(directions)
        new_x = self.actor.x + randx
        new_y = self.actor.y + randy
        if new_x > 60 and new_x < WIDTH -60 and new_y > 60 and new_y < HEIGHT -60:
            self.actor.x = new_x
            self.actor.y = new_y

    def draw(self):
        self.actor.draw()

eye = Eye(["googly-a (1)", "googly-b (1)", "googly-c (1)", "googly-d (1)", "googly-e (1)"], (600, 100))
class Bat:
    def __init__(self, images, pos):
        self.images = images  
        self.index = 0  
        self.animtime = 0 
        self.movetime = 0 
        self.actor = Actor(images[self.index], self.random_position()) 

    def random_position(self):
        xrand= [90 + 60 * i for i in range(6)]
        yrand = [120 + 60 * i for i in range(4)]
        x = random.choice(xrand)
        y = random.choice(yrand)
        return x, y
    
    def reset_position(self):  
        self.actor.x, self.actor.y = self.random_position()

    def update(self):
        # Animasyon
        self.animtime += 1
        if self.animtime > 10: 
            self.animtime = 0
            self.index = (self.index + 1) % len(self.images)
            self.actor.image = self.images[self.index]

        self.movetime += 1
        if self.movetime > 10:
            self.movetime = 0
            self.move()

    def move(self):
        directions = [(0, -60), (0, 60), (-60, 0), (60, 0)]
        randx, randy = random.choice(directions)
        new_x = self.actor.x + randx
        new_y = self.actor.y + randy
        if new_x > 60 and new_x < WIDTH -60 and new_y > 60 and new_y < HEIGHT -60:
            self.actor.x = new_x
            self.actor.y = new_y

    def draw(self):
        self.actor.draw()
bat = Bat(["bat", "bat_hang", "bat_fly"], (600, 100))
class Zombie:
    def __init__(self, images, pos):
        self.images = images
        self.index = 0
        self.actor = Actor(self.images[self.index], pos)
        self.pos = pos
        self.animtime = 0

    def update(self):
        self.animtime += 1
        if self.animtime > 30:  
            self.animtime = 0
            self.index = (self.index + 1) % len(self.images) 
            self.actor.image = self.images[self.index]  
    def draw(self):
        self.actor.draw() 
zombie = Zombie(["zombiee1", "zombiee2", "zombiee3"], (630, 40))

banner = Actor("banner")
banner.topleft = 0, 0
footer = Actor("footer")
footer.topleft = 0, 580

start = Actor("start", (WIDTH // 2, 300))
sound = Actor("sound", (WIDTH // 2, 400))
nosound = Actor("nosound", (WIDTH // 2, 500))
exitbutton = Actor("exit", (WIDTH -100, 80))
exitbutton2 = Actor("exit2", (30, 24))
winscreen = Actor("win (1)")
is_sound = True

def draw():
    if mod == "game":
        banner.draw()
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 0:
                    tile.topleft = j*60, i*60+20
                    tile.draw()
        karakter.draw()
        eye.draw()
        bat.draw()
        zombie.draw()
        footer.draw()
        exitbutton2.draw()
    elif mod == "menu":
        screen.fill((0, 0, 0))
        start.draw()
        sound.draw()
        exitbutton.draw()
    elif mod == "gameover":
        screen.fill((0, 0, 0))
        screen.draw.text("GAME OVER", center=(WIDTH // 2, 300), color="red", fontsize=60)
        screen.draw.text("Press 'Space' to try again", center=(WIDTH // 2, 400), color="white", fontsize=30)
    elif mod == "win":
        screen.fill((0, 0, 0))
        winscreen.draw()

def all_music():
    if is_sound:
        music.play("allmusic")
        music.set_volume(0.5)

def no_music():
    music.stop()

all_music()
def win_music():
    music.play("win")
    music.set_volume(1)

def update():
    global mod, is_sound
    if mod == "game":
        karakter.update()
        eye.update()
        bat.update()
        zombie.update()
        if karakter.actor.colliderect(eye.actor) or karakter.actor.colliderect(bat.actor):
            mod = "gameover"
            no_music()
        elif karakter.actor.colliderect(zombie.actor):
            mod = "win"
            is_sound = False
            win_music()
    
def on_key_down(key):
    global mod, bat, eye
    if mod == "game":
        karakter.moving = True
        if key == keys.RIGHT and karakter.actor.x < WIDTH - 60:
            karakter.actor.x += 60
        if key == keys.LEFT and karakter.actor.x -60 >0:
            karakter.actor.x -= 60
        if key == keys.UP and karakter.actor.y -60 > 0:
            karakter.actor.y -= 60
        if key == keys.DOWN and karakter.actor.y + 60 < HEIGHT - 60:
            karakter.actor.y += 60
    elif mod == "gameover" and key == keys.SPACE:
        mod = "menu"
        karakter.actor.x = 90
        karakter.actor.y = 100
        eye.reset_position()
        bat.reset_position()
        all_music()

def on_key_up(key):
    karakter.moving = False

def on_mouse_down(pos):
    global mod, is_sound
    if mod == "menu":
        if start.collidepoint(pos):
            mod = "game"
        if sound.collidepoint(pos) and sound.image == "sound":
            sound.image = "nosound"
            no_music()
        elif sound.collidepoint(pos) and sound.image == "nosound":
            sound.image = "sound"
            all_music()
        if exitbutton.collidepoint(pos):
            exit()
    if mod == "game":
        if exitbutton2.collidepoint(pos):
            mod ="menu"