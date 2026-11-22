# Thanks chatgpt, sammy altman shall get my ram

# Lets learn something.

**should I put this in gitignore?** no, let the world witness the suffering.

## Main stuff

- `import pygame` -> Imports Pygame CE, because apparently we need a graphics library to draw rectangles
- `pygame.init()` -> Initializes pygame, because apparently we have to turn it on first
- `screen = pygame.display.set_mode((x, y))` -> Creates a window with x/y resolution, screen lets us draw on it
- `clock = pygame.time.Clock()` -> Creates a clock, because the CPU deserves basic human rights
- `pygame.quit()` -> Shuts down pygame, finally some peace
- `raise SystemExit` -> Exits the program, because pygame.quit() alone doesn't end your Python script

## Window props

- `pygame.display.set_caption("The Missing Parenthesis")` -> Sets window title, make it sound like an actual game
- `icon = pygame.image.load("icon.png")` -> Loads the window icon, branding for our future disaster
- `pygame.display.set_icon(icon)` -> Sets window icon, operating system decides how big it appears because freedom is apparently optional
- `screen.fill((r, g, b))` -> Fills screen with an RGB color, randomize it every frame if you hate your eyes
- `pygame.display.flip()` -> Updates the entire window with what we drew, assuming we drew anything
- `pygame.display.update()` -> Updates the display, can also update specific rectangles because efficiency exists
- `width, height = screen.get_size()` -> Gets current window dimensions, useful when the player resizes your masterpiece

## Window resolution / fullscreen

- `width, height = pygame.display.get_desktop_sizes()[0]` -> Gets the first monitor's desktop resolution, because guessing screen sizes is medieval
- `screen = pygame.display.set_mode((int(width / 1.5), int(height / 1.5)))` -> Creates a window smaller than the monitor, basic mathematics saving the day
- `screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)` -> Makes the window resizable, the player now controls your suffering
- `screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)` -> Opens exclusive fullscreen, goodbye desktop
- `pygame.display.toggle_fullscreen()` -> Toggles fullscreen on supported displays, no need to rebuild civilization
- `if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:` -> Detects F11, the universal button for making windows dramatic
- `pygame.display.toggle_fullscreen()` -> Put this inside the F11 condition, fullscreen without unnecessary chaos
- `if event.type == pygame.VIDEORESIZE:` -> Detects window resizing, because apparently players have preferences
- `width, height = screen.get_size()` -> Refresh dimensions after resizing, your old coordinates aren't psychic
- `pygame.SCALED` -> Display flag for scaling a fixed logical resolution, useful for pixel-art games
- `screen = pygame.display.set_mode((960, 540), pygame.SCALED | pygame.RESIZABLE)` -> Keeps logical drawing coordinates at 960x540 while scaling the window, pixels get promoted

## Game loop

- `running = True` -> Keeps the game running, unfortunately
- `while running:` -> Repeats while running is True, welcome to eternity
- `pygame.event.get()` -> Gets events like key presses, clicks, closing, basically the player attempting to communicate
- `for event in pygame.event.get():` -> Goes through each event, one disappointment at a time
- `event.type` -> Type of event, groundbreaking stuff
- `pygame.QUIT` -> Window close event, the player's first sensible decision
- `if event.type == pygame.QUIT:` -> Checks if the player wants to escape your creation
- `running = False` -> Stops the loop, freedom at last
- `clock.tick(60)` -> Limits fps to approximately 60, because 9000 fps on a rectangle is unnecessary
- `dt = clock.tick(60) / 1000` -> Gets seconds since the previous frame, movement no longer depends on owning a NASA computer
- `fps = clock.get_fps()` -> Gets measured FPS, useful for discovering your optimization crimes

## Text

- `font = pygame.font.Font(None, 36)` -> Creates a font with size 36, default because we're financially responsible
- `font = pygame.font.Font("font.ttf", 36)` -> Loads a custom font, suddenly we're graphic designers
- `text = font.render("Hello", True, (255, 255, 255))` -> Creates white text, truly revolutionary
- `screen.blit(text, (x, y))` -> Draws text at x/y, congratulations we invented reading
- `text_rect = text.get_rect(center=(width // 2, height // 2))` -> Centers text horizontally and vertically, because eyeballing coordinates is a war crime against UI
- `screen.blit(text, text_rect)` -> Draws the centered text, finally symmetry
- `text_rect = text.get_rect(midtop=(width // 2, 50))` -> Centers text horizontally at y=50, perfect for menu titles
- `text_rect = text.get_rect(center=(width // 2, 150))` -> Centers horizontally at a specific height, basic menu engineering
- `font.size("Hello")` -> Returns text width and height before rendering, because apparently letters occupy space
- `font.get_height()` -> Gets font height, useful for spacing text without praying
- `font.set_bold(True)` -> Makes font bold, your text has entered its gym era
- `font.set_italic(True)` -> Makes font italic, now it looks important
- `pygame.font.SysFont("arial", 32)` -> Uses an installed system font, assuming the operating system cooperates
- `font.render(f"Score: {score}", True, (255, 255, 255))` -> Creates dynamic text, numbers can now change without rewriting the universe

