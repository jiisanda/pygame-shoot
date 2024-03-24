import pygame                               # imports package pygame

pygame.init()                               # initializing the package

win = pygame.display.set_mode((500, 480))   # setting the window width as (length, breath)

# screenWidth = 500
pygame.display.set_caption("Shoot The Goblin")    # Setting the name/caption to the game

# This goes outside the while loop, near the top of the program
# remember to keep the images and the game file in the same directory

walkRight = [
    pygame.image.load('assets/player/R1.png'), pygame.image.load('assets/player/R2.png'),
    pygame.image.load('assets/player/R3.png'), pygame.image.load('assets/player/R4.png'),
    pygame.image.load('assets/player/R5.png'), pygame.image.load('assets/player/R6.png'),
    pygame.image.load('assets/player/R7.png'), pygame.image.load('assets/player/R8.png'),
    pygame.image.load('assets/player/R9.png')
]
walkLeft = [
    pygame.image.load('assets/player/L1.png'), pygame.image.load('assets/player/L2.png'),
    pygame.image.load('assets/player/L3.png'), pygame.image.load('assets/player/L4.png'),
    pygame.image.load('assets/player/L5.png'), pygame.image.load('assets/player/L6.png'),
    pygame.image.load('assets/player/L7.png'), pygame.image.load('assets/player/L8.png'),
    pygame.image.load('assets/player/L9.png')
]

bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

# bulletSound = pygame.mixer.Sound('Gunshot.mp3')
# music = pygame.mixer.music.load("music.mp3")
# pygame.mixer.music.play(-1)

score = 0


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)   # 4 things inside a tuple is rectangle (x, y, width, height)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
           if self.right:
               win.blit(walkRight[0], (self.x, self.y))
           else:
               win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 100
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('conicsana', 100)
        text = font1.render('-5', 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()


class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Enemy(object):
    walkRight = [
        pygame.image.load('assets/goblin/L1E.png'), pygame.image.load('assets/goblin/L2E.png'),
        pygame.image.load('assets/goblin/L3E.png'), pygame.image.load('assets/goblin/L4E.png'),
        pygame.image.load('assets/goblin/L5E.png'), pygame.image.load('assets/goblin/L6E.png'),
        pygame.image.load('assets/goblin/L7E.png'), pygame.image.load('assets/goblin/L8E.png'),
        pygame.image.load('assets/goblin/L9E.png'), pygame.image.load('assets/goblin/L10E.png'),
        pygame.image.load('assets/goblin/L11E.png')
    ]
    walkLeft = [
        pygame.image.load('assets/goblin/L1E.png'), pygame.image.load('assets/goblin/L2E.png'),
        pygame.image.load('assets/goblin/L3E.png'), pygame.image.load('assets/goblin/L4E.png'),
        pygame.image.load('assets/goblin/L5E.png'), pygame.image.load('assets/goblin/L6E.png'),
        pygame.image.load('assets/goblin/L7E.png'), pygame.image.load('assets/goblin/L8E.png'),
        pygame.image.load('assets/goblin/L9E.png'), pygame.image.load('assets/goblin/L10E.png'),
        pygame.image.load('assets/goblin/L11E.png')
    ]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self. walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self. walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10 ))
            pygame.draw.rect(win, (0, 120, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print("HIT!!!")


def redrawGameWindow():                     # any change in drawing the loop we would be dong it here
    win.blit(bg, (0, 0))
    text = font.render("Score: " + str(score), 1, (0, 0, 0))
    win.blit(text, (350, 10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()  # updates or refreshes the page


# main loop
font = pygame.font.SysFont('comicsans', 30, True)
man = Player(300, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, 450)
ShootLoop = 0
bullets = []
run = True                                  # initializing the run as true for moving the rectangle
while run:                                  # main loop
    clock.tick(27)

    if goblin.visible == True:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score -= 5

    if ShootLoop > 0:
        ShootLoop += 1
    if ShootLoop > 3:
        ShootLoop = 0

    for event in pygame.event.get():        # event: - anything that happens from user here movement of rectangle
        if event.type == pygame.QUIT:       # if the user clicks [x] on the top right corner then
            run = False                     # the run gets False i.e., stops...

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
                
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()      # if the user presses key and the key which user press is known by this fun

    if keys[pygame.K_SPACE] and ShootLoop == 0:
        # bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

        ShootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:     # if it presses Left Key(<--)(here and the x > vel sets the boundaries,then)
        man.x -= man.vel                            # moves left
        man.left = True
        man.right = False
        man.standing = False

    elif (keys[pygame.K_RIGHT]) and (man.x < 500 - man.width - man.vel):
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True             # from this we would know he is looking left or right
        man.walkCount = 0

    if not man.isJump:                        # Now if we jump and we will go up and come down here if not isJump makes True
        if keys[pygame.K_UP]:    # For Jumping
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0

    else:                                   # if isJump is False then
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    redrawGameWindow()

pygame.quit()                               # quits the game
