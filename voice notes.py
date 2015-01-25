import tkinter.filedialog
from tkinter import *
import speech_recognition
			
class App:

    def new_file(self):
        # clear the text
        self.text.delete(0.0, END)

    def save_as(self):
        # returns the saved file
        file = tkinter.filedialog.asksaveasfile(mode='w')
        textoutput = self.text.get(0.0, END) # get all the text
        file.write(textoutput.rstrip()) # with blank perameters, this cuts off all whitespace after a line.
        file.write("\n") # then we add a newline character.

    def open_file(self):
        # returns the opened file
        file = tkinter.filedialog.askopenfile(mode='r')
        fileContents = file.read() # Get all the text from file.

        # set current text to file contents
        self.text.delete(0.0, END)
        self.text.insert(0.0, fileContents)    
	
    def record(self):
        r = speech_recognition.Recognizer()
		
		# use default microphone as the audio source
        with speech_recognition.Microphone() as source:
            audio = r.listen(source) 
			
        # recognize speech using Google Speech Recognition
        try:
            self.text.insert(0.0, r.recognize(audio)) 
        except LookupError:                            		
            self.text.insert(0.0, "Could not understand audio") 
		
    def __init__(self):
        # set up the notepad, title and size
        self.root = Tk()
        self.root.title("Simple Voice Notepad")
        self.root.geometry("300x400")
                   
        # set up buttons
        button_bar = Menu(self.root)
        button_bar.add_command(label="Start record", command=self.record)
        button_bar.add_command(label="Save note", command=self.save_as)
        button_bar.add_command(label="New note", command=self.new_file)
        button_bar.add_command(label="Open note", command=self.open_file)

        self.root.config(menu=button_bar)
			
        # set up the text widget
        self.text = Text(self.root)
        self.text.pack(expand=YES, fill=BOTH) # expand to fit vertically and horizontally


app = App()
app.root.mainloop()