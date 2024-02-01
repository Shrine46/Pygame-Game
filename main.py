import pygame
import sys

# Initialize Pygame and give access to all the methods in the package
pygame.init()

# Set up the screen dimensions
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create clock to later control frame rate
clock = pygame.time.Clock()


#Classes
class Basket(pygame.sprite.Sprite):
    def __init__(self):
        super(Basket, self).__init__()
        self.files = ["basket.png"]
        self.image_size = (150,75)
        self.images = [pygame.image.load("basket.png").convert_alpha()]
        self.image_converted = pygame.transform.scale(self.images[0], self.image_size)
        self.image = self.image_converted
        self.rect = self.image.get_rect(center = (200, 550))
    def move(self, direction):
            self.rect.centerx += direction

class BabyBird(pygame.sprite.Sprite):
    def __init__(self):
        super(BabyBird, self).__init__()
        self.index = 0
        self.files = []
        self.images = pygame.image.load("").convert_alpha()
        self.image = self.images
        

#Class Calls
basket_group = pygame.sprite.Group()
basket = Basket()
basket_group.add(basket)



# Main game loop
count = 0
running = True
while running:

    # Fill the screen with a color (e.g., white)
    screen.fill(WHITE)


    #Draw Items
    basket_group.draw(screen)


    #Basket Movement
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




    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False


    # Update the display
    pygame.display.flip()

    # Set a frame rate to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
sys.exit()