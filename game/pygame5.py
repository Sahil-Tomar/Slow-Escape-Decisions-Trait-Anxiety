import pygame
import random
import pandas as pd
import time
# Initialize pygame
pygame.init()

# Set window size
width=800
height=600
screen = pygame.display.set_mode((width, height))

# Function to display text on the screen
def display_text(text, size, position, color=(255, 255, 255)):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)

# Intro page function
def intro_page():
    background = pygame.image.load('bg2-final.jpg')

    intro_running = True
    while intro_running:
        screen.blit(background, (0, 0))
        display_text("Welcome to the Car Game!", 70, (400, 200))
        display_text("Press Enter to Start", 50, (400, 300))
        display_text("Press Esc to Quit", 40, (400, 350))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro_running = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

# Instruction page function
def instruction_page():
    background = pygame.image.load('instbg-final.jpg')

    instruction_running = True
    while instruction_running:
        screen.blit(background, (0, 0))
        display_text("Instructions", 70, (400, 100))
        display_text("Use 'g' to start the game.", 40, (400, 250))
        display_text("Use 'f' to avoid the crash.", 40, (400, 300))
        display_text("Press Enter to Play", 50, (400, 400))
        display_text("Press Esc to Quit", 40, (400, 450))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instruction_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    instruction_running = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                    
def gameover_page():
    background = pygame.image.load('game-over-final.jpg')

    intro_running = True
    start_time = time.time()  # Record intro start time

    while intro_running:

        # Draw background on each frame
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro_running = False  # Exit loop on QUIT event
            # if event.key == pygame.K_ESCAPE:
            #     pygame.quit()
            #     quit()
        # Update the display (needed for each frame)
        pygame.display.flip()

        # Check elapsed time and exit after 5 seconds
        if time.time() - start_time >= 5:
            intro_running = False
            
# Trail page function
# Trail page function
def trail_page():
    background = pygame.image.load('back (1).jpg')
    font = pygame.font.Font(None, 36)
    for i in range(5):
        acceleration_boosted = False  # Initialize acceleration_boosted
        playerX = 720
        playerY = 450
        enemyX = 20
        enemyY = 450
        enemy_change = 0
        acceleration_probability = 0.0001
        gpressed=False
        beforeg=True

        def simulate_speed():
            nonlocal acceleration_boosted
            nonlocal enemyX
            nonlocal enemy_change

            enemyX += enemy_change
            
            if not acceleration_boosted and random.random() < acceleration_probability:
                acceleration_boost = random.uniform(0.06, 0.07)
                enemy_change = acceleration_boost
                enemyX += enemy_change
                acceleration_boosted = True
                
        running = True
        while running:
            # Screen setup
            screen.fill((0,125,0))
            screen.blit(background, (0,0))

            # Display score text
            score_text = font.render("Count: " + str(i), True, (0, 0, 0))  # Render score text
            screen.blit(score_text, (680, 10))  # Blit score text onto the screen
            text= font.render("Trial",True,(0,0,0))
            screen.blit(text, (400, 10))
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g and beforeg:
                        enemy_change = 0.01
                        gpressed=True
                        beforeg=False
                    if event.key == pygame.K_f and gpressed:
                        speed = enemy_change
                        enemy_change = 0
                        fid = playerX - (enemyX+64)
                        money = 1000 / fid
                        running = False
                        
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

            # Enemy movement
            enemyX += enemy_change
            
            if enemy_change:
                simulate_speed()
                
            speed = enemy_change

            # Collision detection
            if enemyX >= playerX - 50:
                enemy_change = 0
                fid = 0
                money = 0
                crash_count = 1
                print("Crash")
                running = False
                gameover_page()

            # Draw player and enemy
            player(playerX, playerY)
            enemy(enemyX, enemyY)
            pygame.display.update()


# Main game function
def main_game():
    try:
        df = pd.read_csv('results2.csv', dtype={'boost_flag': bool})
    except FileNotFoundError:
        df = pd.DataFrame(columns=['economic_score', 'fail_count', 'flee_distance', 'speed', 'boost_flag'])
    
    background = pygame.image.load('back (1).jpg')
    font = pygame.font.Font(None, 36)
    
    result_dfs = []
    for i in range(5):
        acceleration_boosted = False  # Initialize acceleration_boosted
        playerX = 720
        playerY = 450
        enemyX = 20
        enemyY = 450
        enemy_change = 0
        acceleration_probability = 0.0002
        money = 0
        fid = 0        
        crash_count = 0    
        speed=0.01
        initial_distance = playerX - enemyX
        gpressed=False
        beforeg=True

        def simulate_speed():
            nonlocal acceleration_boosted
            nonlocal enemyX
            nonlocal enemy_change
            nonlocal speed

            enemyX += enemy_change
            
            if not acceleration_boosted and random.random() < acceleration_probability:
                acceleration_boost = random.uniform(0.06, 0.5)
                enemy_change = acceleration_boost
                speed=enemy_change
                enemyX += enemy_change
                acceleration_boosted = True
                
        running = True
        while running:
            # Screen setup
            screen.fill((0,125,0))
            screen.blit(background, (0,0))

            # Display score text
            score_text = font.render("Count: " + str(i), True, (0, 0, 0))  # Render score text
            screen.blit(score_text, (680, 10))  # Blit score text onto the screen
            text= font.render("Main Game",True,(0,0,0))
            screen.blit(text, (400, 10))

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g and beforeg:
                        enemy_change = 0.01
                        speed=enemy_change
                        gpressed=True
                        beforeg=False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()    
                    if event.key == pygame.K_f and gpressed:
                        speed = enemy_change
                        enemy_change = 0
                        fid = playerX - (enemyX+64)
                        money = 10000 / fid
                        running = False

            # Enemy movement
            enemyX += enemy_change
            
            if enemy_change:
                simulate_speed()
                speed = enemy_change
            

            # Collision detection
            if enemyX >= playerX - 50:
                enemy_change = 0
                fid = 0
                money = 0
                crash_count += 1
                print("Crash")
                running = False
                gameover_page()

            # Draw player and enemy
            player(playerX, playerY)
            enemy(enemyX, enemyY)
            pygame.display.update()
            
        result_dict = {
        'economic_score': money,
        'fail_count': crash_count,
        'flee_distance': fid,
        'speed': speed,
        
        'boost_flag': acceleration_boosted
        }
        result_df = pd.DataFrame([result_dict])  # Create a DataFrame for this game
        result_dfs.append(result_df)  # Append the DataFrame to the list
    # Concatenate all DataFrames in the list
    df = pd.concat(result_dfs, ignore_index=True)

    # Save DataFrame to CSV file
    df.to_csv('results2.csv', index=False)
        

# Player and enemy functions
def player(x, y):
    player_img = pygame.image.load('car.png')
    screen.blit(player_img, (x, y))

def enemy(x, y):
    enemy_img = pygame.image.load('enemy-car.png')
    screen.blit(enemy_img, (x, y))

def main():
    intro_page()
    instruction_page()
    trail_page()
    instruction_page()
    main_game()
    

if __name__ == "__main__":
    main()