import pygame
from pygame.rect import Rect
import random
import math
import time
import sys, os

# Import .py files
import settings as s

# Initilize pygame
pygame.init()
pygame.font.init()

# Define screen
win = pygame.display.set_mode((1024, 576), pygame.NOFRAME)
pygame.display.set_caption("Pygame Project")

# NEW SHIT JUST FOR .EXE ---------------------------------
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# NEW SHIT JUST FOR .EXE ---------------------------------


font = pygame.font.Font(None, 30)
HELLO_GUYS = font.render("Loading: ", True, (255, 255, 255))
win.blit(HELLO_GUYS, [0, 0])
pygame.display.update()

# Defining the sprites / images
win.fill((0, 0, 0))
HELLO_GUYS = font.render("Loading: Road1", True, (255, 255, 255))
win.blit(HELLO_GUYS, [0, 0])
pygame.display.update()
Road1 = pygame.image.load(resource_path("Background\\Road1.png"))
Road1_rect = Road1.get_rect()
win.fill((0, 0, 0))
HELLO_GUYS = font.render("Loading: Road2", True, (255, 255, 255))
win.blit(HELLO_GUYS, [0, 0])
pygame.display.update()
Road2 = pygame.image.load(resource_path("Background\\Road1.png"))
Road2_rect = Road2.get_rect()
win.fill((0, 0, 0))
HELLO_GUYS = font.render("Loading: Car_Wash", True, (255, 255, 255))
win.blit(HELLO_GUYS, [0, 0])
pygame.display.update()
Car_Wash = pygame.image.load(resource_path("Background\\Car_Wash.jpg"))
Car_Wash_rect = Car_Wash.get_rect()
win.fill((0, 0, 0))
HELLO_GUYS = font.render("Loading: CarDrive", True, (255, 255, 255))
win.blit(HELLO_GUYS, [0, 0])
pygame.display.update()
CarDrive = pygame.mixer.music.load(resource_path("Sound\\Car-driving.wav"))
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)


win.fill((0, 0, 0))
HELLO_GUYS = font.render("Loading: Long Road", True, (255, 255, 255))
win.blit(HELLO_GUYS, [0, 0])
pygame.display.update()
LongRoad = pygame.image.load(resource_path("Background\\Sad Kid Dies.png"))
LongRoad_rect = LongRoad.get_rect()


win.fill((0, 0, 0))
HELLO_GUYS = font.render("Loading: splat sfx", True, (255, 255, 255))
win.blit(HELLO_GUYS, [0, 0])
pygame.display.update()
splat = pygame.mixer.Sound(resource_path("Sound\\sound-effect-hd.wav"))


Flash = pygame.Surface((win.get_width(), win.get_height()), pygame.SRCALPHA)
Flash.fill((255, 255, 255))
Flash.set_alpha(0)

Road2_rect.y = 0-Road2.get_height()

clock = pygame.time.Clock()


points = 1




