import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the window dimensions and create the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shahanawas Ali Shuvo")

# Define colors
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Function to draw an obtuse triangle
def draw_obtuse_triangle():
    # Vertices of the obtuse triangle
    points = [(200, 100), (400, 300), (600, 150)]
    pygame.draw.polygon(screen, CYAN, points)

# Function to draw a rectangle using 6 vertices (2 triangles)
def draw_green_rectangle():
    # Define 6 vertices for two triangles forming a rectangle
    vertices = [(200, 400), (400, 400), (400, 500),
                (400, 500), (200, 500), (200, 400)]
    
    # Drawing two triangles that form the rectangle
    pygame.draw.polygon(screen, GREEN, vertices[:3])
    pygame.draw.polygon(screen, GREEN, vertices[3:])

# Main loop
running = True
while running:
    screen.fill(ORANGE)  # Set the background color to orange

    draw_obtuse_triangle()  # Draw the obtuse triangle
    draw_green_rectangle()  # Draw the green rectangle

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  # Close the window when "S" is pressed
                running = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
