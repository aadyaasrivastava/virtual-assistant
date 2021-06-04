import pyttsx3                       # for text to audio conversion
import datetime                      # for obtaining date and time
import speech_recognition as sr      # for speech recognition and conversion to string
import wikipedia                     # for searching on wikipedia
import webbrowser                    # for opening a webpage in browser
import os                            # for reaching to a certain path
import random                        # for picking random number
import pyautogui                     # for taking screenshot
import requests                      # for making API requests
import json                          # for parsing data
import pywhatkit                     #for searching youtube
from datetime import date
from bs4 import BeautifulSoup        # for weather forecasting
import subprocess , time             # for opening  and closing the windows applications, after certain interval


# Text to speech using pyttsx3 module.
engine = pyttsx3.init()
def talk(text):
    """
    This function will convert given text to audio and plays it.
    """
    engine.setProperty("rate", 200)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()


def wish():
    """
    enabales  katherine will wish the user according to the time
    and ask for further commands.
    """
    hour = datetime.datetime.now().hour
    if (hour < 12):
        text = "Good morning Ma'am!"
        print(text)
        talk(text)
    elif (hour >= 12 and hour <= 18):
        text = "Good afternoon Ma'am!"
        print(text)
        talk(text)
    else:
        text = "Good evening Ma'am!"
        print(text)
        talk(text)
    text = "KATHERINE, at your services Ma'am. How may I help you?"
    print(text)
    talk(text)


def day_and_time():
    """
    This function will tell current date and time as per the user input.
    """
    today = str(date.today())
    text = "Ma'am Today's date is : " + today
    print(text)
    talk(text)

    from datetime import datetime
    time = datetime.today().strftime("%I:%M %p")
    text = "And current time is : " + time
    print(text)
    talk(text)