## Shapes

- `pygame.draw.rect(screen, (255, 0, 0), (x, y, w, h))` -> Draws a red rectangle, AAA graphics right here
- `pygame.draw.circle(screen, (255, 0, 0), (x, y), 30)` -> Draws a red circle, technological advancement
- `pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 3)` -> Draws a line with thickness 3, Pixar is trembling
- `pygame.draw.rect(screen, (255, 255, 255), (x, y, w, h), 2)` -> Draws only the rectangle outline, premium rectangle DLC
- `pygame.draw.rect(screen, (80, 80, 80), (x, y, w, h), border_radius=12)` -> Draws rounded rectangles, suddenly our UI costs money
- `pygame.draw.ellipse(screen, (255, 0, 0), (x, y, w, h))` -> Draws an ellipse, a circle that gave up
- `pygame.draw.polygon(screen, (255, 255, 255), [(0, 0), (50, 0), (25, 50)])` -> Draws a triangle, geometry has entered the chat

## Images / PNGs

- `img = pygame.image.load("image.png").convert_alpha()` -> Loads a PNG with transparency, assuming the file actually exists
- `screen.blit(img, (x, y))` -> Draws the image at x/y, finally something that isn't a rectangle
- `pygame.transform.scale(img, (100, 100))` -> Resizes image to 100x100, image quality sold separately
- `pygame.transform.smoothscale(img, (100, 100))` -> Resizes with smoother filtering, good for normal images but potentially cursed for pixel art
- `pygame.transform.scale_by(img, 2)` -> Doubles image dimensions, your sprite has been promoted
- `pygame.transform.rotate(img, 90)` -> Rotates image 90 degrees counterclockwise, physics sold separately
- `pygame.transform.flip(img, True, False)` -> Flips horizontally, character has discovered turning around
- `img.get_rect()` -> Gets image rectangle, useful for positioning and collisions, because apparently images need geometry
- `img.get_width()` -> Gets image width, no ruler required
- `img.get_height()` -> Gets image height, revolutionary
- `img.set_alpha(128)` -> Sets whole-surface transparency to roughly 50%, your image is becoming a ghost
- `screen.blit(img, img.get_rect(center=(width // 2, height // 2)))` -> Draws image centered, symmetry strikes again

## Moving images

- `x, y = 100, 100` -> Starting position, our character has officially spawned
- `x += 5` -> Moves right by 5 pixels, incredible mobility
- `x -= 5` -> Moves left, character development
- `y += 5` -> Moves down, gravity sold separately
- `y -= 5` -> Moves up, NASA wants our technology
- `screen.blit(img, (x, y))` -> Draws image at updated position every frame, congratulations we invented animation
- `speed = 250` -> Sets movement speed in pixels per second, finally consistent movement
- `x += speed * dt` -> Moves right independently of FPS, people with old laptops rejoice
- `x = max(0, min(x, width - img.get_width()))` -> Keeps image inside horizontal boundaries, no escaping the simulation
- `y = max(0, min(y, height - img.get_height()))` -> Keeps image inside vertical boundaries, freedom denied

## Keyboard / mouse input