class Car():
    def __init__(self):
        global re, inspect
        self.x = 250
        self.y = 200
        self.speed = 10
        win.fill((0, 0, 0))
        HELLO_GUYS = font.render("Loading: Car1", True, (255, 255, 255))
        win.blit(HELLO_GUYS, [0, 0])
        pygame.display.update()
        self.small_Car1 = pygame.image.load(resource_path("Car\\Car1.png"))
        self.Car1 = pygame.transform.scale(self.small_Car1, (300, 300))
        self.Car1_rect = self.Car1.get_rect()

        win.fill((0, 0, 0))
        HELLO_GUYS = font.render("Loading: Car2", True, (255, 255, 255))
        win.blit(HELLO_GUYS, [0, 0])
        pygame.display.update()
        self.small_Car2 = pygame.image.load(resource_path("Car\\Car2.png"))
        self.Car2 = pygame.transform.scale(self.small_Car2, (300, 300))
        self.Car2_rect = self.Car2.get_rect()


        win.fill((0, 0, 0))
        HELLO_GUYS = font.render("Loading: Car3", True, (255, 255, 255))
        win.blit(HELLO_GUYS, [0, 0])
        pygame.display.update()
        self.small_Car3 = pygame.image.load(resource_path("Car\\Car3.png"))
        self.Car3 = pygame.transform.scale(self.small_Car3, (300, 300))
        self.Car3_rect = self.Car3.get_rect()
        

        win.fill((0, 0, 0))
        HELLO_GUYS = font.render("Loading: Car4", True, (255, 255, 255))
        win.blit(HELLO_GUYS, [0, 0])
        pygame.display.update()
        self.small_Car4 = pygame.image.load(resource_path("Car\\Car4.png"))
        self.Car4 = pygame.transform.scale(self.small_Car4, (300, 300))
        self.Car4_rect = self.Car4.get_rect()
        global source


        win.fill((0, 0, 0))
        HELLO_GUYS = font.render("Loading: Car5", True, (255, 255, 255))
        win.blit(HELLO_GUYS, [0, 0])
        pygame.display.update()
        import re, inspect 
        self.small_Car5 = pygame.image.load(resource_path("Car\\Car5.png"))
        self.Car5 = pygame.transform.scale(self.small_Car5, (300, 300))
        self.Car5_rect = self.Car5.get_rect()


        win.fill((0, 0, 0))
        HELLO_GUYS = font.render("Loading: Car6", True, (255, 255, 255))
        win.blit(HELLO_GUYS, [0, 0])
        pygame.display.update()
        self.small_Car6 = pygame.image.load(resource_path("Car\\Car6.png"))
        self.Car6 = pygame.transform.scale(self.small_Car6, (300, 300))
        self.Car6_rect = self.Car6.get_rect()
        

        win.fill((0, 0, 0))
        HELLO_GUYS = font.render("Loading: Car7", True, (255, 255, 255))
        win.blit(HELLO_GUYS, [0, 0])
        pygame.display.update()
        self.small_Car7 = pygame.image.load(resource_path("Car\\Car7.png"))
        self.Car7 = pygame.transform.scale(self.small_Car7, (300, 300))
        self.Car7_rect = self.Car7.get_rect()


        win.fill((0, 0, 0))
        HELLO_GUYS = font.render("Loading: Car8", True, (255, 255, 255))
        win.blit(HELLO_GUYS, [0, 0])
        pygame.display.update()
        self.small_Car8 = pygame.image.load(resource_path("Car\\Car8.png"))
        self.Car8 = pygame.transform.scale(self.small_Car8, (300, 300))
        self.Car8_rect = self.Car8.get_rect()


        win.fill((0, 0, 0))
        HELLO_GUYS = font.render("Loading: Car9", True, (255, 255, 255))
        win.blit(HELLO_GUYS, [0, 0])
        pygame.display.update()
        self.small_Car9 = pygame.image.load(resource_path("Car\\Car9.png"))
        self.Car9 = pygame.transform.scale(self.small_Car9, (300, 300))
        self.Car9_rect = self.Car9.get_rect()


        win.fill((0, 0, 0))
        HELLO_GUYS = font.render("Loading: Car10", True, (255, 255, 255))
        win.blit(HELLO_GUYS, [0, 0])
        pygame.display.update()
        self.small_Car10 = pygame.image.load(resource_path("Car\\Car10.png"))
        self.Car10 = pygame.transform.scale(self.small_Car10, (300, 300))
        self.Car10_rect = self.Car10.get_rect()


        win.fill((0, 0, 0))
        HELLO_GUYS = font.render("Loading: Car11", True, (255, 255, 255))
        win.blit(HELLO_GUYS, [0, 0])
        pygame.display.update()
        self.small_Car11 = pygame.image.load(resource_path("Car\\Car11.png"))
        self.Car11 = pygame.transform.scale(self.small_Car11, (300, 300))
        self.Car11_rect = self.Car11.get_rect()



        self.Wash1 = pygame.mixer.Sound(resource_path("Sound\\Wash1.wav"))
        self.Wash1.set_volume(0.5)

        self.Car_Surface = pygame.Surface(self.Car1.get_size())
        self.Car_Surface.blit(self.Car1, (0, 0))
        self.Car_Surface.set_colorkey((85, 255, 0))
        self.slowed = False
        self.IsWashing = False
        self.n = 0
        self.lasttime = time.time()
        self.WillFinish = False
        source = inspect.getsource(sys.modules[__name__])
        
    
    def Displaying(self):
        win.blit(self.Car_Surface, (self.x, self.y))
        if points <= 1:
            self.Car_Surface.blit(self.Car1, (0, 0))
        elif points <= 2:
            self.Car_Surface.blit(self.Car2, (0, 0))
        elif points <= 3:
            self.Car_Surface.blit(self.Car3, (0, 0))
        elif points <= 4:
            self.Car_Surface.blit(self.Car4, (0, 0))
        elif points <= 5:
            self.Car_Surface.blit(self.Car5, (0, 0))
        elif points <= 6:
            self.Car_Surface.blit(self.Car6, (0, 0))
        elif points <= 7:
            self.Car_Surface.blit(self.Car7, (0, 0))
        elif points <= 8:
            self.Car_Surface.blit(self.Car8, (0, 0))
        elif points <= 9:
            self.Car_Surface.blit(self.Car9, (0, 0))
        elif points <= 10:
            self.Car_Surface.blit(self.Car10, (0, 0))
        elif points <= 11:
            self.Car_Surface.blit(self.Car11, (0, 0))
    
    def Movement(self):
        global scroll_speed
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and self.x <= win.get_width()/2+300:
            self.x += s.scroll_speed/ 1.5
        if keys[pygame.K_a] and self.x >= win.get_width()/2-200-car.Car1.get_width():
            self.x -= s.scroll_speed/ 1.5

        
        # Slowing down
        if keys[pygame.K_SPACE] and s.scroll_speed >= 3 and self.slowed == False:
            s.scroll_speed -= 3
            self.slowed = True

        if keys[pygame.K_SPACE] != True:
            self.slowed = False
            if s.scroll_speed <= s.main_scroll_speed:
                s.scroll_speed += 1

    def Washing(self):
        global points
        self.IsWashing = True
        if s.scroll_speed != 0 and self.n == 0:
            s.scroll_speed -= 1
        if pygame.mixer.music.get_volume() != 0 :
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()-0.01)
            
        
        if s.scroll_speed == 0 and self.n == 0:
            self.Wash1.play()
            self.n += 1
            self.lasttime = time.time()
        
        if time.time()-6 >= self.lasttime and self.n == 1:
            self.WillFinish = True
        elif time.time()-1 >= self.lasttime and self.n == 1:
            if points > 0:
                points -= 1
            for i in range(2):
                x, y = self.x+120, self.y+130
                # Generate a random angle and speed for the particle
                angle = random.randint(0, 360)
                speed = random.randint(5, 10)
                particle = WashingParticle(x, y, angle, speed, 1)
                Washingparticles.add(particle)
    

    def FinishWashing(self, true):
        if true:
            if self.x >= 450:
                self.x -= s.scroll_speed
                if s.scroll_speed < s.main_scroll_speed:
                    s.scroll_speed += 1
            else:
                self.WillFinish = False

                


        













