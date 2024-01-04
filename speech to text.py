import speech_recognition as sr
import os
from tkinter import *
from tkinter import filedialog, messagebox

# Initialize the recognizer
r = sr.Recognizer()

def transcribe_audio(path):
    # Use SpeechRecognition to recognize the audio
    with sr.AudioFile(path) as source:
        audio = r.listen(source)  # Read the entire audio file
        text=""
        # convert speech to text
        try:
            text = r.recognize_google(audio)  # Use Google Speech Recognition API
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return text

def microphone():
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Start")
        # listen the audio data from the default microphone
        audio = r.listen(source)
        print("End")
        # convert speech to text
        text=""

        try: 
            # language: https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages
            text=r.recognize_google(audio,language="en-SG") # use google speech recogntion API
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            messagebox.showinfo("Error", "Google Speech Recognition could not understand the audio")
            # recall the method
            return microphone()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            messagebox.showinfo("Error", "Could not request results from Google Speech Recognition service")
            # recall the method
            return microphone()

        return text

# Function to handle file selection
def choose_file():
    root2 = Tk()
    root2.title("Transcription from Audio File")
    root2.geometry("500x100")

    text_box = StringVar(root2)

    Label(root2, text='Transcribed text: ', font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    Entry(root2, textvariable=text_box, width=80).grid(row=2, column=0,padx=10)

    # ask user to select the file
    path = filedialog.askopenfilename(filetypes = [("Audio files", ("*.mp3", "*.wav", "*.flac", "*.ogg", "*.aac")),("All files", "*.*")]) 
    if path:
        text = transcribe_audio(path)
        text_box.set(text)
        # messagebox.showinfo("Transcribed Text", text)
    root2.mainloop()    
    
def mic_transcription():
    root3 = Tk()
    root3.title("Transcription from Microphone")
    root3.geometry("500x100")

    buttonClicked=False
    text_box = StringVar(root3)

    def click_button():
        nonlocal buttonClicked
        buttonClicked = not buttonClicked

    Button(root3, text="Record", command=lambda: [text_box.set(microphone()), click_button()]).grid(row=0, column=0, padx=10, pady=10, sticky='w')
    
    Label(root3, text='Transcribed text: ', font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    Entry(root3, textvariable=text_box, width=80).grid(row=2, column=0, padx=10)

    root3.mainloop()

# main method
if __name__=="__main__":
    # # Path to the audio file
    # print("Hello, Welcome to Speech-to-Text Program")
    # print("1. transcribe an audio file")
    # print("2. transcribe from microphone")

    # valid_choice=False
    # while not valid_choice:
    #     choice=int(input("Please Select your choice: "))
        
    #     if choice==1:
    #         valid_choice=True

    #         valid_path=False
    #         while not valid_path:
    #             path=input("Enter Relative Path: ")
                
    #             # check whether file exists
    #             check_path=os.path.isfile(path)
    #             if check_path==True:
    #                 valid_path=True
    #                 text=transcribe_audio(path)
    #                 print("Transcribed Text:\n {:s}".format(text))
                    
    #     elif choice==2:
    #         valid_choice=True

    #         text=microphone()
    #         print("Transcribed Text:\n{:s}".format(text))
    #     else:
    #         valid_choice=False
    #         print("Invalid choice")

    root1 = Tk()
    root1.title("Speech-to-Text")
    
    Label(root1, text='Speech to Text', font=('Arial', 15)).grid(row=0, column=0, padx=10, pady=10, sticky='w')
    Label(root1, text='Select an option: ', font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky='w')

    # Create buttons for file selection and microphone transcription
    file_button = Button(root1, text="Select File", command=choose_file).grid(row=2, column=0, padx=10, pady=10, sticky='w')

    mic_button = Button(root1, text="Transcribe from Microphone", command=mic_transcription).grid(row=3, column=0, padx=10, pady=10, sticky='w')

    root1.mainloop()

    