- `keys = pygame.key.get_pressed()` -> Gets currently held keys, surveillance but make it gaming
- `if keys[pygame.K_w]:` -> Checks if W is held, the player has discovered movement
- `if keys[pygame.K_SPACE]:` -> Checks if space is held, probably about to jump into something stupid
- `event.type == pygame.KEYDOWN` -> Checks for a key press event, someone touched the keyboard
- `event.type == pygame.KEYUP` -> Checks for a key release, congratulations they stopped
- `event.key == pygame.K_RETURN` -> Checks if Enter was pressed inside a KEYDOWN event, commitment issues resolved
- `event.key == pygame.K_ESCAPE` -> Checks Escape, the player's emergency evacuation button
- `event.key == pygame.K_F11` -> Checks F11, fullscreen has entered the building
- `pygame.mouse.get_pos()` -> Gets mouse x/y, tracking the player's questionable decisions
- `pygame.mouse.get_pressed()` -> Gets currently held mouse buttons, click responsibly
- `event.type == pygame.MOUSEBUTTONDOWN` -> Checks for a mouse click, the user has chosen violence against the UI
- `event.button == 1` -> Checks left mouse button, democracy has spoken
- `event.button == 3` -> Checks right mouse button, alternative democracy
- `event.pos` -> Gets mouse position from that specific event, useful when checking clicks
- `event.type == pygame.MOUSEMOTION` -> Detects mouse movement, somebody is moving the expensive plastic
- `pygame.mouse.set_visible(False)` -> Hides cursor, congratulations you made navigation harder
- `pygame.key.set_repeat(300, 40)` -> Repeats KEYDOWN events after 300ms and every 40ms, useful for menus but dangerous for accidental spam

## Collisions

- `rect = img.get_rect(topleft=(x, y))` -> Creates a rectangle around an image, invisible cardboard box technology
- `rect.colliderect(other_rect)` -> Checks if two rectangles overlap, personal space has been violated
- `rect.collidepoint(mouse_pos)` -> Checks if a point is inside the rectangle, useful for buttons that might actually work
- `rect.move(dx, dy)` -> Returns a moved copy of a rectangle, original stays where it was because Python enjoys surprises
- `rect.move_ip(dx, dy)` -> Moves the actual rectangle, finally commitment
- `rect.center = (x, y)` -> Sets rectangle center, easier than calculating top-left like a caveman
- `rect.topleft = (x, y)` -> Sets rectangle top-left position, classic coordinate suffering
- `rect.x += 5` -> Moves rectangle horizontally, rectangle transportation services
- `rect.y += 5` -> Moves rectangle vertically, gravity's unpaid intern
- `rect.clamp_ip(screen.get_rect())` -> Keeps rectangle inside the screen, assuming it fits in the first place

## Main menu

- `scene = "menu"` -> Starts game on the main menu, because dropping players into gameplay is considered rude
- `if scene == "menu":` -> Runs menu logic, welcome to the screen nobody reads
- `elif scene == "game":` -> Runs gameplay logic, finally something happens
- `elif scene == "settings":` -> Runs settings logic, where players change things you spent hours choosing
- `elif scene == "pause":` -> Runs pause logic, game takes a legally required break
- `elif scene == "game_over":` -> Runs game-over logic, the player's skill issue has been documented
- `scene = "game"` -> Switches to gameplay, menu successfully escaped
- `scene = "settings"` -> Opens settings, customization has arrived
- `scene = "menu"` -> Returns to main menu, back to square one
- `scene = "pause"` -> Pauses gameplay through scene switching, time for reflection
- `scene = "game_over"` -> Shows game-over screen, thoughts and prayers
- `if scene == "game": update_game(dt)` -> Updates gameplay only while playing, no secret movement during menus
- `if scene == "menu": draw_menu()` -> Draws menu through a function, organization instead of spaghetti
- `elif scene == "game": draw_game()` -> Draws gameplay, same window different suffering

## Main menu buttons

- `play_button = pygame.Rect(380, 250, 200, 60)` -> Creates an invisible button area, premium invisible rectangle
- `pygame.draw.rect(screen, (70, 70, 70), play_button, border_radius=10)` -> Draws button background, UI development begins
- `mouse_pos = pygame.mouse.get_pos()` -> Gets cursor position, we must know where the human is pointing
- `hovered = play_button.collidepoint(mouse_pos)` -> Checks if cursor is over button, congratulations on discovering hover effects
- `button_color = (110, 110, 110) if hovered else (70, 70, 70)` -> Changes button color on hover, suddenly interactive
- `if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:` -> Detects left click, only put this inside your event loop
- `if play_button.collidepoint(event.pos): scene = "game"` -> Starts game when button is clicked, put this inside the click condition
- `button_text = font.render("PLAY", True, (255, 255, 255))` -> Creates button label, because invisible buttons are terrible UX
- `screen.blit(button_text, button_text.get_rect(center=play_button.center))` -> Centers text inside button, design degree unlocked
- `settings_button = pygame.Rect(380, 330, 200, 60)` -> Creates settings button, more rectangles for the rectangle collection
- `quit_button = pygame.Rect(380, 410, 200, 60)` -> Creates quit button, the most attractive feature

