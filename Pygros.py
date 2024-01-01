#Pygros新概念音游
#凌落尘 2024.1.1

import pygame
import sys
import time
from pyautogui import size

class Pygros:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size())
        pygame.display.set_caption("Pygros")
    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
if __name__ == "__main__":
    ai = Pygros()
    ai.main()
