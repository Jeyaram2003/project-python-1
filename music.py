import pygame
import os
a=input("Enter the song name:")
pygame.mixer.init()

class MusicPlayer:
    def __init__(self, music_directory):
        self.music_directory = music_directory
        self.playing = False

    def load_song(self, a):
        a = os.path.join(self.music_directory, a)
        pygame.mixer.music.load(a)

    def play(self, a):
        self.load_song(a)
        pygame.mixer.music.play()
        self.playing = True
        print(f"Playing: {a}")

    def pause(self):
        if self.playing:
            pygame.mixer.music.pause()
            self.playing = False
            print("Music paused")

    def resume(self):
        if not self.playing:
            pygame.mixer.music.unpause()
            self.playing = True
            print("Music resumed")

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False
        print("Music stopped")

if __name__ == "__main__":
    music_dir = "C:\\Users\\jeyaram\\OneDrive\\Desktop\\python project"
    player = MusicPlayer(music_dir)

    while True:
        command = input("Enter a command (play, pause, resume, stop, quit):").strip().lower()
        if command == "play":
            player.play(a)
        elif command == "pause":
            player.pause()
        elif command == "resume":
            player.resume()
        elif command == "stop":
            player.stop()
        elif command == "quit":
            player.stop()
            break
        else:
            print("Unknown command, please try again.")