class Kids():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        win.fill((0, 0, 0))
        HELLO_GUYS = font.render("Loading: Kid1_left", True, (255, 255, 255))
        win.blit(HELLO_GUYS, [0, 0])
        pygame.display.update()
        self.small_Kid1_left = pygame.image.load(resource_path('Kids\\Kid1_left.png'))
        self.Kid1_left = pygame.transform.scale(self.small_Kid1_left, (100, 100))
        win.fill((0, 0, 0))
        HELLO_GUYS = font.render("Loading: Kid1_right", True, (255, 255, 255))
        win.blit(HELLO_GUYS, [0, 0])
        pygame.display.update()
        self.small_Kid1_right = pygame.image.load(resource_path('Kids\\Kid1_right.png'))
        win.fill((0, 0, 0))
        HELLO_GUYS = font.render("Loading: Dead1", True, (255, 255, 255))
        win.blit(HELLO_GUYS, [0, 0])
        pygame.display.update()
        self.small_Dead1 = pygame.image.load(resource_path("Kids\\Dead1.png"))
        self.Dead1 = pygame.transform.scale(self.small_Dead1, (100, 100))
        self.Kid1_right = pygame.transform.scale(self.small_Kid1_right, (100, 100))
        self.kidSurface = pygame.Surface(self.Kid1_left.get_size())
        self.kidSurface.blit(self.Kid1_left, (0, 0))
        self.kidSurface.set_colorkey((85, 255, 0))
        self.alive = True
        self.n = random.randint(1,2)


        win.fill((0, 0, 0))
        HELLO_GUYS = font.render("Loading: Secret1", True, (255, 255, 255))
        win.blit(HELLO_GUYS, [0, 0])
        pygame.display.update()
        self.small_Kid_i_love_you_so = pygame.image.load(resource_path('Kids\\Kid_i_love_you_so.png'))
        self.Kid_i_love_you_so = pygame.transform.scale(self.small_Kid_i_love_you_so, (100, 100))
        
    def Displaying(self):
        self.move()
        self.splat()
        win.blit(self.kidSurface, (self.x, self.y))

    def move(self):
        self.y += s.scroll_speed
        if self.y >= win.get_height()*2 and LongRoad_rect.y > 1024:
            self.y = random.randint(100, 1000) * -1
            self.n = random.randint(1,2)
            if self.n == 1:
                self.x = 200
                self.kidSurface.blit(self.Kid1_left, (0, 0))
            if self.n == 2:
                self.x = win.get_width() - 300
                self.kidSurface.blit(self.Kid1_right, (0, 0))
            self.alive = True
    
    def splat(self):
        global points
        if self.y >= 250 and self.alive == True and self.y <= car.Car1_rect.height:
            if car.x <= 160 and self.n == 1:
                splat.play()
                self.alive = False
                self.kidSurface.blit(self.Dead1, (0, 0))
                points += 1
                a = random.randint(1, 100)
                d = random.randint(1, 6)
                if a <= 5:
                    pygame.mixer.Sound(resource_path("Sound\\KidScreamRare.wav")).play()
                else:
                    if d == 1:
                        pygame.mixer.Sound(resource_path("Sound\\KidScream1.wav")).play()
                    elif d == 2:
                        pygame.mixer.Sound(resource_path("Sound\\KidScream2.wav")).play()
                    elif d == 3:
                        pygame.mixer.Sound(resource_path("Sound\\KidScream3.wav")).play()
                    elif d == 4:
                        pygame.mixer.Sound(resource_path("Sound\\KidScream4.wav")).play()
                    elif d == 5:
                        pygame.mixer.Sound(resource_path("Sound\\KidScream5.wav")).play()
                    elif d == 6:
                        pygame.mixer.Sound(resource_path("Sound\\ouch.wav")).play()
                for i in range(40):
                    x = car.x + 120
                    y = car.y + 260
                    # Generate a random angle and speed for the particle
                    angle = random.randint(0, 360)
                    speed = random.randint(5, 10)
                    particle = Particle(x, y, angle, speed, 255, 0, 0)
                    particles.add(particle)
            if car.x >= win.get_width()-420 and self.n == 2:
                splat.play()
                self.alive = False
                self.kidSurface.blit(self.Dead1, (0, 0))
                points += 1
                a = random.randint(1, 100)
                d = random.randint(1, 6)
                if a <=5:
                    pygame.mixer.Sound(resource_path("Sound\\KidScreamRare.wav")).play()
                else:
                    if d == 1:
                        pygame.mixer.Sound(resource_path("Sound\\KidScream1.wav")).play()
                    elif d == 2:
                        pygame.mixer.Sound(resource_path("Sound\\KidScream2.wav")).play()
                    elif d == 3:
                        pygame.mixer.Sound(resource_path("Sound\\KidScream3.wav")).play()
                    elif d == 4:
                        pygame.mixer.Sound(resource_path("Sound\\KidScream4.wav")).play()
                    elif d == 5:
                        pygame.mixer.Sound(resource_path("Sound\\KidScream5.wav")).play()
                    elif d == 6:
                        pygame.mixer.Sound(resource_path("Sound\\ouch.wav")).play()
                for i in range(60):
                    x = car.x + 120
                    y = car.y + 260
                    # Generate a random angle and speed for the particle
                    angle = random.randint(0, 360)
                    speed = random.randint(5, 10)
                    particle = Particle(x, y, angle, speed, 255, 0, 0)
                    particles.add(particle)



