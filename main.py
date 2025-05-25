import pygame, sys, random, math

pygame.init()
screenx = 960
screeny = 720
screen = pygame.display.set_mode((screenx, screeny))
clock = pygame.time.Clock()
score = 0
score_text = pygame.font.SysFont("Arial", 24)
time_text = pygame.font.SysFont("Arial", 24)
# Load assets
bg_img = pygame.image.load("assets/spr_background.png")
apple_img = pygame.image.load("assets/spr_apple.png")
cat_img = pygame.image.load("assets/spr_cat.png")
time_ = 60 * 60 # 60 frame = 1 second
# Apple position
apple_x = random.randint(240, 720)
apple_y = 0
apple_speed = 5

cat_x = 0
cat_y = 480
cat_speed = 0
can_collide = True
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cat_speed = -4
            elif event.key == pygame.K_RIGHT:
                cat_speed = 4
        if event.type == pygame.KEYUP:
            cat_speed = 0
    if not game_over:
        cat_x += cat_speed
        # Update apple position
        apple_y += apple_speed
        distance = math.sqrt((cat_x - apple_x) ** 2 + (cat_y - apple_y) ** 2)
        time_ -= 1
        if apple_y > screeny:
            apple_y = 0
            apple_x = random.randint(240, 720)
        if can_collide and distance < 60:
            score += 1
            apple_y = 0
            apple_x = random.randint(240, 720)
            can_collide = False
        if apple_y > 200:
            can_collide = True
        if time_ == 0:
            game_over = True
        # Draw everything
        screen.blit(bg_img, (0, 0))
        if not game_over:
            screen.blit(cat_img, (cat_x, cat_y))
        screen.blit(apple_img, (apple_x, apple_y))
        score_render = score_text.render(f"Score: {score}", True, (255, 255, 255))
        time_render = time_text.render(f"Time: {time_/60:.0f}", True, (255, 255, 255))
        screen.blit(score_render, (0, 0))
        screen.blit(time_render, (0, 20))
        pygame.display.update()
        clock.tick(60)  # 60 FPS
