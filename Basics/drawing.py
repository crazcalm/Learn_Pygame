import pygame, math

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (250, 250, 250)
GREEN = (  0, 250,   0)
RED   = (250,   0,   0)
BLUE  = (  0,   0, 250)

# Set the width and height of the screen
SIZE = (700, 500)
screen = pygame.display.set_mode(SIZE)

# Setting the window title
pygame.display.set_caption("Window Title")

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ------------ Main Program Loop --------------
while done == False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # user did something
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            print("User pressed a key")
        if event.type == pygame.KEYUP:
            print("User let go of a key")
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")

    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT


    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT


    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT


    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)


    # Draw on the screen a green line from (0,0) to (100, 100)
    # that is 5 pixels wide
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

    # Draw a rectangle
    pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)

    # Draw an ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, BLACK, [125, 125, 250, 100], 2)

    # Draw text to the screen
    # Select the font to use. Default font, 25 pt size
    font = pygame.font.Font(None, 25)

    # Render the text. "True" means anti-aliased text.
    # Black is the color
    text = font.render("My Text",True, BLACK )

    # Put the image of the text on the screen at 250x250
    screen.blit(text, [250, 250])


    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT


    # Go ahead and update the screen with what we've drawn
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(20)

# Close the window and quit
# If you forget this line, the program will "hang"
# on exit if running from IDLE
pygame.quit()
