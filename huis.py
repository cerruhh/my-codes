



from turtle import *

def teken(doen,getal):
    doen= doen.upper()
    if doen=="F":
        forward(getal)
    elif doen=="R":
        right(getal)
    elif doen=="L":
        left(getal)
    else:
        print("onbekend commando met input: ", doen, " nummer: ", getal)

def string_artist(progam):
    cmd_list = progam.split('-')
    for command in cmd_list:
        cmd_len = len(command)
        if cmd_len == 0:
            continue
        cmd_type = command[0]
        num = 0
        if cmd_len > 1:
            num_string = command[1:]
            num = int(num_string)
        print(command, ':', cmd_type, num)
        time.sleep(0.5)
        teken(cmd_type, num)

reset()
import time
commandostring = "L90-f100-l90-f10-r135-f180-r90-f180-r135-f10-L90-f100-r90-f245"

string_artist(commandostring)



#teken ("L", 90)
#¤teken ("f", 100)
#¤teken ("R", 45)
#¤teken ("f", 70)
#teken ("R", 90)
#teken ("f", 70)
#teken ("r", 45)
#teken ("f", 100)
#teken ("r", 90)
#teken ("f", 100)


#forward(100)
#right(45)
#forward(70)
#right(90)
#forward(70)
#right(45)
#forward(100)
#right(90)
#forward(100)

