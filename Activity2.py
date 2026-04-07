import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adding image and background image")

background_image = pygame.transform.scale(pygame.image.load("background_image.jpg").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

penguin_image = pygame.transform.scale(pygame.image.load("penguin_image.jpg").convert_alpha(), (200, 200))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))

text = pygame.font.Font(None, 36).render('Hello World', True, pygame.Color('black'))

text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background_image, (0, 0))
        screen.blit(penguin_image, penguin_rect)
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == "__main__":
    game_loop()