def takeCommand():
    """
    This function takes microphone input from user and returns a string.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening.....")
        # giving some time before considering it as final input.
        # r.pause_threshold = 1
        audio = r.listen(source , 5 , 5)

        # dealing with external module hence using exception handling.
        try:
           print("Recognizing input...")
           input = r.recognize_google(audio , language = "en-in")
           print(f"You said : {input}\n")

        except Exception as e:
            # print(e)
            text = "Please say it again Ma'am."
            print(text)
            talk(text)
            return "None"
        return input


def newsReader():
    """
    This function will tell top 5 news headlines using API and json module.
    """

    req = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=(OWN API PROVIDED BY WEBSITE)")
    dict = json.loads(req.text)

    text = "Top 5 News for today are:\n"
    print(text)
    talk(text)

    counter = 5
    arts = dict['articles']
    for i in arts:
        if(counter > 0):
            print("The Headline is - " + str(i["title"]))
            talk("The Headline is - " + str(i["title"]))

            print("Story - " + str(i["description"]))
            talk(i["description"])

            print("Checkout the link for detail : " + str(i['url']))
            talk("Moving to the next news...")

            counter -= 1


def there_exists(terms):
    """
    Function to check if required word or phrase is present in the text or not.
    """
    for term in terms:
        if term in input:
            return True



def details():
    """
    This function will print and talk written text.
    """
    text = "Hello Ma'am! I am Katherine. I am a virtual assistant created by Aadyaa Ma'am. " \
           "You can check the things that I can do by saying 'what can you do' or 'things you can do'"
    print(text)
    talk(text)



def katherineWork():
    """
        This function will print and talk written text.
    """
    text = "Ma'am, I can open numerous applications and webpages, play games, take screenshots, tell you time, date, weather, location and " \
           "can read news headlines, flip coin , search on spotify, google, youtube and wikipedia. I can also calculate, take notes etc." \
           "I am still learning new things from wonderful humans like you. Nice knowing your Ma'am."
    print(text)
    talk(text)




# main function
if __name__ == "__main__":
    wish()

    while True:
        input = takeCommand().lower()


        # Greetings.
        if there_exists(["hi" , "hello" , "hey" , "katherine you there"]):
            text = "Hello! katherine at your service Ma'am."
            print(text)
            talk(text)


        elif there_exists(["how are you" , "how you doing" , "whats up"]):
            text = "Hello! Thanks for asking! I am good Ma'am and all ready at your service Ma'am"
            print(text)
            talk(text)


        # Assistant Details.
        elif there_exists(["who are you" , "who made you" , "what is your name"]):
            details()


        # Things that katherine can do.
        elif there_exists(["what can you do" , "things you can do"]):
          katherineWork()


        # Logic behind each task execution as per the input.
        elif there_exists(["day","date","time"]):
            day_and_time()


        # Searching on wikipedia.
        elif ("wikipedia" in input):
            text = "Searching on Wikipedia Ma'am..."
            print(text)
            talk(text)
            input = input.replace("wikipedia" , "")
            try:
                result = wikipedia.summary(input , sentences=1)
                text = "Ma'am According to Wikipedia : " + result
                print(text)
                talk(text)
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it Ma'am, can you please say it again?"
                print(text)
                talk(text)


        # Searching on google
        elif there_exists(["search google" , "google search" , "search on google"]):
            text = "Searching on Google Ma'am..."
            print(text)
            talk(text)
            search_term = input.split("google")[-1]
            try:
                url = "https://google.com/search?q=" + search_term
                webbrowser.get().open(url)
                text = "This is what I found on Google Ma'am."
                print(text)
                talk(text)
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it Ma'am, can you please say it again?"
                print(text)
                talk(text)


        # Searching on spotify
        elif there_exists(["search spotify" , "spotify search"]):
            text = "Searching on Spotify Ma'am..."
            print(text)
            talk(text)
            search_term = input.split("spotify")[-1]
            try:
                url = "https://open.spotify.com/search/"+search_term
                webbrowser.get().open(url)
                text = "This is what I found on Spotify Ma'am."
                print(text)
                talk(text)
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it Ma'am, can you please say it again?"
                print(text)
                talk(text)

        # Searching on youtube
        elif there_exists(["search youtube" , "search on youtube"]):
            text = "Searching on Youtube Ma'am..."
            print(text)
            talk(text)
            search_term = input.split("youtube")[-1]
            try:
                url = "https://www.youtube.com/results?search_query=" + search_term
                text = "This is what I found on Youtube Ma'am."
                print(text)
                talk(text)
                webbrowser.get().open(url)
            except Exception as e:
                 # print(e)
                text = "Could not recognize or find it Ma'am, can you please say it again?"
                print(text)
                talk(text)


        # Opening different webpages.
        elif ("open youtube" in input):
            url = "https://www.youtube.com/"
            webbrowser.get().open(url)
        elif ("open google" in input):
            url = "https://www.google.com/"
            webbrowser.get().open(url)
        elif ("open linkedin" in input):
            url = "https://www.linkedin.com/"
            webbrowser.get().open(url)
        elif ("open github" in input):
            url = "http://github.com/"
            webbrowser.get().open(url)
        elif ("open gmail" in input):
            url = "http://gmail.com/"
            webbrowser.get().open(url)
        elif ("open twitter" in input):
            url = "https://twitter.com/"
            webbrowser.get().open(url)
        elif ("open facebook" in input):
            url = "https://www.facebook.com/"
            webbrowser.get().open(url)
        elif ("open instagram" in input):
            url = "https://www.instagram.com/"
            webbrowser.get().open(url)
        elif ("open flipkart" in input):
            url = "https://www.flipkart.com/"
            webbrowser.get().open(url)
        elif ("open amazon" in input):
            url = "https://www.amazon.in/"
            webbrowser.get().open(url)
        elif ("open stack overlow" in input):
            url = "https://stackoverflow.com/"
            webbrowser.get().open(url)
        elif ("open geeksforgeeks" in input):
            url = "https://www.geeksforgeeks.org/"
            webbrowser.get().open(url)


        # playing music.
        elif there_exists(["play" , "music" , "play music" , "song"]):
            song = text.replace('play', ' ')
            url = "https://www.youtube.com//"
            webbrowser.get().open(url)
            talk('playing' + song)
            pywhatkit.playonyt(song)



        # opening coding platforms (IDEs) and other applications.
        elif ("open code blocks" in input):
            location = "#"
            os.startfile(location)
        elif ("open visual studio" in input or "open vs code" in input):
            location = "#"
            os.startfile(location)
        elif ("open git" in input):
            location = "#"
            os.startfile(location)
        elif ("open pycharm" in input):
            location = "#"
            os.startfile(location)
        elif ("open netbeans" in input):
            location = "#"
            os.startfile(location)
        elif ("open chrome" in input):
            location = "#"
            os.startfile(location)
        elif ("open word" in input):
            location = "#"
            os.startfile(location)
        elif ("open excel" in input):
            location = "#"
            os.startfile(location)
        elif ("open powerpoint" in input):
            location = "#"
            os.startfile(location)
        elif ("open adobe" in input):
            location = "#"
            os.startfile(location)
        elif ("open notepad" in input):
            location = "#"
            os.startfile(location)


        # opening emails (inbox).
        elif there_exists(["mails" , "mail" , "my email" , "my emails"]):
            url = "https://mail.google.com/mail/u/0/#inbox"
            webbrowser.get().open(url)
            text = "Here are your mails Ma'am."
            print(text)
            talk(text)


        # news reading.
        elif ("news" in input):
                newsReader()


        # current location.
        elif ("location" in input):
            import geocoder
            g = geocoder.ip('me')
            talk(str(g.latlng))
            print(g.latlng)


        # Opening camera
        elif ("camera" in input):
            subprocess.run('start microsoft.windows.camera:', shell=True)
            time.sleep(11)
            text = "Ma'am it will automatically close after 11 seconds."
            print(text)
            talk(text)
            subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)


        # make a note
        elif there_exists(["make a note" , "take a note" , "take note" , "takes notes"]):
            text = "Opening note taker..."
            print(text)
            talk(text)
            try:
                url = "https://www.google.co.in/keep//#home"
                text = "Note taker opened Ma'am."
                print(text)
                talk(text)
                webbrowser.get().open(url)
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it Ma'am, can you please say it again?"
                print(text)
                talk(text)


        # Take screenshot
        elif there_exists(["capture" , "capture screen" , "take screenshot" , "screenshot"]):
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save("D:\katherine (virtual assistant)\\" + "_Katherine_screenshot.png")
            text = "Screenshot taken Ma'am."
            print(text)
            talk(text)



        # Play Rock , Paper , Scissor Game
        elif there_exists(["game" , "play a game" , "rock paper scissor"]):
            text = "Please choose among rock, paper and scissor"
            print(text)
            talk(text)

            pmove = takeCommand()

            moves = ["rock", "paper", "scissor"]
            cmove = random.choice(moves)

            if pmove == cmove:
                text = "the match is draw"
                print(text)
                talk(text)
            elif (pmove == "rock" and cmove == "scissor") or (pmove == "paper" and cmove == "rock") or (pmove == "scissor" and cmove == "paper"):
                text = "Player wins"
                print(text)
                talk(text)
            elif (pmove == "scissor" and cmove == "rock") or (pmove == "rock" and cmove == "paper") or ("paper" and cmove == "scissor"):
                text = "Computer wins"
                print(text)
                talk(text)


        # Weather Forecasting.
        elif there_exists(["temperature" , "weather" , "what is the weather" , "how is the weather"]):
            try :
                url = "https://google.com/search?q=" + input
                r = requests.get(url)
                data = BeautifulSoup(r.text , "html.parser")
                weather = data.find("div" , class_="BNeawe").text
                output = "Current weather is : " + weather
                print(output)
                talk(output)
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it Ma'am, can you please say it again?"
                print(text)
                talk(text)


        # Toss a coin
        elif there_exists(["toss" , "flip" , "coin"]):
            moves = ["head" , "tails"]
            choice = random.choice(moves)
            text = "Ma'am we have got : " + choice
            print(text)
            talk(text)

        # Calculations.
        elif there_exists(["calculate" , "plus" , "minus" , "add" , "subtract" , "multiply" , "divide" ,
                           "+" , "-" , "*" , "/" , "power" or "**"]):
            try:
                value = input.split()[1]
                if value == '+' or value == "add" or value == "plus":
                    talk(int(input.split()[0]) + int(input.split()[2]))
                elif value == '-' or value == "minus" or value == "subtract":
                    talk(int(input.split()[0]) - int(input.split()[2]))
                elif value == 'multiply':
                    talk(int(input.split()[0]) * int(input.split()[2]))
                elif value == 'divide':
                    talk(int(input.split()[0]) / int(input.split()[2]))
                elif value == 'power':
                    talk(int(input.split()[0]) ** int(input.split()[2]))
                else:
                    talk("Wrong Operator")
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it Ma'am, can you please say it again?"
                print(text)
                talk(text)

        # About creator.
        elif there_exists(["creator", "Aadyaa"]):
            text = '''
                     Aadyaa Srivastava is a self taught pragmatic  programmer,Web Developer, Writer and marketer.
                    She is currently a Sophomore in Maharaja Agrasen University,pursuing her bachelors in 
                    Computer Science and Engineering. She  loves to create major and minor projects with an aim
                    to make daily life easy.Infact am also one of her projects made in Python. She believes words 
                    when spoke in right time on right place can have a huge positive impact on an individual.
                    So she wrote volunteered to write for NGO to highlight social taboos against humanity.
                    She is a Software Developer with an experience in C, C plus plus, Python, Data Structures, 
                    Algorithm,Cloud Services, Technical Content Writing, Proofreading and Front End Web Development.

                    '''
            talk(text)

        # Terminating KATHERINE.
        elif there_exists(["sleep" , "Ram_Ram","nothing" ,"adios ","jalga" "bye" , "exit" , "quit" , "thank you"]):
            text = "Bye. See you soon Ma'am. Have a nice day. Take care!"
            print(text)
            talk(text)
            break