## Different scenes

- `def draw_menu():` -> Function responsible for drawing the menu, separation of concerns has entered the building
- `def draw_game():` -> Function responsible for drawing gameplay, finally some structure
- `def draw_settings():` -> Function responsible for settings UI, the options nobody changes
- `def update_game(dt):` -> Function for updating gameplay, where the actual suffering happens
- `def handle_menu_event(event):` -> Handles menu input, no need to interrogate every button in every scene
- `def handle_game_event(event):` -> Handles gameplay input, keyboard chaos stays where it belongs
- `def handle_settings_event(event):` -> Handles settings input, sliders and buttons get their own department
- `if scene == "menu": handle_menu_event(event)` -> Sends input to menu, no accidental jumping behind the menu
- `elif scene == "game": handle_game_event(event)` -> Sends input to gameplay, context matters apparently
- `elif scene == "settings": handle_settings_event(event)` -> Sends input to settings, organized suffering
- `previous_scene = scene` -> Remembers previous scene, useful for returning after pause
- `scene = previous_scene` -> Returns to previous scene, assuming you saved it before switching
- `def change_scene(new_scene):` -> Function for scene transitions, centralized bureaucracy
- `global scene` -> Allows a function to reassign the module-level scene variable, Python demands paperwork
- `scene = new_scene` -> Changes scene inside the function, teleportation for menus

## Scene transitions / fading

- `fade = pygame.Surface(screen.get_size())` -> Creates overlay matching the screen, cinematic ambitions detected
- `fade.fill((0, 0, 0))` -> Makes overlay black, darkness is affordable
- `fade.set_alpha(128)` -> Makes overlay partially transparent, budget cinematic transition
- `screen.blit(fade, (0, 0))` -> Draws overlay over the scene, congratulations on inventing darkness
- `fade_alpha = min(255, fade_alpha + 300 * dt)` -> Gradually increases darkness, frame-independent dramatic effect
- `fade.set_alpha(int(fade_alpha))` -> Applies fade transparency, alpha needs a whole number because apparently fractions are offensive
- `fade_alpha = max(0, fade_alpha - 300 * dt)` -> Gradually reveals the new scene, the darkness has been defeated
- `transitioning = True` -> Marks transition as active, don't switch scenes repeatedly every frame
- `transitioning = False` -> Ends transition, cinema is over

## JSON basics

- `import json` -> Imports JSON support, Python can now remember things between launches
- `data = {}` -> Creates an empty dictionary, future home of questionable player decisions
- `data = {"level": 1, "score": 0, "music": True}` -> Creates save data, progress and preferences in one tiny box
- `json.dumps(data)` -> Converts Python data into a JSON string, dictionary gets a passport
- `json.dumps(data, indent=4)` -> Creates readable JSON text, because one-line files are crimes against humanity
- `json.loads('{"level": 1}')` -> Converts JSON text into Python data, reverse engineering but legal
- `data["level"]` -> Reads level value, crashes if the key doesn't exist because Python believes in consequences
- `data.get("level", 1)` -> Reads level safely with default 1, fewer crashes and fewer regrets
- `data["score"] = 100` -> Changes score in memory, not saved to disk yet
- `data["music"] = False` -> Changes music preference, silence is a valid artistic direction
- `data.update({"level": 2, "score": 150})` -> Updates multiple values, efficiency has been discovered
- `del data["score"]` -> Removes score entry, financial records mysteriously disappearing
- `True` -> Becomes `true` in JSON, capitalization is apparently negotiable
- `False` -> Becomes `false` in JSON, same situation
- `None` -> Becomes `null` in JSON, nothingness now has a file format

## JSON writing

- `with open("save.json", "w", encoding="utf-8") as file:` -> Opens file for writing, creates it if missing and overwrites existing content
- `json.dump(data, file, indent=4)` -> Writes dictionary to JSON, put this inside the with block
- `json.dump(data, file, indent=4, ensure_ascii=False)` -> Saves readable Unicode text, Greek characters no longer become hieroglyphic escape codes
- `with open("settings.json", "w", encoding="utf-8") as file:` -> Opens settings file, the player gets preferences
- `json.dump(settings, file, indent=4)` -> Saves settings, put inside the with block because indentation still exists
- `file.write("hello")` -> Writes plain text, useful but not JSON unless your data is actually valid JSON
- `"w"` -> Write mode, destroys previous file contents, handle with basic respect
- `"a"` -> Append mode, adds text to the end, not how you normally update one JSON document

