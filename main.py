import pygame
import sys
import random
import math

# Initialize Pygame and give access to all the methods in the package
pygame.init()

# Set up the screen dimensions
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors & Fonts
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)

# Create clock to later control frame rate
clock = pygame.time.Clock()

#Functions
def game_over():
    text = font.render("You Lose", True, (255, 255, 255))
    screen.blit(text, (335, 300))
    count +=1
    if count == 300:
        running = False

#Classes
class Basket(pygame.sprite.Sprite):
    def __init__(self):
        super(Basket, self).__init__()
        self.files = ["basket.png"]
        self.image_size = (100,50)
        self.images = pygame.image.load("basket.png").convert_alpha()
        self.image = pygame.transform.scale(self.images, self.image_size)
        self.rect = self.image.get_rect(center = (200, 550))
    def move(self, direction):
            self.rect.centerx += direction


class Fruit(pygame.sprite.Sprite):
    def __init__(self, x):
        super(Fruit, self).__init__()
        self.image_size = (50, 50)
        self.files = ['apple.png', 'banana.png', 'grape.png', 'orange.png', 'pear.png']
        self.image = pygame.image.load(self.files[x]).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.image_size)
        self.rect = self.image.get_rect(center=(random.randint(20, 380), random.randint(75, 200)))
        
        
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super(Rock, self).__init__()
        self.index = 0
        self.image_size = (15, 20)
        self.files = ['meteor1.png', 'meteor2.png', 'meteor3.png']
        self.images = [pygame.image.load(filename).convert_alpha() for filename in self.files]
        self.image = pygame.transform.scale(self.images[self.index], self.image_size)
        self.rect = self.image.get_rect(center=(random.randint(20, 380), random.randint(75, 200)))
        

#Class Calls
basket_group = pygame.sprite.Group()
basket = Basket()
basket_group.add(basket)

fruit_group = pygame.sprite.Group()
for i in range(5):
    num = random.randint(0, 4)
    fruit = Fruit(num)
    fruit_group.add(fruit)

rock_group = pygame.sprite.Group()
for i in range(1):
    rock = Rock()
    rock_group.add(rock)




# Main game loop
lives = 3
score = 0
count = 0
timeout_count = 0
speed = 0
animation = 0
alive = True
running = True
while running:
    
    screen.fill(BLACK)
    score_text = font.render((f"Score {score}"), True, (255, 255, 255))
    lives_text = font.render((f"Lives {lives}"), True, (255, 255, 255))
    boost_text = font.render((f"Boost {count//10}/30"), True, (255, 255, 255))
    screen.blit(score_text, (0, 0))
    screen.blit(lives_text, (0, 25))
    screen.blit(boost_text, (0, 50))
    
    # Draw Items
    basket_group.draw(screen)
    fruit_group.draw(screen)
    rock_group.draw(screen)
    
    # Alive Handling
    if alive == False:
        text = font.render("You Lose", True, (255, 255, 255))
        screen.blit(text, (150, 300))
        timeout_count +=1
        if timeout_count == 300:
            running = False

    # Basket Movement
    if alive:
        dist = 1
        keys = pygame.key.get_pressed() 
        if count < 300: count+=1
        if keys[pygame.K_SPACE]:
            if count - 5 <= 0:
                if count - 120 > -125:  
                    count -= 120
            else:
                count -= 5
                dist = 5
        if keys[pygame.K_LEFT] and basket.rect.left>0:
            basket.move(dist*(-1))
        if keys[pygame.K_RIGHT] and basket.rect.right<400:
            basket.move(dist)
    
    # Fruit Movement & Collision Detect
    for fruit in fruit_group:
        if random.randint(0,100) >= 1:
            fruit.rect.centery += .5 + speed
        collisions = pygame.sprite.spritecollide(basket, fruit_group, True)
        if collisions:
            score += len(collisions)
            print("Score:", score)
            if score%10 == 0:
                speed+=.1
                rock = Rock()
                rock_group.add(rock)
            num = random.randint(0, 4)
            fruit = Fruit(num)
            fruit_group.add(fruit)
        if fruit.rect.bottom >= 600:
            lives -= 1
            fruit.kill()
            num = random.randint(0, 4)
            fruit = Fruit(num)
            fruit_group.add(fruit)
        if lives <= 0:
            alive = False
                
    # All Rock Handling           
    for rock in rock_group:
        animation += 1
        if animation % 15 == 0:
            rock.index = (rock.index + 1) % 3
            rock.image = rock.images[rock.index]
        rock.rect.centery += 2 + (speed * 5)
        collisions = pygame.sprite.spritecollide(basket, rock_group, True)
        if collisions:
            alive = False
        
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

    # Set a frame rate to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
sys.exit()