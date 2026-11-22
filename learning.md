# Thanks chatgpt, sammy altman shall get my ram

# Lets learn something.

*should I put this in gitignore?* no, let the world witness the suffering.

## Main stuff

- `pygame.init()` -> Initializes pygame, because apparently we have to turn it on first
- `pygame.display.set_mode((x, y))` -> Creates a window with x/y res, screen = ... lets us draw on it
- `pygame.time.Clock()` -> Creates a clock, tick(60) limits fps so the CPU doesn't apply for retirement
- `pygame.quit()` -> Shuts down pygame, finally some peace

## Window props

- `pygame.display.set_caption("")` -> Sets window title, make it sound like an actual game
- `pygame.display.set_icon(icon)` -> Sets window icon, icon = pygame.image.load("icon.png"), branding for our future disaster
- `screen.fill((r, g, b))` -> Fills screen with an RGB color, randomize it every frame if you hate your eyes
- `pygame.display.flip()` -> Updates the window with what we drew, assuming we drew anything

## Game loop

- `running = True` -> Keeps the game running, unfortunately
- `while running:` -> Repeats while running is True, welcome to eternity
- `pygame.event.get()` -> Gets events like key presses, clicks, closing, basically the player attempting to communicate
- `for event in pygame.event.get():` -> Goes through each event, one disappointment at a time
- `event.type` -> Type of event, groundbreaking stuff
- `pygame.QUIT` -> Window close event, the player's first sensible decision
- `running = False` -> Stops the loop, freedom at last
- `clock.tick(60)` -> Limits fps to 60, because 9000 fps on a rectangle is unnecessary

## Text

- `font = pygame.font.Font(None, 36)` -> Creates a font with size 36, default because we're financially responsible
- `pygame.font.Font("font.ttf", 36)` -> Loads a custom font, suddenly we're graphic designers
- `text = font.render("Hello", True, (255, 255, 255))` -> Creates white text, truly revolutionary
- `screen.blit(text, (x, y))` -> Draws text at x/y, congratulations we invented reading

## Shapes

- `pygame.draw.rect(screen, (255, 0, 0), (x, y, w, h))` -> Draws a red rectangle, AAA graphics right here
- `pygame.draw.circle(screen, (255, 0, 0), (x, y), 30)` -> Draws a red circle, technological advancement
- `pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 3)` -> Draws a line with thickness 3, Pixar is trembling

## Images / PNGs

- `img = pygame.image.load("image.png").convert_alpha()` -> Loads a PNG with transparency, assuming the file actually exists
- `screen.blit(img, (x, y))` -> Draws the image at x/y, finally something that isn't a rectangle
- `pygame.transform.scale(img, (100, 100))` -> Resizes image to 100x100, image quality sold separately
- `img.get_rect()` -> Gets image rectangle, useful for positioning and collisions, because apparently images need geometry

## Moving images

- `x, y = 100, 100` -> Starting position, our character has officially spawned
- `x += 5` -> Moves right by 5 pixels, incredible mobility
- `x -= 5` -> Moves left, character development
- `y += 5` -> Moves down, gravity sold separately
- `y -= 5` -> Moves up, NASA wants our technology
- `screen.blit(img, (x, y))` -> Draws image at updated position every frame, congratulations we invented animation

## Keyboard / mouse input

- `keys = pygame.key.get_pressed()` -> Gets currently held keys, surveillance but make it gaming
- `if keys[pygame.K_w]:` -> Checks if W is held, the player has discovered movement
- `if keys[pygame.K_SPACE]:` -> Checks if space is held, probably about to jump into something stupid
- `event.type == pygame.KEYDOWN` -> Checks for a key press event, someone touched the keyboard
- `event.key == pygame.K_RETURN` -> Checks if Enter was pressed inside a KEYDOWN event, commitment issues resolved
- `pygame.mouse.get_pos()` -> Gets mouse x/y, tracking the player's questionable decisions
- `pygame.mouse.get_pressed()` -> Gets currently held mouse buttons, click responsibly
- `event.type == pygame.MOUSEBUTTONDOWN` -> Checks for a mouse click, the user has chosen violence against the UI

## Collisions

- `rect = img.get_rect(topleft=(x, y))` -> Creates a rectangle around an image, invisible cardboard box technology
- `rect.colliderect(other_rect)` -> Checks if two rectangles overlap, personal space has been violated
- `rect.collidepoint(mouse_pos)` -> Checks if a point is inside the rectangle, useful for buttons that might actually work

## Things to remember

- Load images and fonts before the game loop, unless you enjoy unnecessary suffering
- Draw everything inside the game loop, not in your imagination
- `screen.fill()` should usually come before drawing, unless you want accidental modern art
- `pygame.display.flip()` goes after drawing, revolutionary concept
- Update x/y to move stuff, then redraw it, teleportation wasn't in the budget
- Use `clock.tick(60)` instead of `time.sleep()` for fps, this is a game not a hibernating bear
- Pygame CE still uses `import pygame`, because naming conventions are apparently optional
- Don't forget to save your files, Git cannot resurrect code you never committed
- If something doesn't work, check indentation before blaming the entire Python ecosystem