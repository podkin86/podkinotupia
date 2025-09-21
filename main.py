import pygame

pygame.init()


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

        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_d:

                x = x + 5
    

            elif event.key == pygame.K_q:

                x = x - 5

            elif event.key == pygame.K_s:

                y = y + 5


            elif event.key == pygame.K_z:

                y = y - 5

            elif event.key == pygame.K_m:
                
                

                if secret == 1:
                    secret=0
                else:
                    secret=1


        elif event.type == pygame.KEYUP:


            if event.key == pygame.K_d:

                x = x + 5
    

            elif event.key == pygame.K_q:

                x = x - 5

            elif event.key == pygame.K_s:

                y = y + 5


            elif event.key == pygame.K_z:

                y = y - 5

        if secret == 1:
            screen.fill("black") 

        pygame.draw.circle(screen, couleur_rond, (x, y), 30)



    pygame.display.flip() 
    clock.tick(60)      
