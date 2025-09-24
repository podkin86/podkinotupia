import pygame

pygame.init()
color_screen = "white"
mode_verif = 1
screen = pygame.display.set_mode((1366,763))
g_verif = 1
clock = pygame.time.Clock()
color_circle = (0, 0, 0)
x = 400
y = 300

circle_taille = 25


screen.fill(color_screen) 



while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        
        if event.type == pygame.MOUSEMOTION and mode_verif == 0:

           
            x, y = event.pos 
            pygame.draw.circle(screen, color_circle, (x, y), circle_taille)

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
                screen.fill(color_screen) 
            
            elif event.key == pygame.K_g:
                if g_verif == 1:
                    color_circle = (255, 255, 255)

                    g_verif = 0
                else:
                    color_circle = (0, 0, 0)
                    g_verif = 1
                    
    
                

        if pygame.mouse.get_pressed()[0]:
            
            x, y = pygame.mouse.get_pos()    



        
        

            pygame.draw.circle(screen, color_circle, (x, y), circle_taille)



    pygame.display.flip() 
    clock.tick(60000)      