## JSON reading

- `with open("save.json", "r", encoding="utf-8") as file:` -> Opens save file for reading, assuming it exists
- `data = json.load(file)` -> Loads JSON into Python, put this inside the with block
- `"r"` -> Read mode, doesn't modify file, peaceful for once
- `data.get("score", 0)` -> Gets saved score or defaults to zero, bankruptcy protection
- `data.get("level", 1)` -> Gets saved level or starts at level one, mercy for new players
- `data.get("music", True)` -> Gets music preference, defaults to enabled
- `json.JSONDecodeError` -> Error raised when JSON is malformed, someone murdered the save file
- `FileNotFoundError` -> Error when file doesn't exist, your first launch is not a conspiracy
- `try:` -> Attempts an operation that might fail, optimism in code form
- `except (FileNotFoundError, json.JSONDecodeError):` -> Handles missing or broken JSON, your game survives reality

## Saving game progress

- `save_data = {"level": 1, "score": 0, "completed": []}` -> Default save structure, fresh player fresh suffering
- `save_data["level"] = current_level` -> Updates saved level in memory, disk still knows nothing
- `save_data["score"] = score` -> Updates score in memory, the economy is booming
- `save_data["completed"].append("tutorial")` -> Marks tutorial completed, player has survived the introduction
- `save_game()` -> Calls your custom saving function, assuming you actually wrote it
- `load_game()` -> Calls your custom loading function, again Python doesn't invent functions for you
- `if save_data["level"] > 1:` -> Checks whether player has progress, Continue button might finally be useful
- `scene = "game"` -> Starts gameplay after loading progress, time travel achieved
- `save_data["level"] = 1` -> Resets level, new game means new suffering
- `save_data["score"] = 0` -> Resets score, the stock market has crashed
- `save_data["completed"] = []` -> Clears completed levels, history erased
- `save_game()` -> Save after reset so old progress doesn't return like an unpaid debt

## Saving safely

- `from pathlib import Path` -> Imports path handling, less manual slash nonsense
- `SAVE_PATH = Path("save.json")` -> Defines save location, relative to current working directory
- `SAVE_PATH.exists()` -> Checks if save file exists, basic detective work
- `SAVE_PATH.parent.mkdir(parents=True, exist_ok=True)` -> Creates missing parent directories, useful when saves live in their own folder
- `temp_path = SAVE_PATH.with_suffix(".tmp")` -> Creates temporary save path, a little insurance against corrupted saves
- `with open(temp_path, "w", encoding="utf-8") as file:` -> Writes to temporary file first, assuming the disk cooperates
- `json.dump(save_data, file, indent=4)` -> Writes data inside that block, same old JSON magic
- `temp_path.replace(SAVE_PATH)` -> Replaces old save after writing finishes, safer than directly overwriting it
- `try: save_game()` -> Attempts saving, because disks occasionally choose violence
- `except OSError as error:` -> Catches filesystem failures, put this after try with an indented handler
- `print(f"Save failed: {error}")` -> Reports failure, better than pretending everything worked

## Settings saving

- `settings = {"music_volume": 0.5, "sfx_volume": 0.8, "fullscreen": False}` -> Default settings, civilization restored
- `settings["music_volume"] = 0.3` -> Changes music volume, player has functioning ears
- `settings["sfx_volume"] = 0.7` -> Changes sound effect volume, explosions are negotiable
- `settings["fullscreen"] = True` -> Remembers fullscreen preference, doesn't automatically change the window
- `settings["music_volume"] = max(0.0, min(1.0, settings["music_volume"]))` -> Keeps volume between zero and one, preventing mathematical stupidity
- `json.dump(settings, file, indent=4)` -> Saves settings inside an opened file, preferences survive restart
- `settings = json.load(file)` -> Loads settings from an opened file, the player doesn't have to suffer again

## Music

