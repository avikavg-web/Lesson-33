import pygame
import sys

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My first game screen")

GREY = (58, 58, 58)
image_path = "image.png"

try:
    original_image = pygame.image.load(image_path)
    my_image = pygame.transform.scale(original_image, (300, 300))
    image_rect = my_image.get_rect(center=(screen_width // 2, screen_height // 2))
except pygame.error:
    pygame.quit()
    sys.exit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GREY)
    screen.blit(my_image, image_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()