import pyttsx3                      #text-to-speech module
import speech_recognition as sr     #speech recognition module 
import datetime                     #date,time module
import wikipedia as wiki            #wikipedia
import webbrowser as web


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
#print(voices[1].id)     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
engine.setProperty('voice',voices[1].id)


def speak(audio):        #audio functionality
    engine.say(audio)
    engine.runAndWait()

def wishAmartya():      #wishAmartya function greets once main function checked
    
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 1
            audio = r.listen(source)  
            initiate = r.recognize_google(audio, language='en-in')
            print("I am ready")
        
            if 'toxic' or 'toxic' in initiate:
                
                hour = int(datetime.datetime.now().hour)
                #print(hour)
                if hour>=0 and hour<12:
                    speak("Good Morning Sir! ")
                elif hour>=12 and hour<18:
                    speak("Good Afternoon Sir!")
                else:
                    speak("Good Evening Sir!")
            else:
                print("*************")
            
    except Exception:
        # print(e)
        print("Waiting for initialization")
        return "None"

def takeOrder():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:            #chances of error
        print("On it....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
     
    except Exception:
        # print(e)
        print("........")
        
        return "None"
    return query
    

if __name__=="__main__": 
    wishAmartya()
    while True:            #main function
        
    
        query = takeOrder().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wiki.summary(query, sentences=1)
            print(results)
            speak("Wikipedia says")
            speak(results)

        elif 'toxic' in query:
            speak('how can i help u sir')  

        elif 'open whatsapp' in query:
            web.get().open("https://web.whatsapp.com/")

        elif 'open classroom' in query or 'open class' in query:
            web.get().open("https://classroom.google.com/u/1/a/not-turned-in/all")

        elif 'open youtube' in query or 'open Youtube' in query:
            web.get().open("https://youtube.com")

        elif 'open google' in query:
            web.get().open("https://www.google.com/")

        elif 'goodbye' in query or 'bye' in query or 'main chalta hun' in query or 'khuda hafiz' in query:
            speak('bye')
            break
   
    
    
