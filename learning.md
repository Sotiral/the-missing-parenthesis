# Lets learn something.

*should I put this in gitignore?*

thanks chatgpt

## Main stuff

- pygame.init() -> Initializes pygame
- pygame.display.set_mode((x, y)) -> Creates a window with x/y res, screen = ... lets us draw on it
- pygame.time.Clock() -> Creates a clock, tick(60) limits fps
- pygame.quit() -> Shuts down pygame

## Window props

- pygame.display.set_caption("") -> Sets window title
- screen.fill((r, g, b)) -> Fills screen with an RGB color
- pygame.display.flip() -> Updates the window with what we drew

## Game loop

- running = True -> Keeps the game running
- while running: -> Repeats while running is True
- pygame.event.get() -> Gets events like key presses, clicks, closing
- for event in pygame.event.get(): -> Goes through each event
- event.type -> Type of event
- pygame.QUIT -> Window close event
- running = False -> Stops the loop