- `pygame.mixer.init()` -> Initializes audio mixer if needed, because silence wasn't part of the design
- `pygame.mixer.music.load("assets/music/menu.ogg")` -> Loads menu music, preferably something that doesn't sound like a dying printer
- `pygame.mixer.music.play()` -> Plays music once, the soundtrack has arrived
- `pygame.mixer.music.play(-1)` -> Loops music forever, psychological warfare through repetition
- `pygame.mixer.music.stop()` -> Stops music immediately, blessed silence
- `pygame.mixer.music.pause()` -> Pauses music, even the soundtrack needs a break
- `pygame.mixer.music.unpause()` -> Resumes music, the suffering continues
- `pygame.mixer.music.set_volume(0.5)` -> Sets music volume to 50%, your ears remain employed
- `pygame.mixer.music.get_volume()` -> Gets current music volume, useful for settings
- `pygame.mixer.music.fadeout(1000)` -> Fades music out over one second, dramatic departure
- `pygame.mixer.music.rewind()` -> Rewinds music to beginning, another chance at musical greatness
- `pygame.mixer.music.get_busy()` -> Checks whether music is actively playing, the DJ's attendance register
- `pygame.mixer.music.set_pos(10.0)` -> Seeks to approximately 10 seconds where supported, music time travel with format restrictions

## Music between scenes

- `current_music = None` -> Tracks current soundtrack, prevents restarting it every frame
- `def play_music(path):` -> Defines your own music-switching function, organized noise management
- `global current_music` -> Allows function to update current track, Python requires authorization
- `if current_music != path:` -> Checks if requested music differs, no unnecessary reloads
- `pygame.mixer.music.load(path)` -> Loads new soundtrack inside the condition, DJ changes records
- `pygame.mixer.music.play(-1, fade_ms=500)` -> Starts looping with a short fade-in, civilized noise
- `current_music = path` -> Remembers track, otherwise it reloads forever
- `play_music("assets/music/menu.ogg")` -> Calls your custom function for menu music, don't do this blindly every frame
- `play_music("assets/music/game.ogg")` -> Changes to gameplay music, stakes have increased
- `pygame.mixer.music.stop()` -> Stops soundtrack before changing scenes when silence is intentional

## Sound effects

- `click_sound = pygame.mixer.Sound("assets/sfx/click.wav")` -> Loads button click sound, tiny noise massive achievement
- `click_sound.play()` -> Plays click sound, your button now has a personality
- `jump_sound = pygame.mixer.Sound("assets/sfx/jump.wav")` -> Loads jump sound, gravity gets an audio department
- `jump_sound.play()` -> Plays jump sound, character has left the ground
- `error_sound = pygame.mixer.Sound("assets/sfx/error.wav")` -> Loads error sound, perfect for a debugging game
- `error_sound.play()` -> Plays error sound, player has disappointed the compiler
- `click_sound.set_volume(0.4)` -> Sets effect volume, clicking doesn't need to cause hearing damage
- `channel = click_sound.play()` -> Plays sound and returns its channel if available, sound now has management
- `pygame.mixer.stop()` -> Stops all sound effects, the entire audio department has been fired
- `pygame.mixer.Sound("assets/sfx/win.ogg")` -> Loads OGG sound effect, WAV isn't your only option

## Animations basics

- `frames = []` -> Creates list for animation frames, empty cinema
- `frames = [pygame.image.load(f"assets/player/{i}.png").convert_alpha() for i in range(4)]` -> Loads four animation frames, tiny flipbook technology
- `frame_index = 0` -> Starts animation at first frame, a humble beginning
- `animation_speed = 8` -> Sets animation speed to eight frames per second, separate from game FPS
- `frame_index += animation_speed * dt` -> Advances animation based on time, no speed advantage for expensive GPUs
- `frame_index %= len(frames)` -> Loops animation index, infinite walking achieved
- `current_frame = frames[int(frame_index)]` -> Selects current frame, float becomes an integer because lists have standards
- `screen.blit(current_frame, (x, y))` -> Draws current frame, congratulations on inventing cartoons
- `frame_index = 0` -> Resets animation, useful when switching actions
- `animation_speed = 12` -> Faster animation, character drank six coffees
- `animation_speed = 4` -> Slower animation, character now runs on an old laptop

## Sprite sheets

- `sheet = pygame.image.load("assets/player/spritesheet.png").convert_alpha()` -> Loads sprite sheet, multiple frames imprisoned in one PNG
- `frame = pygame.Surface((32, 32), pygame.SRCALPHA)` -> Creates transparent frame surface, 32x32 pixel luxury apartment
- `frame.blit(sheet, (0, 0), (64, 0, 32, 32))` -> Extracts a frame from sheet coordinates, assuming the sprites are aligned
- `frame = sheet.subsurface((64, 0, 32, 32)).copy()` -> Extracts and copies frame directly, less manual suffering
- `frames = [sheet.subsurface((i * 32, 0, 32, 32)).copy() for i in range(4)]` -> Extracts four horizontal frames, factory production
- `pygame.transform.scale(frame, (128, 128))` -> Enlarges sprite, pixel art gets promoted to billboard
- `pygame.transform.flip(frame, True, False)` -> Flips sprite to face opposite direction, animation budget cut in half

