import pyttsx3

# Initialize the pyttsx3 object
engine = pyttsx3.init()

# Text-to-speech conversion function
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

#Choose voice (male or female)
voices = engine.getProperty('voices')

print("Choose the voice you want: 1:Female   0:Male")
t = int(input())
engine.setProperty('voice', voices[t].id)

print("Choose the reading speed you want:")
x = int(input())
engine.setProperty('rate', x)

# Enter the text to convert
text = input("Enter the text you want to convert to speech: ")

# Call the text-to-speech function
text_to_speech(text)
