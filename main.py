import pygame
import assets
import configs

from objects.bird import Bird
from objects.floor import Floor
from objects.bg import Bg
from objects.pipe import Pipe
from objects.start_message import StartMessage
from objects.over_message import OverMessage
from objects.score import Score

pygame.init()
       
screen = pygame.display.set_mode((configs.screen_width, configs.screen_height))
clock = pygame.time.Clock()
pipe_create_event = pygame.USEREVENT
running = True
gameover = False
gamestarted = False


assets.load_sprites()
assets.load_audios()

sprites = pygame.sprite.LayeredUpdates()

def create_sprites():
    Bg(0, sprites)
    Bg(1, sprites)
    Floor(0, sprites)
    Floor(1, sprites)
    return Bird(sprites), StartMessage(sprites), Score(sprites)

bird, start_message, score = create_sprites()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pipe_create_event:
            Pipe(sprites)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not gamestarted and not gameover:
                gamestarted = True
                start_message.kill()
                pygame.time.set_timer(pipe_create_event, 1500)
            if event.key == pygame.K_ESCAPE and gameover:
                gameover = False
                gamestarted = False
                sprites.empty()
                bird, start_message, score = create_sprites()

        bird.handleEvent(event)

    screen.fill(0)

    sprites.draw(screen)

    if gamestarted and not gameover:
        sprites.update()

    if bird.checkCollision(sprites) and not gameover:
        gameover = True 
        gamestarted = False 
        over_message = OverMessage(sprites)  
        pygame.time.set_timer(pipe_create_event, 0)
        assets.play_audio("hit")

    for sprite in sprites:
        if type(sprite) is Pipe and sprite.passedis():
            score.value += 1
            assets.play_audio("point")


    pygame.display.flip()
    clock.tick(configs.fps)


pygame.quit()