#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os, sys
from os import system
from sys import platform
import random
from termcolor import cprint

"""
Rules
stone paper scissors

a  -> stone     win  scissors
s  -> paper     win  stone
d  -> scissors  win  paper

"""

def randEnemy():
    enemy = random.randrange(1,4)
    if (enemy == 1):
        return "a"
    elif (enemy == 2):
        return "s"
    elif (enemy == 3):
        return "d"

def string_check(question):
    y = False
    while y != True:
        s = input(question)
        y = str.isalpha(s)
        if s == "a" or s == "s" or s == "d":
            y = True
        else:
            y = False
    return s

def clearscreen():
    """
    Check OS and setting the right method.
    """
    if platform == "linux" or platform == "linux2":
        system('clear')
    elif platform == "win32":
        system('cls')


""" ------ MAIN ------ """
def main():
    while True:
        clearscreen()        
        cprint("#" * 80)
        cprint("")
        cprint("Hello this is a stone paper scissors game".center(80))
        cprint("Press Ctrl-C to exit".center(80))
        cprint("")
        cprint("#" * 80)

        e=randEnemy()
        my=string_check('Choose Stone = [a] Paper = [s] Scissors = [d] : ')
        if e == "a":
            er = "Stone"
        elif e == "s":
            er = "Paper"
        else:
            er = "Scissors"

        if my == "a":
            myr = "Stone"
        elif my == "s":
            myr = "Paper"
        else:
            myr = "Scissors"

        cprint(f"Your choice is: {myr}")
        cprint(f"Enemy choise is: {er}")

        """ -- DRAW -- """
        if my == "a" and e == "a":
            cprint("Draw", 'yellow')
        if my == "s" and e == "s":
            cprint("Draw", 'yellow')
        if my == "d" and e == "d":
            cprint("Draw", 'yellow')

        """ -- I WIN -- """
        if my == "a" and e == "d":
            cprint("You Won", 'green')
        if my == "s" and e == "a":
            cprint("You Won", 'green')
        if my == "d" and e == "s":
            cprint("You Won", 'green')

        """ -- ENEMY WIN -- """
        if e == "a" and my == "d":
            cprint("You Lost", 'red')
        if e == "s" and my == "a":
            cprint("You lost", 'red')
        if e == "d" and my == "s":
            cprint("You Lost", 'red')


        cprint("#" * 80)
        input("Press enter to continue...".center(80))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nBye Bye!")

