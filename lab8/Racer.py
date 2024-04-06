import pygame
from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# Set up the window
width = 500
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Car Game')

# Define colors
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

# Road and marker sizes
road_width = 300
marker_width = 10
marker_height = 50

# Lane coordinates
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

# Road and edge markers
road = (100, 0, road_width, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

# For animating movement of the lane markers
lane_marker_move_y = 0

# Player's starting coordinates
player_x = 250
player_y = 400

# Frame settings
clock = pygame.time.Clock()
fps = 120

# Game settings
gameover = False
speed = 2
score = 0
coins_collected = 0

# Load sound effects
coin_image = pygame.image.load('coin.png')
coin_image = pygame.transform.scale(coin_image, (20, 20))
#collision_sound = pygame.mixer.Sound('collision.wav')


# Define Vehicle class
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (45, 90))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]


# Define PlayerVehicle class as a subclass of Vehicle
class PlayerVehicle(Vehicle):
    def __init__(self, x, y):
        image = pygame.image.load('car.png')
        super().__init__(image, x, y)


# Define Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]


# Sprite groups
player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

# Create the player's car
player = PlayerVehicle(player_x, player_y)
player_group.add(player)

# Load the vehicle images
vehicle_images = [pygame.image.load('car2.png'),
                  pygame.image.load('car3.png'),
                  pygame.image.load('car4.png')]

# Load the crash image
crash = pygame.image.load('crash.png')
crash_rect = crash.get_rect()

# Game loop
running = True
while running:
    clock.tick(fps)

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100

    # Draw road and markers
    screen.fill(green)
    pygame.draw.rect(screen, gray, road)
    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)

    # Draw lane markers
    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0
    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))

    # Draw the player's car
    player_group.draw(screen)

    # Add a vehicle
    if len(vehicle_group) < 2:
        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False
        if add_vehicle:
            lane = random.choice(lanes)
            image = random.choice(vehicle_images)
            vehicle = Vehicle(image, lane, height / -2)
            vehicle_group.add(vehicle)

    # Make the vehicles move
    for vehicle in vehicle_group:
        vehicle.rect.y += speed
        if vehicle.rect.top >= height:
            vehicle.kill()
            score += 1
            if score > 0 and score % 5 == 0:
                speed += 1

    # Draw the vehicles
    vehicle_group.draw(screen)

    # Add coins
    if random.randint(0, 1000) < 10:  # Adjust the probability as needed
        coin_lane = random.choice(lanes)
        coin = Coin(coin_lane, height / -2)
        coin_group.add(coin)

    # Make the coins move
    for coin in coin_group:
        coin.rect.y += speed
        if coin.rect.top >= height:
            coin.kill()
        elif pygame.sprite.collide_rect(player, coin):
            coin.kill()
            coins_collected += 1
            #coin_image.play()

    # Draw the coins
    coin_group.draw(screen)

    # Display the score and coins collected
    font = pygame.font.Font(None, 30)
    score_text = font.render('Score: ' + str(score), True, white)
    coin_text = font.render('Coins: ' + str(coins_collected), True, white)
    screen.blit(score_text, (20, 20))
    screen.blit(coin_text, (width - 120, 20))

    # Check for collisions with vehicles
    if pygame.sprite.spritecollide(player, vehicle_group, False):
        #collision_sound.play()
        gameover = True

    # Display game over screen
    if gameover:
        screen.blit(crash, crash_rect)
        pygame.draw.rect(screen, red, (0, 50, width, 100))
        font = pygame.font.Font(None, 30)
        text = font.render('Game over. Play again? (Press Y or N)', True, white)
        text_rect = text.get_rect(center=(width / 2, 100))
        screen.blit(text, text_rect)

    pygame.display.update()

    # Wait for user input to play again or exit
    while gameover:
        for event in pygame.event.get():
            if event.type == QUIT:
                gameover = False
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_y:
                    gameover = False
                    speed = 2
                    score = 0
                    coins_collected = 0
                    vehicle_group.empty()
                    coin_group.empty()
                    player.rect.center = [player_x, player_y]
                elif event.key == K_n:
                    gameover = False
                    running = False

pygame.quit()
