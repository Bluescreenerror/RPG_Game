import easygui as e
import time as t
import random as r

usr_armour = 0
usr_money = 850
usr_health = 200
ai_health = 200
ai_money = 850
ai_armour = 0
count = 0
fin = True


def buy_menu():
    # noinspection PyGlobalUndefined
    global buy
    buy = e.choicebox(
        "Choose the item you want to buy. If you don't buy anything then by default you'll equip a pistol. Press 'Esc' or 'Exit' to continue with a pistol. \n\nChoose 'info' to know more about the items.\n\nPress 'Cancel' to skip the attack .\n\nMoney you currently have is: " + "$" + str(
            usr_money), "Buy menu", items)


decision_list = ['Attack', 'Defend']
while fin is True:
    if count != 0:
        continue_play = e.buttonbox("Do you wish to continue?", "Prompt", ["Yes", "No"])
        if continue_play != "Yes":
            break
    else:
        play = e.buttonbox("Do you want to play the RPG game?", "Prompt", ["Play", "Cancel"])
        if play != "Play":
            break
    decision = e.buttonbox("What would you like to do?." + "\n\n" + "Your money: " + "$" + str(usr_money) + "\n\n" + "Your health: " + str(usr_health) + "\n\n" + "Your armour: " + str(usr_armour), "Choice", decision_list)
    if decision == "Attack":
        if usr_armour != 100:
            if usr_money <= 200:
                items = ["Info", "Exit"]
            if 250 <= usr_money < 450:
                items = ["SPAS-12 - $250", "Info", "Exit"]
            if 450 <= usr_money < 650:
                items = ["SPAS-12 - $250", "Stim shot - $450", "Info", "Exit"]
            if 650 <= usr_money <= 800:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Armour - $650", "Info", "Exit"]
            if 800 <= usr_money < 1200:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Armour - $650", "Info", "Exit"]
            if usr_money >= 1200:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Armour - $650", "Rocket Launcher - $1200", "Info", "Exit"]
        else:
            if usr_money <= 200:
                items = ["Info", "Exit"]
            if 250 <= usr_money < 450:
                items = ["SPAS-12 - $250", "Info", "Exit"]
            if 450 <= usr_money < 650:
                items = ["SPAS-12 - $250", "Stim shot - $450", "Info", "Exit"]
            if 650 <= usr_money <= 800:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Info", "Exit"]
            if 800 <= usr_money < 1200:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Info", "Exit"]
            if usr_money >= 1200:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Rocket Launcher - $1200", "Info", "Exit"]

        buy_menu()
        if buy == "Info":
            e.msgbox('''
            AK-47- 

            Damage: 8
            Armour damage: 14
            Bullet accuracy: 20%
            Magazine: 30
            Cost: $850

            SPAS-12 - 

            Damage: 60
            Armour damage: 80
            Shell accuracy: 12.5%
            Tube capacity: 9
            Cost: $200

            Rocket Launcher - 

            Damage: 120
            Armour damage: 70
            Projectile accuracy: 7.69%
            Rockets: 5
            Cost: $1200

            Berreta- 

            Damage: 8
            Armour damage: 8
            Bullet accuracy: 50%
            Magazine: 11
            Cost: N/A     
            
            Armour -
             
            Takes upto 100 damage 
            Cost: $650 
            
            Stim shot - 
            
            Adds 50HP
            Cost: $450
            
            ''')

            if usr_money <= 200:
                items = ["Exit"]
            if 250 <= usr_money < 450:
                items = ["SPAS-12 - $250", "Exit"]
            if 450 <= usr_money < 650:
                items = ["SPAS-12 - $250", "Stim shot - $450", "Exit"]
            if 650 <= usr_money <= 800:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Armour - $650", "Exit"]
            if 800 <= usr_money < 1200:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Armour - $650", "Exit"]
            if usr_money >= 1200:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Armour - $650",
                         "Rocket Launcher - $1200", "Exit"]

            buy_menu()
        if buy == "AK-47 - $800":
            usr_money = usr_money - 800
            e.msgbox("You bought an AK-47!.\n\n Money left: " + "$" + str(usr_money), "Prompt")
            t.sleep(0.5)
            e.msgbox("Attacking...", "Prompt")
            shot = 0
            for i in range(30):
                a = r.randint(0, 3)
                if a == 0:
                    shot = shot + 1
            if ai_armour > 0:
                if 14 * shot > ai_armour:
                    ai_armour = 0
                    damage = 14 * shot - ai_armour
                    ai_health = ai_health - damage
                else:
                    ai_armour = ai_armour - 14 * shot
            else:
                ai_health = ai_health - 9 * shot

            t.sleep(1)
            e.msgbox("Attack complete!", "Prompt")
            e.msgbox(
                "Damage given: " + str(9 * shot) + "\n\n" + "AI health: " + str(
                    ai_health) + "\n\n" + "Accuracy: " + str(
                    shot / 30 * 100) + "%" + "\n\n" + "Hits: " + str(shot) + "\n\n" + "Money Gained: " + "$" + str(
                    40 * shot),
                "Prompt")
            usr_money = usr_money + 40 * shot

        if buy == "SPAS-12 - $250":
            shot = 0
            usr_money = usr_money - 250
            e.msgbox("You bought a SPAS-12!.\n\n Money left: " + "$" + str(usr_money) + "\n\n", "Prompt")
            t.sleep(0.5)
            e.msgbox("Attacking...", "Prompt")
            for i in range(0, 9):
                a = r.randint(0, 7)
                if a == 1:
                    shot = shot + 1

            if ai_armour > 0:
                if 80 * shot > ai_armour:
                    ai_armour = 0
                    damage = 80 * shot - ai_armour
                    ai_health = ai_health - damage
                else:
                    ai_armour = ai_armour - 80 * shot
            else:
                ai_health = ai_health - 60 * shot

            t.sleep(1)
            e.msgbox("Attack complete!", "Prompt")
            e.msgbox(
                "Damage given: " + str(60 * shot) + "\n\n" + "AI health: " + str(
                    ai_health) + "\n\n" + "Accuracy: " + str(
                    shot / 9 * 100) + "%" + "\n\n" + "Hits: " + str(shot) + "\n\n" + "Money Gained: " + "$" + str(
                    300 * shot),
                "Prompt")
            usr_money = usr_money + 300 * shot

        if buy == "Rocket Launcher - $1200":
            usr_money = usr_money - 1200
            e.msgbox("You bought the Launcher!.\n\n Money left: " + "$" + str(usr_money), "Prompt")
            t.sleep(0.5)
            e.msgbox("Attacking...", "Prompt")
            shot = 0
            for i in range(5):
                a = r.randint(0, 17)
                if a == 0:
                    shot = shot + 1
            if ai_armour > 0:
                if 120 * shot > ai_armour:
                    ai_armour = 0
                    damage = 120 * shot - ai_armour
                    ai_health = ai_health - damage
                else:
                    ai_armour = ai_armour - 120 * shot
            else:
                ai_health = ai_health - 120 * shot

            t.sleep(1)
            e.msgbox("Attack complete!", "Prompt")
            e.msgbox(
                "Damage given: " + str(120 * shot) + "\n\n" + "AI health: " + str(
                    ai_health) + "\n\n" + "Accuracy: " + str(
                    shot / 5 * 100) + "%" + "\n\n" + "Hits: " + str(shot) + "\n\n" + "Money Gained: " + "$" + str(
                    600 * shot),
                "Prompt")
            usr_money = usr_money + 120 * shot

        if buy == "Exit":
            e.msgbox("You're using pistol", "Prompt")
            t.sleep(0.5)
            e.msgbox("Attacking...", "Prompt")
            shot = 0
            for i in range(0, 17):
                a = r.randint(0, 1)
                if a == 0:
                    shot = shot + 1
            if ai_armour > 0:
                if 8 * shot > ai_armour:
                    ai_armour = 0
                    damage = 8 * shot - ai_armour
                    ai_health = ai_health - damage
                else:
                    ai_armour = ai_armour - 8 * shot
            else:
                ai_health = ai_health - 8 * shot

            t.sleep(1)
            e.msgbox("Attack complete!", "Prompt")
            e.msgbox(
                "Damage given: " + str(8 * shot) + "\n\n" + "AI health: " + str(
                    ai_health) + "\n\n" + "Accuracy: " + str(
                    shot / 17 * 100) + "%" + "\n\n" + "Hits: " + str(shot) + "\n\n" + "Money Gained: " + "$" + str(
                    80 * shot),
                "Prompt")
            usr_money = usr_money + 80 * shot

        if buy == "Armour - $650":
            usr_money = usr_money - 650
            e.msgbox("You bought an Armour!.\n\n Money left: " + "$" + str(usr_money), "Prompt")
            usr_armour = usr_armour + 100
            e.msgbox("Your armour: " + str(usr_armour), "Prompt")

        if buy == "Stim shot - $450":
            usr_money = usr_money - 450
            e.msgbox("You used a Stim shot!.\n\nMoney left: " + "$" + str(usr_money), "Prompt")
            usr_health = usr_health + 50

        if ai_health <= 0:
            e.msgbox("You killed the enemy!" + "\n\n" + "You won!")
            fin = False
            break

        if ai_money < 250:
            ai_items = ["Beretta"]
            ai_weapon = "Beretta"
        if 250 <= ai_money < 450:
            ai_items = ["SPAS-12", "Beretta"]
            x = r.randint(0, 1)
            ai_weapon = ai_items[x]
        if 450 <= ai_money < 650:
            ai_items = ["SPAS-12", "Beretta", "Stim shot"]
            x = r.randint(0, 2)
            ai_weapon = ai_items[x]
        if 650 <= ai_money < 800:
            ai_items = ["SPAS-12", "Armour", "Beretta", "Stim shot"]
            x = r.randint(0, 3)
            ai_weapon = ai_items[x]
        if 800 <= ai_money < 1200:
            ai_items = ["AK-47", "SPAS-12", "Armour", "Beretta", "Stim shot"]
            x = r.randint(0, 4)
            ai_weapon = ai_items[x]
        if ai_money > 1200:
            ai_items = ["AK-47", "SPAS-12", "Armour", "Beretta", "Rocket Launcher", "Stim shot"]
            x = r.randint(0, 5)
            ai_weapon = ai_items[x]

        t.sleep(0.8)

        e.msgbox("Enemy's turn!", "Prompt")
        t.sleep(1)
        e.msgbox("Enemy is bought a/an : " + str(ai_weapon) + "\n\n", "Prompt")

        if ai_weapon == "AK-47":
            ai_money = ai_money - 800
            e.msgbox("Enemy is Attacking...", "Prompt")
            shot = 0
            for i in range(30):
                a = r.randint(0, 3)
                if a == 0:
                    shot = shot + 1
            if usr_armour > 0:
                if 9 * shot > usr_armour:
                    usr_armour = 0
                    damage = 9 * shot - usr_armour
                    usr_health = usr_health - damage
                else:
                    usr_armour = usr_armour - 9 * shot
            else:
                usr_health = usr_health - 9 * shot

            t.sleep(1)
            e.msgbox("Attack complete!", "Prompt")
            e.msgbox(
                "Damage taken: " + str(9 * shot) + "\n\n" + "Your health: " + str(
                    usr_health) + "\n\n" + "Accuracy: " + str(
                    shot / 30 * 100) + "%" + "\n\n" + "Hits: " + str(
                    shot) + "\n\n" + "Money Gained by enemy: " + "$" + str(40 * shot), "Prompt")
            ai_money = ai_money + 40 * shot

        if ai_weapon == "SPAS-12":
            ai_money = ai_money - 200
            e.msgbox("Enemy is Attacking...", "Prompt")
            shot = 0
            for i in range(0, 9):
                a = r.randint(0, 7)
                if a == 1:
                    shot = shot + 1
            if usr_armour > 0:
                if 80 * shot > usr_armour:
                    usr_armour = 0
                    damage = 80 * shot - usr_armour
                    usr_health = usr_health - damage
                else:
                    usr_armour = usr_armour - 80 * shot
            else:
                usr_health = usr_health - 60 * shot

            t.sleep(1)
            e.msgbox("Attack complete!", "Prompt")
            e.msgbox("Damage taken: " + str(60 * shot) + "\n\n" + "Your health: " + str(
                usr_health) + "\n\n" + "Accuracy: " + str(
                shot / 9 * 100) + "%" + "\n\n" + "Hits: " + str(shot) + "\n\n" + "Money Gained by enemy: " + "$" + str(
                300 * shot), "Prompt")
            ai_money = ai_money + 300 * shot

        if ai_weapon == "Rocket Launcher":
            ai_money = ai_money - 1200
            e.msgbox("Enemy is Attacking...", "Prompt")
            shot = 0
            for i in range(5):
                a = r.randint(0, 17)
                if a == 0:
                    shot = shot + 1
            if usr_armour > 0:
                if 70 * shot > usr_armour:
                    usr_armour = 0
                    damage = 70 * shot - usr_armour
                    usr_health = usr_health - damage
                else:
                    usr_armour = usr_armour - 70 * shot
            else:
                usr_health = usr_health - 120 * shot

            t.sleep(1)

            e.msgbox("Attack complete!", "Prompt")
            e.msgbox("Damage taken: " + str(120 * shot) + "\n\n" + "Your health: " + str(
                usr_health) + "\n\n" + "Accuracy: " + str(
                shot / 5 * 100) + "%" + "\n\n" + "Hits: " + str(shot) + "\n\n" + "Money Gained by enemy: " + "$" + str(
                600 * shot), "Prompt")
            ai_money = ai_money + 600 * shot

        if ai_weapon == "Beretta":
            e.msgbox("Enemy is Attacking...", "Prompt")
            shot = 0
            for i in range(0, 17):
                a = r.randint(0, 1)
                if a == 0:
                    shot = shot + 1
            if usr_armour > 0:
                if 8 * shot > usr_armour:
                    usr_armour = 0
                    damage = 8 * shot - usr_armour
                    usr_health = usr_health - damage
                else:
                    usr_armour = usr_armour - 8 * shot
            else:
                usr_health = usr_health - 8 * shot

            t.sleep(1)

            e.msgbox("Attack complete!", "Prompt")
            e.msgbox("Damage taken: " + str(8 * shot) + "\n\n" + "Your health: " + str(
                usr_health) + "\n\n" + "Accuracy: " + str(
                shot / 17 * 100) + "%" + "\n\n" + "Hits: " + str(shot) + "\n\n" + "Money Gained by enemy: " + "$" + str(
                80 * shot), "Prompt")
            ai_money = ai_money + 80 * shot

        if ai_weapon == "Armour":
            ai_money = ai_money - 650
            ai_armour = ai_armour + 100

        if ai_weapon == "Stim shot":
            usr_money = usr_money - 450
            e.msgbox("You used a Stim shot!.\n\nMoney left: " + "$" + str(usr_money), "Prompt")
            usr_health = usr_health + 50

        if usr_health <= 0:
            e.msgbox("Enemy killed you!" + "\n\n" + "You lost!")
            fin = False
            break

        e.msgbox("Money left with AI: " + "$" + str(ai_money) + "\t\t" "|" "\t\t" + "Money left with you: " + "$" + str(
            usr_money) + "\n\n" "AI health: " + str(ai_health) + "\t\t" "|" "\t" + "Your health: " + str(
            usr_health) + "\n\n" + "AI armour: " + str(ai_armour) + "\t\t" "|" "\t" + "Your armour: " + str(usr_armour))
        count = count + 1

    else:
        e.msgbox("Enemy's turn!", "Prompt")

        if ai_money < 250:
            ai_items = ["Beretta"]
            ai_weapon = "Beretta"
        if 250 <= ai_money < 450:
            ai_items = ["SPAS-12", "Beretta"]
            x = r.randint(0, 1)
            ai_weapon = ai_items[x]
        if 450 <= ai_money < 650:
            ai_items = ["SPAS-12", "Beretta", "Stim shot"]
            x = r.randint(0, 2)
            ai_weapon = ai_items[x]
        if 650 <= ai_money < 800:
            ai_items = ["SPAS-12", "Armour", "Beretta", "Stim shot"]
            x = r.randint(0, 3)
            ai_weapon = ai_items[x]
        if 800 <= ai_money < 1200:
            ai_items = ["AK-47", "SPAS-12", "Armour", "Beretta", "Stim shot"]
            x = r.randint(0, 4)
            ai_weapon = ai_items[x]
        if ai_money >= 1200:
            ai_items = ["AK-47", "SPAS-12", "Armour", "Beretta", "Rocket Launcher", "Stim shot"]
            x = r.randint(0, 5)
            ai_weapon = ai_items[x]

        e.msgbox("Enemy is bought a/an : " + str(ai_weapon) + "\n\n", "Prompt")

        if ai_weapon == "AK-47":
            ai_money = ai_money - 800
            e.msgbox("Enemy is Attacking...", "Prompt")
            shot = 0
            for i in range(30):
                a = r.randint(0, 3)
                if a == 0:
                    shot = shot + 1
            if usr_armour > 0:
                if 9 * shot > usr_armour:
                    usr_armour = 0
                    damage = 9 * shot - usr_armour
                    usr_health = usr_health - damage
                else:
                    usr_armour = usr_armour - 9 * shot
            else:
                usr_health = usr_health - 9 * shot

            t.sleep(1)
            e.msgbox("Attack complete!", "Prompt")
            e.msgbox(
                "Damage taken: " + str(9 * shot) + "\n\n" + "Your health: " + str(
                    usr_health) + "\n\n" + "Accuracy: " + str(
                    shot / 30 * 100) + "%" + "\n\n" + "Hits: " + str(
                    shot) + "\n\n" + "Money Gained by enemy: " + "$" + str(40 * shot), "Prompt")
            ai_money = ai_money + 40 * shot

        if ai_weapon == "SPAS-12":
            ai_money = ai_money - 250
            e.msgbox("Enemy is Attacking...", "Prompt")
            shot = 0
            for i in range(0, 9):
                a = r.randint(0, 7)
                if a == 1:
                    shot = shot + 1
            if usr_armour > 0:
                if 80 * shot > usr_armour:
                    usr_armour = 0
                    damage = 80 * shot - usr_armour
                    usr_health = usr_health - damage
                else:
                    usr_armour = usr_armour - 80 * shot
            else:
                usr_health = usr_health - 60 * shot

            t.sleep(1)
            e.msgbox("Attack complete!", "Prompt")
            e.msgbox("Damage taken: " + str(60 * shot) + "\n\n" + "Your health: " + str(
                usr_health) + "\n\n" + "Accuracy: " + str(
                shot / 9 * 100) + "%" + "\n\n" + "Hits: " + str(shot) + "\n\n" + "Money Gained by enemy: " + "$" + str(
                300 * shot), "Prompt")
            ai_money = ai_money + 300 * shot

        if ai_weapon == "Rocket Launcher":
            ai_money = ai_money - 1200
            e.msgbox("Enemy is Attacking...", "Prompt")
            shot = 0
            for i in range(5):
                a = r.randint(0, 17)
                if a == 0:
                    shot = shot + 1
            if usr_armour > 0:
                if 70 * shot > usr_armour:
                    usr_armour = 0
                    damage = 70 * shot - usr_armour
                    usr_health = usr_health - damage
                else:
                    usr_armour = usr_armour - 70 * shot
            else:
                usr_health = usr_health - 120 * shot

            t.sleep(1)

            e.msgbox("Attack complete!", "Prompt")
            e.msgbox("Damage taken: " + str(120 * shot) + "\n\n" + "Your health: " + str(
                usr_health) + "\n\n" + "Accuracy: " + str(
                shot / 5 * 100) + "%" + "\n\n" + "Hits: " + str(shot) + "\n\n" + "Money Gained by enemy: " + "$" + str(
                600 * shot), "Prompt")
            ai_money = ai_money + 600 * shot

        if ai_weapon == "Beretta":
            e.msgbox("Enemy is Attacking...", "Prompt")
            shot = 0
            for i in range(0, 17):
                a = r.randint(0, 1)
                if a == 0:
                    shot = shot + 1
            if usr_armour > 0:
                if 8 * shot > usr_armour:
                    usr_armour = 0
                    damage = 8 * shot - usr_armour
                    usr_health = usr_health - damage
                else:
                    usr_armour = usr_armour - 8 * shot
            else:
                usr_health = usr_health - 8 * shot

            t.sleep(1)

            e.msgbox("Attack complete!", "Prompt")
            e.msgbox("Damage taken: " + str(8 * shot) + "\n\n" + "Your health: " + str(
                usr_health) + "\n\n" + "Accuracy: " + str(
                shot / 17 * 100) + "%" + "\n\n" + "Hits: " + str(shot) + "\n\n" + "Money Gained by enemy: " + "$" + str(
                80 * shot), "Prompt")
            ai_money = ai_money + 80 * shot

        if ai_weapon == "Armour":
            ai_money = ai_money - 650
            ai_armour = ai_armour + 100

        if ai_weapon == "Stim shot":
            ai_money = ai_money - 450
            ai_health = ai_health + 50

        if usr_health <= 0:
            e.msgbox("Enemy killed you!" + "\n\n" + "You lost!")
            fin = False
            break

        t.sleep(1)

        e.msgbox("Your turn!", "Prompt")

        if usr_armour != 100:
            if usr_money <= 200:
                items = ["Info", "Exit"]
            if 250 <= usr_money < 450:
                items = ["SPAS-12 - $250", "Info", "Exit"]
            if 450 <= usr_money < 650:
                items = ["SPAS-12 - $250", "Stim shot - $450", "Info", "Exit"]
            if 650 <= usr_money <= 800:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Armour - $650", "Info", "Exit"]
            if 800 <= usr_money < 1200:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Armour - $650", "Info", "Exit"]
            if usr_money >= 1200:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Armour - $650", "Rocket Launcher - $1200", "Info", "Exit"]
        else:
            if usr_money <= 200:
                items = ["Info", "Exit"]
            if 250 <= usr_money < 450:
                items = ["SPAS-12 - $250", "Info", "Exit"]
            if 450 <= usr_money < 650:
                items = ["SPAS-12 - $250", "Stim shot - $450", "Info", "Exit"]
            if 650 <= usr_money <= 800:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Info", "Exit"]
            if 800 <= usr_money < 1200:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Info", "Exit"]
            if usr_money >= 1200:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Rocket Launcher - $1200", "Info", "Exit"]

        buy_menu()

        if buy == "Info":
            e.msgbox('''
                       AK-47- 

                       Damage: 8
                       Armour damage: 14
                       Bullet accuracy: 20%
                       Magazine: 30
                       Cost: $850

                       SPAS-12 - 

                       Damage: 60
                       Armour damage: 80
                       Shell accuracy: 12.5%
                       Tube capacity: 9
                       Cost: $200

                       Rocket Launcher - 

                       Damage: 120
                       Armour damage: 70
                       Projectile accuracy: 7.69%
                       Rockets: 5
                       Cost: $1200

                       Berreta- 

                       Damage: 8
                       Armour damage: 8
                       Bullet accuracy: 50%
                       Magazine: 11
                       Cost: N/A     

                       Armour -

                       Takes upto 100 damage 
                       Cost: $650 

                       Stim shot - 

                       Adds 50HP
                       Cost: $450

                       ''')

            if usr_money <= 200:
                items = ["Exit"]
            if 250 <= usr_money < 450:
                items = ["SPAS-12 - $250", "Exit"]
            if 450 <= usr_money < 650:
                items = ["SPAS-12 - $250", "Stim shot - $450", "Exit"]
            if 650 <= usr_money <= 800:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Armour - $650", "Exit"]
            if 800 <= usr_money < 1200:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Armour - $650", "Exit"]
            if usr_money >= 1200:
                items = ["AK-47 - $800", "SPAS-12 - $250", "Stim shot - $450", "Armour - $650",
                         "Rocket Launcher - $1200", "Exit"]

            buy_menu()

        if buy == "AK-47 - $800":
            usr_money = usr_money - 800
            e.msgbox("You bought an AK-47!.\n\n Money left: " + "$" + str(usr_money), "Prompt")
            t.sleep(0.5)
            e.msgbox("Attacking...", "Prompt")
            shot = 0
            for i in range(30):
                a = r.randint(0, 3)
                if a == 0:
                    shot = shot + 1
            if ai_armour > 0:
                if 14 * shot > ai_armour:
                    ai_armour = 0
                    damage = 14 * shot - ai_armour
                    ai_health = ai_health - damage
                else:
                    ai_armour = ai_armour - 14 * shot
            else:
                ai_health = ai_health - 9 * shot

            t.sleep(1)
            e.msgbox("Attack complete!", "Prompt")
            e.msgbox(
                "Damage given: " + str(9 * shot) + "\n\n" + "AI health: " + str(
                    ai_health) + "\n\n" + "Accuracy: " + str(
                    shot / 30 * 100) + "%" + "\n\n" + "Hits: " + str(shot) + "\n\n" + "Money Gained: " + "$" + str(
                    40 * shot),
                "Prompt")
            usr_money = usr_money + 40 * shot

        if buy == "SPAS-12 - $250":
            shot = 0
            usr_money = usr_money - 250
            e.msgbox("You bought a SPAS-12!.\n\n Money left: " + "$" + str(usr_money) + "\n\n", "Prompt")
            t.sleep(0.5)
            e.msgbox("Attacking...", "Prompt")
            for i in range(0, 9):
                a = r.randint(0, 7)
                if a == 1:
                    shot = shot + 1

            if ai_armour > 0:
                if 80 * shot > ai_armour:
                    ai_armour = 0
                    damage = 80 * shot - ai_armour
                    ai_health = ai_health - damage
                else:
                    ai_armour = ai_armour - 80 * shot
            else:
                ai_health = ai_health - 60 * shot

            t.sleep(1)
            e.msgbox("Attack complete!", "Prompt")
            e.msgbox(
                "Damage given: " + str(60 * shot) + "\n\n" + "AI health: " + str(
                    ai_health) + "\n\n" + "Accuracy: " + str(
                    shot / 9 * 100) + "%" + "\n\n" + "Hits: " + str(shot) + "\n\n" + "Money Gained: " + "$" + str(
                    300 * shot),
                "Prompt")
            usr_money = usr_money + 300 * shot

        if buy == "Rocket Launcher - $1200":
            usr_money = usr_money - 1200
            e.msgbox("You bought the Launcher!.\n\n Money left: " + "$" + str(usr_money), "Prompt")
            t.sleep(0.5)
            e.msgbox("Attacking...", "Prompt")
            shot = 0
            for i in range(5):
                a = r.randint(0, 17)
                if a == 0:
                    shot = shot + 1
            if ai_armour > 0:
                if 120 * shot > ai_armour:
                    ai_armour = 0
                    damage = 120 * shot - ai_armour
                    ai_health = ai_health - damage
                else:
                    ai_armour = ai_armour - 120 * shot
            else:
                ai_health = ai_health - 120 * shot

            t.sleep(1)
            e.msgbox("Attack complete!", "Prompt")
            e.msgbox(
                "Damage given: " + str(120 * shot) + "\n\n" + "AI health: " + str(
                    ai_health) + "\n\n" + "Accuracy: " + str(
                    shot / 5 * 100) + "%" + "\n\n" + "Hits: " + str(shot) + "\n\n" + "Money Gained: " + "$" + str(
                    600 * shot),
                "Prompt")
            usr_money = usr_money + 120 * shot

        if buy == "Exit":
            e.msgbox("You're using pistol", "Prompt")
            t.sleep(0.5)
            e.msgbox("Attacking...", "Prompt")
            shot = 0
            for i in range(0, 17):
                a = r.randint(0, 1)
                if a == 0:
                    shot = shot + 1
            if ai_armour > 0:
                if 8 * shot > ai_armour:
                    ai_armour = 0
                    damage = 8 * shot - ai_armour
                    ai_health = ai_health - damage
                else:
                    ai_armour = ai_armour - 8 * shot
            else:
                ai_health = ai_health - 8 * shot

            t.sleep(1)
            e.msgbox("Attack complete!", "Prompt")
            e.msgbox(
                "Damage given: " + str(8 * shot) + "\n\n" + "AI health: " + str(
                    ai_health) + "\n\n" + "Accuracy: " + str(
                    shot / 17 * 100) + "%" + "\n\n" + "Hits: " + str(shot) + "\n\n" + "Money Gained: " + "$" + str(
                    80 * shot),
                "Prompt")
            usr_money = usr_money + 80 * shot

        if buy == "Armour - $650":
            usr_money = usr_money - 650
            e.msgbox("You bought an Armour!.\n\n Money left: " + "$" + str(usr_money), "Prompt")
            usr_armour = usr_armour + 100
            e.msgbox("Your armour: " + str(usr_armour), "Prompt")

        if buy == "Stim shot - $450":
            usr_money = usr_money - 450
            e.msgbox("You used a Stim shot!.\n\nMoney left: " + "$" + str(usr_money), "Prompt")
            usr_health = usr_health + 50

        if ai_health <= 0:
            e.msgbox("You killed the enemy!" + "\n\n" + "You won!")
            fin = False
            break

        e.msgbox("Money left with AI: " + "$" + str(ai_money) + "\t\t" "|" "\t\t" + "Money left with you: " + "$" + str(
            usr_money) + "\n\n" "AI health: " + str(ai_health) + "\t\t" "|" "\t" + "Your health: " + str(
            usr_health) + "\n\n" + "AI armour: " + str(ai_armour) + "\t\t" "|" "\t" + "Your armour: " + str(usr_armour))
        count = count + 1