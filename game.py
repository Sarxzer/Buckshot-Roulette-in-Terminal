import random as r
import time
import keyboard as k
import threading
import queue
import os

class Game:
    def __init__(self):
        self.save = open("save.txt", "a+") 
        self.printType("Welcome, sir!")
        if self.save.read() == "":
            self.firstTime()
        else:
            self.menu()
    
    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def printType(self, text):
        def print_chars():
            for i, char in enumerate(text):
                print(char, end="", flush=True)
                time.sleep(r.randrange(0, 100) / 900)
                if not self.printing:
                    return i  # return the index of the last printed character
            return len(text) - 1  # if all characters were printed, return the index of the last character
    
        self.printing = True
        q = queue.Queue()
        thread = threading.Thread(target=lambda q=q: q.put(print_chars()))
        thread.start()
    
        k.wait("space")
        self.printing = False
    
        # print the remaining part of the text
        if thread.is_alive():
            print(text[q.get() + 1:], end="")
            thread.join()
        print()
    
    def exit(self):
        self.printType("Goodbye!")
        self.save.close()
        exit()
    

    def firstTime(self):
        print("(space to continue)")
        k.wait("space")
        self.printType("You just woke up in a dark room.")
        k.wait("space")
        self.printType("This room looks like a bathroom.")
        k.wait("space")
        self.printType("You see a door in front of you and a broken computer.")
        k.wait("space")
        self.menu()

    def menu(self):
        self.printType("What will you do?")
        time.sleep(0.5)
        print("1. Go to the door")
        time.sleep(0.5)
        print("2. Go to the computer")
        time.sleep(0.5)
        print("3. Exit")

        choice = k.read_key()

        if choice == "1":
            self.door()
        elif choice == "2":
            self.printType("You go to the computer.")
            k.wait("space")
            self.printType("The computer is broken.")
            k.wait("space")
            self.printType("You go back.")
            k.wait("space")
            self.menu()
        elif choice == "3":
            self.exit()
        else:
            self.menu()
    
    def door(self, long=True):
        self.printType("You open the door.")
        k.wait("space")
        if long:
            self.printType("Behind the door is a balcony.")
            k.wait("space")
            self.printType("There is a guy smoking a cigarette and you hear a loud music from downstairs.")
            k.wait("space")
            self.printType("There is another door at the other side of the balcony.")
            k.wait("space")
            self.printType("What will you do?")
        
        time.sleep(0.5)
        print("1. Go to the guy")
        time.sleep(0.5)
        print("2. Go to the other door")
        time.sleep(0.5)
        print("3. Go back to the room")
        time.sleep(0.5)

        choice = k.read_key()

        if choice == "1":
            self.guy()
        elif choice == "2":
            self.otherDoor()
        elif choice == "3":
            self.menu()
        else:
            self.printType("You decided to wait a bit.")
            k.wait("space")  
            self.door()
    
    def guy(self):
        self.printType("You approach the guy.")
        k.wait("space")
        self.printType("He doesn't notice you.")
        k.wait("space")
        self.printType("You try to talk to him but he doesn't respond.")
        k.wait("space")
        self.printType("You decide to go back.")
        k.wait("space")
        self.door(False)
    
    def otherDoor(self):
        self.printType("You open the door.")
        k.wait("space")
        self.printType("Behind the door seems to be a storage room.")
        k.wait("space")
        self.printType("There is a table with a lot od cables connected and a shotgun in the middle.")
        k.wait("space")
        self.printType("A guy is sitting on a chair.")
        k.wait("space")
        self.printType("He is looking at you.")
        k.wait("space")
        self.printType("He greets you and offers you a seat.")
        k.wait("space")
        self.printType("The game have started.")
        k.wait("space")
        self.clear()
        self.game()
    
    def drawTable(self, lifePlayer=3, lifeEnemy=3, bullets=[1,1,2,2,0,0,0,0], toolsPlayer=[3,0,1,0,4,0,7,0], toolsEnemy=[5,0,2,0,4,0,0,6], shot=1):

        toolsNames = ["", "Saw", "Cigarette", "Beer", "Magnifying glass", "Handcuffs", "Burner phone", "Expired medicine", "Adrenaline", "Inverter"]

        lifeEnemy = ["☇"] * lifeEnemy + [" "] * (6 - lifeEnemy)
        lifePlayer = ["☇"] * lifePlayer + [" "] * (6 - lifePlayer)
        for i in range(8):
            if bullets[i] == 1:
                bullets[i] = "▒"
            elif bullets[i] == 2:
                bullets[i] = "▓"
            else:
                bullets[i] = " "
        bullets = " ".join(bullets)

        for i in range(8):
            toolsPlayer[i] = toolsNames[toolsPlayer[i]]

            if len(toolsPlayer[i]) < 16:
                toolsPlayer[i] += " " * (16 - len(toolsPlayer[i]))
            
            toolsEnemy[i] = toolsNames[toolsEnemy[i]]

            if len(toolsEnemy[i]) < 16:
                toolsEnemy[i] += " " * (16 - len(toolsEnemy[i]))
        
        #shot = 
            


        print("┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓")
        print("┃  ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓  ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓  ┃")
        print("┃  ┃" + toolsEnemy[0] + "┃   ┃" + toolsEnemy[1] + "┃  ┃" + toolsEnemy[2] + "┃   ┃" + toolsEnemy[3] + "┃  ┃")
        print("┃  ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛  ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛  ┃")
        print("┃                                                                                    ┣╍╍╍┓")
        print("┃  ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓  ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓  ┃ " + lifeEnemy[0] + " ┃")
        print("┃  ┃" + toolsEnemy[4] + "┃   ┃" + toolsEnemy[5] + "┃  ┃" + toolsEnemy[6] + "┃   ┃" + toolsEnemy[7] + "┃  ┃ " + lifeEnemy[1] + " ┃")
        print("┃  ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛  ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛  ┃ " + lifeEnemy[2] + " ┃")
        print("┃                                                                                    ┃ " + lifeEnemy[3] + " ┃")
        print("┃                                                                                    ┃ " + lifeEnemy[4] + " ┃")
        print("┃                                   ┏╍╍╍╍╍╍╍╍╍╍╍╍┓                   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┫ " + lifeEnemy[5] + " ┃")
        print("┣╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┫" + shot + "┣╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┫" + bullets + "┣╍╍╍┫")
        print("┃                                   ┗╍╍╍╍╍╍╍╍╍╍╍╍┛                   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┫ " + lifePlayer[5] + " ┃")
        print("┃                                                                                    ┃ " + lifePlayer[4] + " ┃")
        print("┃                                                                                    ┃ " + lifePlayer[3] + " ┃")
        print("┃  ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓  ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓  ┃ " + lifePlayer[2] + " ┃")
        print("┃  ┃" + toolsPlayer[0] + "┃   ┃" + toolsPlayer[1] + "┃  ┃" + toolsPlayer[2] + "┃   ┃" + toolsPlayer[3] + "┃  ┃ " + lifePlayer[1] + " ┃")
        print("┃  ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛  ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛  ┃ " + lifePlayer[0] + " ┃")
        print("┃                                                                                    ┣╍╍╍┛")
        print("┃  ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓  ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓  ┃")
        print("┃  ┃" + toolsPlayer[4] + "┃   ┃" + toolsPlayer[5] + "┃  ┃" + toolsPlayer[6] + "┃   ┃" + toolsPlayer[7] + "┃  ┃")
        print("┃  ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛  ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛  ┃")
        print("┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛")
        exit()
    
    #def game(self):

Game()