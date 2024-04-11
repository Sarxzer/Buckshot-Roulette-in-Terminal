import random as r
import time
import os
from collections import Counter

#Auto-Install Required Modules
try:
    import keyboard as k
except:
    os.system("pip install keyboard")
    import keyboard as k


class Game:
    #def __init__(self):
    #    self.save = open("save.txt", "a+") 
    #    self.printType("Welcome, sir!")
    #    if self.save.read() == "":
    #        self.firstTime()
    #    else:
    #        self.menu()
    
    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def printType(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(r.randrange(0, 10) / 100)
        print()
    
    def exit(self):
        self.printType("Goodbye!")
        self.save.close()
        exit()

    def wait(self, key):
        k.wait(key)
        while k.is_pressed(key):
            pass
        
        
    

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
        self.printType("There is a table with a lot of cables connected and a shotgun in the middle.")
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
    
    def drawTable(self, lifePlayer=0, lifeEnemy=0, bullets=[0,0,0,0,0,0,0,0], toolsPlayer=[0,0,0,0,0,0,0,0], toolsEnemy=[0,0,0,0,0,0,0,0]):

        toolsNames = ["", "Saw", "Cigarette", "Beer", "Magnifying glass", "Handcuffs", "Burner phone", "Expired medicine", "Adrenaline", "Inverter"]

        lifeEnemyDraw = ["☇"] * lifeEnemy + [" "] * (6 - lifeEnemy)
        lifePlayerDraw = ["☇"] * lifePlayer + [" "] * (6 - lifePlayer)

        bulletsDraw = [""] * 8

        for i in range(8):
            if bullets[i] == 1:
                bulletsDraw[i] = "▒"
            elif bullets[i] == 2:
                bulletsDraw[i] = "█"
            else:
                bulletsDraw[i] = " "
        bulletsDraw = " ".join(bulletsDraw)

        toolsPlayerNames = []
        toolsEnemyNames = []
        for i in range(8):
            toolName = toolsNames[int(toolsPlayer[i])]

            if len(toolName) < 16:
                toolName += " " * (16 - len(toolName))
            toolsPlayerNames.append(toolName)
            
            toolName = toolsNames[int(toolsEnemy[i])]

            if len(toolName) < 16:
                toolName += " " * (16 - len(toolName))
            toolsEnemyNames.append(toolName)
    


        print("┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓")
        print("┃  ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓  ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓  ┃")
        print("┃  ┃" + toolsEnemyNames[0] + "┃   ┃" + toolsEnemyNames[1] + "┃  ┃" + toolsEnemyNames[2] + "┃   ┃" + toolsEnemyNames[3] + "┃  ┃")
        print("┃  ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛  ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛  ┃")
        print("┃                                                                                    ┣╍╍╍┓")
        print("┃  ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓  ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓  ┃ " + lifeEnemyDraw[0] + " ┃")
        print("┃  ┃" + toolsEnemyNames[4] + "┃   ┃" + toolsEnemyNames[5] + "┃  ┃" + toolsEnemyNames[6] + "┃   ┃" + toolsEnemyNames[7] + "┃  ┃ " + lifeEnemyDraw[1] + " ┃")
        print("┃  ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛  ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛  ┃ " + lifeEnemyDraw[2] + " ┃")
        print("┃                                                                                    ┃ " + lifeEnemyDraw[3] + " ┃")
        print("┃                                                                                    ┃ " + lifeEnemyDraw[4] + " ┃")
        print("┃                                   ┏╍╍╍╍╍╍╍╍╍╍╍╍┓                   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┫ " + lifeEnemyDraw[5] + " ┃")
        print("┣╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┫ 0 Shotgun  ┣╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┫" + bulletsDraw + "┣╍╍╍┫")
        print("┃                                   ┗╍╍╍╍╍╍╍╍╍╍╍╍┛                   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┫ " + lifePlayerDraw[5] + " ┃")
        print("┃                                                                                    ┃ " + lifePlayerDraw[4] + " ┃")
        print("┃                                                                                    ┃ " + lifePlayerDraw[3] + " ┃")
        print("┃  ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓  ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓  ┃ " + lifePlayerDraw[2] + " ┃")
        print("┃  1" + toolsPlayerNames[0] + "┃   2" + toolsPlayerNames[1] + "┃  3" + toolsPlayerNames[2] + "┃   4" + toolsPlayerNames[3] + "┃  ┃ " + lifePlayerDraw[1] + " ┃")
        print("┃  ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛  ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛  ┃ " + lifePlayerDraw[0] + " ┃")
        print("┃                                                                                    ┣╍╍╍┛")
        print("┃  ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓  ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓   ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓  ┃")
        print("┃  5" + toolsPlayerNames[4] + "┃   6" + toolsPlayerNames[5] + "┃  7" + toolsPlayerNames[6] + "┃   8" + toolsPlayerNames[7] + "┃  ┃")
        print("┃  ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛  ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛   ┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛  ┃")
        print("┗╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┛")
    
    def rounds(self, round, normal=True):
        normal = " ☠ " if normal else "III"
        if round == 1:
            print("┏╍╍╍╍╍╍╍╍╍┳╍╍╍╍╍╍╍╍╍┳╍╍╍╍╍╍╍╍╍┓")
            print("┃  ┏╍╍╍┓  ┃         ┃         ┃")
            print("┃  ┃ I ┃  ┃   I I   ┃   " + normal + "   ┃")
            print("┃  ┗╍╍╍┛  ┃         ┃         ┃")
            print("┗╍╍╍╍╍╍╍╍╍┻╍╍╍╍╍╍╍╍╍┻╍╍╍╍╍╍╍╍╍┛")
        elif round == 2:
            print("┏╍╍╍╍╍╍╍╍╍┳╍╍╍╍╍╍╍╍╍┳╍╍╍╍╍╍╍╍╍┓")
            print("┃         ┃  ┏╍╍╍┓  ┃         ┃")
            print("┃    I    ┃  ┃I I┃  ┃   " + normal + "   ┃")
            print("┃         ┃  ┗╍╍╍┛  ┃         ┃")
            print("┗╍╍╍╍╍╍╍╍╍┻╍╍╍╍╍╍╍╍╍┻╍╍╍╍╍╍╍╍╍┛")
        elif round == 3:
            print("┏╍╍╍╍╍╍╍╍╍┳╍╍╍╍╍╍╍╍╍┳╍╍╍╍╍╍╍╍╍┓")
            print("┃         ┃         ┃  ┏╍╍╍┓  ┃")
            print("┃    I    ┃   I I   ┃  ┃" + normal + "┃  ┃")
            print("┃         ┃         ┃  ┗╍╍╍┛  ┃")
            print("┗╍╍╍╍╍╍╍╍╍┻╍╍╍╍╍╍╍╍╍┻╍╍╍╍╍╍╍╍╍┛")

    def randomBullet(self):
        bulletsBeforeSort = [r.randint(0, 2) for _ in range(8)]
        bullets = []
        while not 1 in bullets and not 2 in bullets:
            for i in bulletsBeforeSort:
                if i != 0:
                    bullets.append(i)
            for i in range(8 - len(bullets)):
                bullets.append(0)
        print(bullets)
        return bullets
    
    def shoot(self, lifePlayer, lifeEnemy, bullets, toolsPlayer, toolsEnemy, dealerKnowledge):
        self.drawTable(lifePlayer, lifeEnemy, [0,0,0,0,0,0,0,0], toolsPlayer, toolsEnemy)
        self.printType("Who do you want to shoot?")
        print("1. Yourself (when you shoot yourself, you play the next turn)")
        print("2. The dealer")

        choice = k.read_key()
        
        if choice == "1":
            if bullets[0] == 2:
                lifePlayer -= 1
                os.system("color 4")
                time.sleep(0.2)
                os.system("color 7")
                self.printType("You shot yourself.")
                dealerKnowledge[1].append(2)
            else:
                self.printType("You shot yourself but the bullet was blank.")
                dealerKnowledge[1].append(1)
            bullets.pop(0)
            played = 1
        elif choice == "2":
            if bullets[0] == 2:
                lifeEnemy -= 1
                os.system("color 4")
                time.sleep(0.2)
                os.system("color 7")
                self.printType("You shot the dealer.")
                dealerKnowledge[1].append(2)
            else:
                self.printType("You shot the dealer but the bullet was blank.")
                dealerKnowledge[1].append(1)
            bullets.pop(0)
            played = 2
        else:
            print("You decided to wait a bit.")
            k.wait("space")
            lifePlayer, lifeEnemy, bullets, toolsPlayer, toolsEnemy, dealerKnowledge, played = self.shoot(lifePlayer, lifeEnemy, bullets, toolsPlayer, toolsEnemy, dealerKnowledge)
        
        
        return lifePlayer, lifeEnemy, bullets, toolsPlayer, toolsEnemy, dealerKnowledge, played
    
    def dealerShoot(self, lifePlayer, lifeEnemy, bullets, toolsPlayer, toolsEnemy, dealerKnowledge):
        actualKnowsBulletsCounter = Counter(dealerKnowledge[0]) - Counter(dealerKnowledge[1])
        actualKnowsBullets = list(actualKnowsBulletsCounter.elements())

        if not 2 in actualKnowsBullets:
            self.printType("The dealer shot himself but the bullet was blank.")
            dealerKnowledge[1].append(1)
            bullets.pop(0)
            played = 1
        elif not 1 in actualKnowsBullets:
            self.printType("The dealer shot you")
            lifePlayer -= 1
            dealerKnowledge[1].append(2)
            bullets.pop(0)
            played = 2
        else:
            if r.randint(1, 2) == 1:
                if bullets[0] == 2:
                    lifePlayer -= 1
                    os.system("color 4")
                    time.sleep(0.2)
                    os.system("color 7")
                    time.sleep(0.2)
                    self.printType("The dealer shot you.")
                    dealerKnowledge[1].append(2)
                    bullets.pop(0)
                    played = 2
                elif bullets[0] == 1:
                    self.printType("The dealer shot you but the bullet was blank.")
                    dealerKnowledge[1].append(1)
                    bullets.pop(0)
                    played = 2
            else:
                if bullets[0] == 2:
                    lifeEnemy -= 1
                    os.system("color 4")
                    time.sleep(0.2)
                    os.system("color 7")
                    time.sleep(0.2)
                    self.printType("The dealer shot himself.")
                    dealerKnowledge[1].append(2)
                    bullets.pop(0)
                    played = 1
                elif bullets[0] == 1:
                    self.printType("The dealer shot himself but the bullet was blank.")
                    dealerKnowledge[1].append(1)
                    bullets.pop(0)
                    played = 1
        return lifePlayer, lifeEnemy, bullets, toolsPlayer, toolsEnemy, dealerKnowledge, played
        
    
    def game(self):
        self.clear()
        self.printType("Please, sign the waiver.")
        print()
        print("GENERAL RELEASE OF LIABILITY")
        print("In consideration of being allowed to participate in any way in the game, related events and activities, I the undersigned, acknowledge, appreciate, and agree that:")
        print("1. The risk of injury from the activities involved in this game is significant, including the potential for permanent paralysis and death, and while particular rules, equipment, and personal discipline may reduce this risk, the risk of serious injury does exist;")
        print("2. I KNOWINGLY AND FREELY ASSUME ALL SUCH RISKS, both known and unknown, EVEN IF ARISING FROM THE NEGLIGENCE OF THE RELEASEES or others, and assume full responsibility for my participation;")
        print("3. I willingly agree to comply with the stated and customary terms and conditions for participation. If, however, I observe any unusual significant hazard during my presence or participation, I will remove myself from participation and bring such to the attention of the nearest official immediately;")
        print("4. I, for myself and on behalf of my heirs, assigns, personal representatives and next of kin, HEREBY RELEASE AND HOLD HARMLESS the game, their officers, officials, agents, and/or employees, other participants, sponsoring agencies, sponsors, advertisers, and, if applicable, owners and lessors of premises used for the activity (RELEASEES), WITH RESPECT TO ANY AND ALL INJURY, DISABILITY, DEATH, or loss or damage to person or property, WHETHER ARISING FROM THE NEGLIGENCE OF THE RELEASEES OR OTHERWISE, to the fullest extent permitted by law.")
        print("I HAVE READ THIS RELEASE")

        playerName = input("Enter name: ")

        self.printType("He take the paper")
        k.wait("space")
        self.clear()
        self.rounds(1)
        time.sleep(2)
        self.clear()
        
        lifePlayer = 2
        lifeEnemy = 2
        
        bullets = [2,1,1,0,0,0,0,0]
        
        toolsPlayer = [0,0,0,0,0,0,0,0]
        toolsEnemy = [0,0,0,0,0,0,0,0]

        while lifePlayer != 0 and lifeEnemy != 0:
            if bullets == []:
                bullets = self.randomBullet()
            
            dealerKnowledge = [bullets, [], toolsPlayer, toolsEnemy] # [start bullets, current bullets, player tools, enemy tools]

            self.drawTable(lifePlayer, lifeEnemy, bullets, toolsPlayer, toolsEnemy)

            if bullets.count(2) == 1:
                self.printType(str(bullets.count(2)) + " live round, " + str(bullets.count(1)) + " blanks.")
            else:
                self.printType(str(bullets.count(2)) + " live rounds, " + str(bullets.count(1)) + " blanks.")
            time.sleep(3)
            self.clear()
            self.printType("dealer: I insert the bullets in an unknown order.")
            while 0 in bullets:
                bullets.remove(0)
            r.shuffle(bullets)

            while len(bullets) != 0 or lifePlayer == 0 or lifeEnemy == 0:
                played = 0
                print("Dealer knowledge: " + str(dealerKnowledge))
                print("Player knowledge: " + str([bullets, [], toolsPlayer, toolsEnemy]))
                print("Bullet knowledge: " + str(bullets))
                self.drawTable(lifePlayer, lifeEnemy, [0,0,0,0,0,0,0,0], toolsPlayer, toolsEnemy)
                print("(0 to use the shotgun)")
                k.wait("0")
                self.clear()
                self.printType("You take the shotgun.")
                while (played != 1 and bullets != []) or lifePlayer == 0 or lifeEnemy == 0:
                    lifePlayer, lifeEnemy, bullets, toolsPlayer, toolsEnemy, dealerKnowledge, played = self.shoot(lifePlayer, lifeEnemy, bullets, toolsPlayer, toolsEnemy, dealerKnowledge)
                
                    if played == 1 and bullets != []:
                        k.wait("space")
                        self.printType("You play the next turn.")
                        time.sleep(1)
                    
                    self.clear()
                
                played = 0
                print("Dealer knowledge: " + str(dealerKnowledge))
                print("Player knowledge: " + str([bullets, [], toolsPlayer, toolsEnemy]))
                print("Bullet knowledge: " + str(bullets))
                self.drawTable(lifePlayer, lifeEnemy, [0,0,0,0,0,0,0,0], toolsPlayer, toolsEnemy)
                self.printType("dealer: I take the shotgun.")
                time.sleep(1)
                self.clear()
                while (played != 2 and bullets != []) or lifePlayer == 0 or lifeEnemy == 0:
                    lifePlayer, lifeEnemy, bullets, toolsPlayer, toolsEnemy, dealerKnowledge, played = self.dealerShoot(lifePlayer, lifeEnemy, bullets, toolsPlayer, toolsEnemy, dealerKnowledge)

                    if played == 1 and bullets != []:
                        k.wait("space")
                        self.printType("The dealer play the next turn.")
                        time.sleep(1)
                    
                    self.clear()
            
            self.clear()
            self.printType("There is no more bullets.")
            time.sleep(1)
            self.printType("New bullets are comming.")






        

        



Game().game()