## Different character animations

- `animations = {"idle": idle_frames, "walk": walk_frames, "jump": jump_frames}` -> Stores animation lists, character finally has a personality
- `state = "idle"` -> Character starts idle, doing absolutely nothing professionally
- `state = "walk"` -> Switches to walking animation, employment begins
- `state = "jump"` -> Switches to jumping animation, gravity has been challenged
- `current_frames = animations[state]` -> Gets frames for current action, organized sprite chaos
- `if new_state != state:` -> Checks if animation changed, prevents resetting every frame
- `state = new_state` -> Updates current animation state, identity crisis resolved
- `frame_index = 0` -> Resets animation after state change, starts from the beginning
- `frame_index = (frame_index + animation_speed * dt) % len(current_frames)` -> Advances looping animation, forever and ever
- `screen.blit(current_frames[int(frame_index)], (x, y))` -> Draws selected animation frame, your PNG is officially alive
- `facing_left = True` -> Remembers direction, character can now acknowledge the left side of existence
- `sprite = pygame.transform.flip(current_frame, facing_left, False)` -> Flips sprite based on direction, no separate left animation needed

## One-time animations

- `frame_index = min(frame_index + animation_speed * dt, len(frames) - 1)` -> Plays animation once and stops on final frame, no infinite death animation
- `animation_finished = int(frame_index) == len(frames) - 1` -> Checks if last frame was reached, useful for scene changes
- `if animation_finished: scene = "game_over"` -> Changes scene after animation, dramatic timing achieved
- `frame_index = 0` -> Restarts one-time animation, another opportunity for disaster

## Timers / delays

- `pygame.time.get_ticks()` -> Gets milliseconds since pygame initialized, the game has developed a sense of time
- `start_time = pygame.time.get_ticks()` -> Records current time, stopwatch activated
- `elapsed = pygame.time.get_ticks() - start_time` -> Calculates elapsed milliseconds, mathematics returns
- `if elapsed >= 3000:` -> Checks if three seconds passed, assuming elapsed is in milliseconds
- `pygame.time.set_timer(pygame.USEREVENT + 1, 1000)` -> Creates repeating event every second, automated annoyance
- `if event.type == pygame.USEREVENT + 1:` -> Handles timer event, time has sent a notification
- `pygame.time.set_timer(pygame.USEREVENT + 1, 0)` -> Disables that timer, silence restored
- `pygame.time.delay(500)` -> Freezes execution for roughly half a second, usually terrible inside gameplay
- `dt = clock.tick(60) / 1000` -> Better timing for movement and animations, no freezing required

## Simple visual effects

- `flash = pygame.Surface(screen.get_size(), pygame.SRCALPHA)` -> Creates transparent overlay, special effects department opens
- `flash.fill((255, 255, 255, 100))` -> Makes translucent white overlay, flashbang for rectangles
- `screen.blit(flash, (0, 0))` -> Draws overlay, visual feedback achieved
- `shake_x = random.randint(-5, 5)` -> Generates random horizontal shake, import random first
- `shake_y = random.randint(-5, 5)` -> Generates random vertical shake, earthquake simulator
- `screen.blit(img, (x + shake_x, y + shake_y))` -> Draws shaken image, low-budget cinematography
- `alpha = max(0, alpha - 200 * dt)` -> Gradually reduces opacity, object fades into unemployment
- `sprite.set_alpha(int(alpha))` -> Applies opacity to sprite, disappearing act completed

## Useful Python for games

- `import random` -> Imports randomness, chaos is now officially supported
- `random.randint(1, 10)` -> Random integer from 1 to 10 inclusive, gambling mechanics without actual gambling
- `random.choice(["easy", "medium", "hard"])` -> Picks random option, difficulty roulette
- `random.uniform(0, 1)` -> Random decimal between zero and one, probability department
- `min(value, 100)` -> Limits maximum value, numbers have boundaries
- `max(value, 0)` -> Limits minimum value, negative health denied
- `max(0, min(value, 100))` -> Clamps value between zero and 100, mathematical prison
- `round(value, 2)` -> Rounds number to two decimal places, precision has standards
- `enumerate(items)` -> Loops with index and value, less manual counting
- `list.append(item)` -> Adds item to list, collection grows
- `list.pop()` -> Removes and returns last item, collection shrinks
- `dict.get("key", default)` -> Safely reads dictionary value, no unnecessary KeyError funerals
- `os.path.join("assets", "images", "player.png")` -> Builds file path, import os first
- `Path(__file__).resolve().parent` -> Gets folder containing current Python file, useful when launched from random directories