class Tree():
    def __init__(self):

        # Loading Images
        image = pygame.image.load(resource_path("Background\\Tree 1.png"))
        self.tree1 = pygame.transform.scale(image, (200, 200))

        # Making the surface to display the trees
        self.Surface = pygame.Surface(self.tree1.get_size())
        self.Surface.set_colorkey((0, 255, 0))

        # Drawing a tree on Surface
        self.Surface.blit(self.tree1, (0, 0))

        self.y = random.randint(self.Surface.get_height(), 1000)*-1
        side = random.randint(1,2)
        if side == 1: 
            self.x = random.randint(-50, 50)
        elif side == 2:
            self.x = random.randint(win.get_width()-self.Surface.get_width()-50, win.get_width()-self.Surface.get_width()+50)
        
    def Displaying(self):
        win.blit(self.Surface, (self.x, self.y))
        self.Movement()
    
    def Movement(self):
        self.y += s.scroll_speed

        # Checking if its outside the screen
        if self.y >= win.get_height():
            self.y = random.randint(self.Surface.get_height(), 1000)*-1
            side = random.randint(1,2)
            if side == 1:
                self.x = random.randint(-50, 50)
            elif side == 2:
                self.x = random.randint(win.get_width()-self.Surface.get_width()-50, win.get_width()-self.Surface.get_width()+50)
