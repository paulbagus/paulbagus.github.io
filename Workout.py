import pyttsx3 #python text to speech module (pip install py3-tts), documentation: https://pyttsx3.readthedocs.io/en/latest/
import time
from numpy import random

engine = pyttsx3.init()
voices = engine.getProperty("voices")

#################function definitions######################

def setVoice(number, speed=150):
    #number is an integer between 0 an 142
    engine.setProperty("voice", voices[number].id)
    engine.setProperty("rate", speed)

def say(text):
    engine.say(text)
    engine.runAndWait()

def beginCountdown():
    say("three")
    time.sleep(1)
    say("two")
    time.sleep(1)
    say("one")
    time.sleep(1)
    say("go!")

def endCountdown():
    say("three")
    time.sleep(1)
    say("two")
    time.sleep(1)
    say("one")
    time.sleep(1)
    say("finished!")

def ready():
    print("Ready? Press enter!")
    input()

def timer(workout_time):
    beginCountdown()
    time.sleep(workout_time-3)
    endCountdown()

def finished():
    print("Finished? Press Enter!")
    input()

def buddabred():

    print("Welcome to Buddabred Workout!")
    setVoice(39, 150)#Good News
    say("Welcome to Buddabread Workout!") 

    budda_loop = True
    while budda_loop:
        try:
            print("Press enter to start...")
            input()
            print("Bred: 3x12s Halten schwerer Griff")
            setVoice(100, 200)#Rocko
            say("Bred")
            ready()
            timer(12)
            ready()
            timer(12)
            ready()
            timer(12)

            print("Pump: Max ABC-Pullups guter Griff")
            say("Pump")
            finished()

            print("Budda: 15s Slope")
            say("Butter")
            ready()
            timer(15)

            print("Buddapump: 15s Slope mit Kompression und Beine 90 Grad")
            say("Butterpump")
            ready()
            timer(15)

            print("Bredcrumb: 5 2-Finger Pullups oder 7 normale Pullups")
            say("Bredcrump")
            finished()
            print("Vaddapump (a) or Vaddacrumb (b)?")
            say("Faddapump or Faddacrumb?")

            input_loop = True
            while input_loop:
                choice = input()
                match choice:
                    case "a":
                        print("Faddapump it is! Max halten Kompression guter Griff!") 
                        say("Faddapump it is!")
                        input_loop = False
                    case "b":
                        print("Faddacrump it is! Schwerer Griff max halten!")
                        say("Faddacrump it is!")
                        input_loop = False
                    case _:
                        print("Type in 'a' or 'b'")

            finished()

            print("Repeat? y/n")
            say("Repeat?")

            input_loop = True
            while input_loop:
                choice = input()
                match choice:
                    case "y":
                        print("Strong!")
                        say("Strong!")
                        input_loop = False
                    case "n":
                        print("Weak! Next time you'll do better!")
                        say("Weak! Next time you'll do better!")
                        input_loop = False
                        budda_loop = False
                    case _:
                        print("Type in 'y' or 'n'")

        except KeyboardInterrupt:
            setVoice(100, 200)#Rocko
            print("\nYou give up? y/n")
            say("You give up?")
            input_loop = True
            while input_loop:
                choice = input()
                match choice:
                    case "n":
                        print("Strong! But even thinking about giving up is weak! So start again from the beginning to learn your lesson.")
                        say("Strong! But even thinking about giving up is weak! So start again from the beginning to learn your lesson.")
                        input_loop = False
                    case "y":
                        print("Weak! You are a disgrace!")
                        say("Weak! You are a disgrace!")
                        
                        input_loop = False
                        budda_loop = False
                    case _:
                        print("Type in 'y' or 'n'")

    print("Buddabred workout is over!")
    setVoice(6, 100)#Bad News
    say("Buddabred workout is over!")

def bruce():

    print("Welcome to Bruce Lee Workout!")
    setVoice(39, 150)#Good News
    say("Welcome to Bruce Lee Workout!") 

    bruce_loop = True
    while bruce_loop:
        try:
            print("Press enter to start...")
            input()
            print("20x Russian Twist (both sides).")
            setVoice(100, 200)#Rocko
            say("Twenty times russian twist.")
            finished()

            print("10 Leg Raises.")
            say("Ten leg raises.")
            finished()

            print("15 Crunches.")
            say("Fifteen crunches.")
            finished()

            print("10 Heel Touches (both sides).")
            say("Ten Heel Touches")
            finished()
            
            print("10 Modified V-Sits.")
            say("10 Modified V-Sits.")
            finished()

            print("Hold!")
            say("Hold!")
            ready()
            timer(90)

            coinflip = random.randint(2)

            match coinflip:
                case 0:
                    pass
                case 1:
                    print("Surprise! Hold Plank as long as you can!")
                    say("Surprise!")
                    finished()
            
            print("Repeat? y/n")
            say("Repeat?")

            input_loop = True
            while input_loop:
                choice = input()
                match choice:
                    case "y":
                        print("Strong!")
                        say("Strong!")
                        input_loop = False
                    case "n":
                        print("Weak! Next time you'll do better!")
                        say("Weak! Next time you'll do better!")
                        input_loop = False
                        bruce_loop = False
                    case _:
                        print("Type in 'y' or 'n'")

        except KeyboardInterrupt:
            setVoice(100, 200)#Rocko
            print("\nYou give up? y/n")
            say("You give up?")
            input_loop = True
            while input_loop:
                choice = input()
                match choice:
                    case "n":
                        print("Strong! But even thinking about giving up is weak! So start again from the beginning to learn your lesson.")
                        say("Strong! But even thinking about giving up is weak! So start again from the beginning to learn your lesson.")
                        input_loop = False
                    case "y":
                        print("Weak! You are a disgrace!")
                        say("Weak! You are a disgrace!")
                        
                        input_loop = False
                        bruce_loop = False
                    case _:
                        print("Type in 'y' or 'n'")

#################end of function definitions######################

print("Which workout do you want to do? Buddabred (a) or Bruce Lee? (b)")

input_loop = True
while input_loop:
    choice = input()
    match choice:
        case "a":
            buddabred() 
            input_loop = False
        case "b":
            bruce()
            input_loop = False
        case _:
            print("Type in 'a' or 'b'")


