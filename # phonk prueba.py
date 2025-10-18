import time
import random
import pygame
import os
from PIL import Image


funk_file_path = '/home/fernando/Música/LABUBU FUNK.mp3'

y = True

def abrir_imagen():
    try:
        imagen = Image.open("/home/fernando/Imágenes/cara phonk.jpg")
        imagen.show()
    except FileNotFoundError:
        pass
    except Exception:
        pass

while y == True:
    x = random.randint(1,10000)
    time.sleep(1)
    print(x)

    def check_and_play_funk():
    
        
        if not os.path.exists(funk_file_path):
            return

        try:
            pygame.init()
            pygame.mixer.init()
        except pygame.error:
            return 
        
        try:
            pygame.mixer.music.load(funk_file_path)
            pygame.mixer.music.play(0) 
            
            while pygame.mixer.music.get_busy():
                time.sleep(0.5)

        except pygame.error:
            pass

        finally:
            pygame.mixer.music.stop()
            pygame.quit()
            
    if x == 1:
         check_and_play_funk()
         abrir_imagen()
         y = False
