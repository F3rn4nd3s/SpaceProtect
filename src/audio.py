import pygame
import os

class AudioManager:
    def __init__(self):
        pygame.mixer.init()

        base_path = os.path.join("assets", "sounds")

        self.sounds = {
            "shoot": pygame.mixer.Sound(os.path.join(base_path, "shoot.wav")),
            "explosion": pygame.mixer.Sound(os.path.join(base_path, "explosion.wav")),
            "hit": pygame.mixer.Sound(os.path.join(base_path, "hit.wav")),
            "game_over": pygame.mixer.Sound(os.path.join(base_path, "game_over.wav")),
        }

        for sound in self.sounds.values():
            sound.set_volume(0.4)

    def play_sound(self, name):
        if name in self.sounds:
            self.sounds[name].play()

    def play_music(self):
        pygame.mixer.music.load(os.path.join("assets", "sounds", "music.wav"))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()
