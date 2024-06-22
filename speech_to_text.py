import speech_recognition

import pyttsx3

recognizer = speech_recognition.Recognizer()


while True:
    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=1) 
        audio =recognizer.listen(mic)
        text =recognizer.recognize_google(audio)
        
        text = text.lower()
        print(f"Recognized: {text}")
        n = int(input('Press 1 to continue and 0 to quit: '))
        if n == 1:
            continue
        if n == 0:
            break
