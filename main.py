import pygame

pygame.init()

mode_verif = 0
screen = pygame.display.set_mode((1080,720))

clock = pygame.time.Clock()
couleur_rond = (255, 255, 255)
x = 400
y = 300

secret = 0

screen.fill("black") 
pygame.draw.circle(screen, couleur_rond, (x, y), 30)


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        
        if event.type == pygame.MOUSEMOTION:

            if mode_verif == 0:
                x, y = event.pos 

            else:
                pass


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_m:
                

                if mode_verif == 1:
                    mode_verif=0
                else:
                    mode_verif=1


        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos


        if secret == 1:
            screen.fill("black") 

        pygame.draw.circle(screen, couleur_rond, (x, y), 30)



    pygame.display.flip() 
    clock.tick(60)      
