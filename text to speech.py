import gtts
import pygame
from tkinter import *
from tkinter import filedialog, messagebox
import os

def text_to_speech(text, language):
    speech = gtts.gTTS(text=text, lang=language, slow=False)
    file = r"Speech_Recognition\text.mp3"

    speech.save(file)

    # Initialize Pygame mixer
    pygame.mixer.init()

    pygame.mixer.music.load(file)
    messagebox.showinfo("Success", "File converted to speech!")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()  # Stop the music playback
    pygame.mixer.quit()  # Quit Pygame mixer

def file_to_speech(filename, language):
    file = open(filename, "r").read().replace("\n", " ")

    speech = gtts.gTTS(text=str(file), lang=language, slow=False)
    file = r"Speech_Recognition\voice.mp3"
    speech.save(file)

    # Initialize Pygame mixer
    pygame.mixer.init()

    pygame.mixer.music.load(file)
    messagebox.showinfo("Success", "File converted to speech!")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()  # Stop the music playback
    pygame.mixer.quit()  # Quit Pygame mixer

def choose_file():

    root3=Tk()
    root3.title("Choose File to play")

    language = StringVar(root3)
    
    # dropdown menu options
    options = ["en","zh"]

    Label(root3, text='Language: ', font=('Arial', 15)).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    Entry(root3, textvariable=language, state='disabled').grid(row=2, column=0, padx=10, sticky='w')
    OptionMenu(root3, language, *options).grid(row=3, column=0, padx=10, pady=10, sticky='w')

    Button(root3, text="Confirm", command=lambda: [open_file()]).grid(row=4, column=0, padx=10, pady=10, sticky='w')

    def open_file():
        path = filedialog.askopenfilename()
        if path:
            file_to_speech(path,language.get())

    root3.mainloop()

def text_menu():
    root2 = Tk()
    root2.title("Text to Speech Menu")

    text = StringVar(root2)
    language = StringVar(root2)

    # dropdown menu options
    options = ["en","zh"]

    Label(root2, text='Enter the Information: ', font=('Arial', 15)).grid(row=0, column=0, padx=10, pady=10, sticky='w')

    Label(root2, text='Language: ', font=('Arial', 15)).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    Entry(root2, textvariable=language, state='disabled').grid(row=2, column=0, padx=10, sticky='w')
    OptionMenu(root2, language, *options).grid(row=3, column=0, padx=10, pady=10, sticky='w')

    Label(root2, text='Text: ', font=('Arial', 12)).grid(row=4, column=0, padx=10, pady=10, sticky='w')
    Entry(root2, textvariable=text, width=80).grid(row=5, column=0, padx=10)

    Button(root2, text='Confirm', font=('Arial', 15), command=lambda: text_to_speech(text.get(), language.get())).grid(row=5,column=1, pady=10)    

    root2.mainloop()

# main method
if __name__ == "__main__":
    root = Tk()
    root.title("Text-to-Speech")

    Label(root, text='Text to Speech', font=('Arial', 15)).grid(row=0, column=0, padx=10, pady=10, sticky='w')

    text_button = Button(root, text="Text to Speech", command=lambda:text_menu).grid(row=1, column=0, padx=10, pady=10, sticky='w')

    file_button = Button(root, text="Choose File", command=choose_file).grid(row=2, column=0, padx=10, pady=10, sticky='w')

    root.mainloop()
