import customtkinter as ctk
from customtkinter import filedialog
import pygame

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('green')

soundPath = None

class MP3Player:
    def __init__(self):
        self.path = None
        self.isRunning = False
        self.musicLen = 0
        self.minutes = 0
        self.seconds = 0
    
    def openSound(self):
        self.path = filedialog.askopenfilename(filetypes=[('MP3 Files', '*.mp3')])
        pygame.mixer.init()
        pygame.mixer.music.load(self.path)
        self.musicLen = pygame.mixer.Sound(self.path).get_length()
        self.minutes = int(self.musicLen // 60)
        self.seconds = int(self.musicLen % 60)
        musicLengthText.configure(text=f"{self.minutes}:{self.seconds}")
        musicSlider.configure(from_=0, to=self.musicLen)  
        
    def playSound(self):
        if not pygame.mixer.music.get_busy():  
            pygame.mixer.music.play()
            self.isRunning = True
        else:
            pygame.mixer.music.stop()
            self.isRunning = False
    
    def updateSlider(self):
        if self.isRunning:
            position = pygame.mixer.music.get_pos() / 1000  # Get position in seconds
            musicSlider.set(position)
        root.after(100, self.updateSlider)  

root = ctk.CTk()
root.title("Wroblefy")
root.geometry('650x450')

mp3Player = MP3Player()


openButton = ctk.CTkButton(root, text='Open MP3', corner_radius=10, command=mp3Player.openSound)
openButton.pack(pady=True)  


playButton = ctk.CTkButton(root, text='▶', corner_radius=10, command=mp3Player.playSound)
playButton.pack(pady=True)


musicSlider = ctk.CTkSlider(root, from_=0, to=1)
musicSlider.pack(pady=True)


musicLengthText = ctk.CTkLabel(root, text="00:00")
musicLengthText.pack(pady=True)

mp3Player.updateSlider() 

historyFrame = ctk.CTkFrame(root, width=200,height=150,corner_radius=15)
historyFrame.pack(pady=True)

root.mainloop()