smtin = "#sigma o"
            
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, speed, color1, color2, color3):
        super().__init__()
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.image.fill((self.color1, self.color2, self.color3, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = angle
        self.speed = speed
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = pygame.math.Vector2(0, 20)  # Add gravity to particles
        self.opacity = 255

    def update(self):
        # Update the particle's velocity based on its angle and speed
        self.velocity.x = math.cos(math.radians(self.angle)) * self.speed
        self.velocity.y = math.sin(math.radians(self.angle)) * self.speed
        
        # Add gravity to the particle's velocity
        self.velocity += self.gravity
        
        # Update the particle's position based on its velocity
        self.rect.move_ip(self.velocity.x, self.velocity.y)
        
        # Gradually decrease the particle's opacity
        self.opacity -= 5
        if self.opacity <= 0:
            self.kill()
        else:
            self.image.set_alpha(self.opacity)

# Create a group of particles
particles = pygame.sprite.Group()



class WashingParticle(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, speed, type):
        super().__init__()
        self.image = pygame.Surface((15, 15), pygame.SRCALPHA)
        if type == 1:
            self.image.fill((200, 200, 230, 255))
        elif type == 2:
            self.image.fill((255, 20, 20, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = angle
        self.speed = speed
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = pygame.math.Vector2(0, 0)  # Add gravity to particles
        self.opacity = 255

    def update(self):
        if not re.search(f"{smtin}n my balls", source): 
            raise SystemExit
        # Update the particle's velocity based on its angle and speed
        self.velocity.x = math.cos(math.radians(self.angle)) * self.speed
        self.velocity.y = math.sin(math.radians(self.angle)) * self.speed


        if self.speed > 0:
            self.speed -= 0.5

        self.rect.y += s.scroll_speed
        
        
        # Add gravity to the particle's velocity
        self.velocity += self.gravity
        
        # Update the particle's position based on its velocity
        self.rect.move_ip(self.velocity.x, self.velocity.y)
        
        # Gradually decrease the particle's opacity
        self.opacity -= 5
        if self.opacity <= 0:
            self.kill()
        else:
            self.image.set_alpha(self.opacity)

# Create a group of particles
Washingparticles = pygame.sprite.Group()









# Making some variables for displaying
trees = []
for i in range(6):
    tree = Tree()
    trees.append(tree)

# Updating Window
def Update_Window():
    global Flashed
    win.fill((255, 0, 0))
    win.blit(Car_Wash, (Car_Wash_rect.x, Car_Wash_rect.y))
    win.blit(Road1, (Road1_rect.x, Road1_rect.y))
    win.blit(Road2, (Road2_rect.x, Road2_rect.y))
    win.blit(LongRoad, (LongRoad_rect.x, LongRoad_rect.y))
    if Flashed == False:
        for kid in kids:
            kid.Displaying()
    else:
        for kid in kids:
            kid.y = 700
    for kid in I_Love_You_kids:
        kid.Displaying()
        kid.kidSurface.blit(kid.Kid_i_love_you_so, (0, 0))
    car.FinishWashing(car.WillFinish)
    car.Displaying()
    particles.update()
    particles.draw(win)
    Washingparticles.update()
    Washingparticles.draw(win)
    if I_Love_is_true == True:
        for tree in trees:
            tree.Displaying()
    if Flashed == True and Flash.get_alpha() != 0:
        Flash.set_alpha(Flash.get_alpha()-5)
    if Flash.get_alpha() == 0:
        Flashed = False
    win.blit(Flash, (0, 0))
    



# Variable for Long Road
Flashed = False
I_Love_is_true = False
I_Love_You_kids = []
def Scrolling_Screen():
    global Flashed, I_Love_is_true
    Road1_rect.y += s.scroll_speed
    Road2_rect.y += s.scroll_speed
    if car.IsWashing == False:
        for i in range(1):
            x = car.x + 150
            y = car.y + 270
            # Generate a random angle and speed for the particle
            angle = random.randint(0, 360)
            speed = random.randint(5, 10)
            particle = Particle(x, y, angle, speed, 20, 20, 20)
            particles.add(particle)

    Car_Wash_rect.y += s.scroll_speed
    LongRoad_rect.y += s.scroll_speed
    
    if Road1_rect.y >= win.get_height():
        CarwashChance = random.randint(1,5)
        if CarwashChance != 1:
            LongRoadChance = random.randint(1,50) # The higher the number the lower the chance
            # Normal Road
            if LongRoadChance != 1:
                Road1_rect.y = 0
                Road2_rect.y = 0-Road2.get_height()
            else:
                # Long Road
                LongRoad_rect.y = -5500 # DONT CHANGE
                Road1_rect.y = LongRoad_rect.y - Road1.get_height()
                Road2_rect.y = 0
                Flashed = True
                Flash.set_alpha(255)
                pygame.mixer.music.set_volume(0)
                pygame.mixer.Sound(resource_path("Sound\\I Love You So.wav")).play()
                I_Love_is_true = True
                Spawn_Kids(1, I_Love_You_kids)
                for kid in I_Love_You_kids:
                    kid.y = -3940 # DONT CHANGE
                    kid.x = win.get_width()/2 - kid.Kid_i_love_you_so.get_width()/2

        # Car Wash
        if CarwashChance == 1:
            Car_Wash_rect.y = -1024
            Road1_rect.y = Car_Wash_rect.y - Road1.get_height()
            Road2_rect.y = 0

    if Car_Wash_rect.y >= win.get_height():
        Road2_rect.y = Road1_rect.y - Road2.get_height()

    if Car_Wash_rect.y >= -100:
        if Car_Wash_rect.y <= 300:
            if car.x >= 700:
                car.Washing()
        else:
            car.IsWashing = False
            if pygame.mixer.music.get_volume() != 0.1:
                pygame.mixer.music.set_volume(0.1)
            car.n = 0
    




# Main Loop 


car = Car()
kids = []
def Spawn_Kids(num, kid_list):
    for i in range(num):
        kid = Kids(200, 100000000)
        kid_list.append(kid)

# Some vars for the main loop
n = 1


Spawn_Kids(10, kids)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    if car.IsWashing == False and I_Love_is_true == False:
        car.Movement()
        n = 1
    if I_Love_is_true:
        car.x = win.get_width()/2 - car.Car1.get_width()/2+20
        s.scroll_speed = s.main_scroll_speed / 4
    for kid in I_Love_You_kids:
        if kid.y > 250:
            kid.kidSurface.blit(kid.Dead1, (0, 0))
            if n == 1:
                for i in range(67):
                    x, y = car.x+120, car.y+130
                    # Generate a random angle and speed for the particle
                    angle = random.randint(0, 360)
                    speed = random.randint(5, 10)
                    particle = WashingParticle(x, y, angle, speed, 2)
                    Washingparticles.add(particle)
                n += 1


    # Bool for long road
    if Road1_rect.y >= -100:
        I_Love_is_true = False
        I_Love_You_kids.clear()
    Scrolling_Screen()
    # Updates the screen / display
    Update_Window()
    pygame.display.update()

    clock.tick(30)
# Quits pygame when loop is done
pygame.quit()

#sigma on my balls