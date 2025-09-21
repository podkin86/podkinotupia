import pygame

pygame.init()

mode_verif = 1
screen = pygame.display.set_mode((1366,763))

clock = pygame.time.Clock()
couleur_rond = (0, 0, 0)
x = 400
y = 300

circle_taille = 150


screen.fill("white") 



while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        
        if event.type == pygame.MOUSEMOTION and mode_verif == 0:

           
            x, y = event.pos 

        else:
            pass


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                

                if mode_verif == 1:
                    mode_verif=0
                else:
                    mode_verif=1

            elif event.key == pygame.K_6:
                if circle_taille > 5:
                    circle_taille = circle_taille - 5
            
            elif event.key == pygame.K_EQUALS:
                if circle_taille < 146:
                    circle_taille = circle_taille + 5

            elif event.key == pygame.K_r:
                screen.fill("black") 

                

        if pygame.mouse.get_pressed()[0]:
            
            x, y = pygame.mouse.get_pos()    



        
        

        pygame.draw.circle(screen, couleur_rond, (x, y), circle_taille)



    pygame.display.flip() 
    clock.tick(60000)      