## Project organization

- `main.py` -> Main entry point, the conductor of this questionable orchestra
- `settings.py` -> Game constants and defaults, one place for your bad decisions
- `scenes/` -> Folder for scene files, organization instead of 3000 lines of suffering
- `scenes/menu.py` -> Main menu code, buttons get their own home
- `scenes/game.py` -> Gameplay code, actual game lives here
- `scenes/settings.py` -> Settings scene, configuration bureaucracy
- `assets/` -> Folder for images, fonts and audio, the game's warehouse
- `assets/images/` -> Images and sprites, visual evidence
- `assets/music/` -> Background tracks, soundtrack department
- `assets/sfx/` -> Sound effects, button clicking industry
- `assets/fonts/` -> Custom fonts, typography headquarters
- `data/` -> Static game data, levels and dialogue that ship with the game
- `saves/` -> Player progress and settings, the game's memory
- `requirements.txt` -> Dependency list, so other computers know what to install
- `pygame-ce` -> Package name for requirements, because importing pygame wasn't confusing enough

## Things to remember

- Load images, fonts and sounds before the game loop, unless you enjoy unnecessary suffering
- Draw everything inside the game loop, not in your imagination
- `screen.fill()` should usually come before drawing, unless you want accidental modern art
- `pygame.display.flip()` goes after drawing, revolutionary concept
- Update x/y to move stuff, then redraw it, teleportation wasn't in the budget
- Use `clock.tick(60)` instead of `time.sleep()` for FPS, this is a game not a hibernating bear
- Use `dt` for movement and animations, otherwise fast computers become speedrun machines
- Pygame CE still uses `import pygame`, because naming conventions are apparently optional
- Don't forget to save your files, Git cannot resurrect code you never committed
- If something doesn't work, check indentation before blaming the entire Python ecosystem
- `pygame.display.get_desktop_sizes()[0]` gets first monitor resolution, not necessarily your actual game window size
- `screen.get_size()` gets the current drawing surface dimensions, use this for centering UI
- `pygame.RESIZABLE` allows resizing, but your layout still needs to adapt
- `pygame.SCALED` helps fixed-resolution games scale, but test it because experimental convenience is still experimental
- Don't reload music every frame, your ears and storage deserve better
- Don't load PNGs every frame, your SSD didn't sign up for this
- Don't save JSON every frame, write when progress or settings actually change
- JSON doesn't support arbitrary Python objects, save simple numbers, strings, booleans, lists and dictionaries
- JSON is not secure against editing, players can change their own saves, welcome to offline gaming
- Use `try/except` for loading saves, corrupted files happen
- Save files should usually be excluded from Git, unless you want everyone's progress immortalized in commit history
- Keep static game data in Git, keep personal saves out of it
- Button collision uses rectangles, so the clickable area must match the actual button
- Mouse clicks should be handled in the event loop, not by repeatedly activating buttons every frame
- When changing animation state, reset the frame index once, not 60 times per second
- Don't mix milliseconds and seconds, `get_ticks()` uses milliseconds while `dt` usually uses seconds
- A sprite sheet is just multiple animation frames in one image, not black magic
- For pixel art, prefer integer scaling, because blurry pixels are a crime against aesthetics
- `convert_alpha()` usually needs a display mode to be created first, initialize your window before converting images
- `pygame.mixer.music` is best for streamed background music, `pygame.mixer.Sound` is better for short effects
- Pygame doesn't have a built-in scene manager, you make one yourself because apparently life was too easy
- Use functions for menus and scenes, otherwise your main loop becomes an archaeological excavation
- Keep one main event loop, multiple competing loops are an excellent way to create bugs
- Store game settings separately from save progress, unless you want deleting a save to reset the volume too
- Never trust that a file exists, computers are excellent at disappointing people
- Save relative to a deliberate folder, not whatever random working directory your terminal chose
- Test fullscreen, resizing, audio and saves before shipping, your computer is not every computer
- And finally, **if the game works, commit it before you touch anything else.**