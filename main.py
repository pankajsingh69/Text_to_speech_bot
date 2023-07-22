import win32com.client
print("Welcome text to speech bot")

while True:
    say = input("Enter what you want me to say : ")
    if say == 'q':
        speaker.Speak("Bye Bye")
        break
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(say)
