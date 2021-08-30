import random as r
import time as t
from datetime import datetime

from tkinter import *
import threading

def sleep_time(sleeping):
    while(sleeping >= 0):
        label_TimerDATA.config(text=f"{sleeping} second(s) left.")
        sleeping -= 1
        t.sleep(1)

def Activity_Set(update_status, update_details, activity, sleeping):
    label_CallStack_name.config(text=f"[{activity}]")
    label_CallStack_details.config(text=f"> {sleeping} seconds.")
    print(f"[] > [{activity}] > [{sleeping} seconds]")
    Update(f"{update_status}", f"{update_details}")
    sleep_time(sleeping)
    Lobby()

#######################################################################
#################  BATTLE [Side Story] REQUIREMENTS  ##################
#######################################################################
def Event_Pick_Activity():
    option = r.randint(1,100)
    if(option <= 100):
        sleeping = r.randint(120, 200)
        Activity_Set("The Order of The Sword and The Lord of Summer", "Side Story", "The Order of The Sword and The Lord of Summer", sleeping)

def Side_Story_Pick_Activity():
    option = r.randint(1, 100)
    
    if(option <= 50):
        sleeping = r.randint(500, 1000)
        Activity_Set("Unrecorded History", "Side Story", "Unrecorded History", sleeping)
    
    elif(option <= 100 and option > 50):
        Event_Pick_Activity()

#######################################################################
################# [Spirit Altar] and [Hunt] REQUIREMENTS ##############
#######################################################################
def Timed_Stage(times, current, stage_name):
    while(current <= times):
        sleeping = r.randint(60, 90)
        label_CallStack_name.config(text=f"[{stage_name}]")
        print(f"[Activity] > [Repeat {stage_name} {current}/{times}] > [{sleeping} seconds]")
        Update(f"Repeat {current}/{times}", f"Auto {stage_name}")
        current+=1
        sleep_time(sleeping)
    Lobby()

#######################################################################
################  BATTLE [Spirit Altar] REQUIREMENTS  #################
#######################################################################
def Spirit_Altar_Pick_Activity():    
    now = datetime.now()
    altar= ["Dark Altar", "Fire Altar", "Frost Altar", "Forest Altar", "Light Altar"]
    current_hour = int(now.strftime("%H"))
    current_day = now.strftime("%A")
    
    if(current_hour >= 0 and current_hour < 6):
    
        if(current_day == "Monday"):
            # Sunday -> Weekend
            current_altar = altar[r.randint(0,4)]
        
        elif(current_day == "Tuesday"):
            # Monday
            current_altar = altar[0]
        
        elif(current_day == "Wednesday"):
            # Tuesday
            current_altar = altar[1]
        
        elif(current_day == "Thursday"):
            # Wednesday
            current_altar = altar[2]
        
        elif(current_day == "Friday"):
            # Thursday
            current_altar = altar[3]
        
        elif(current_day == "Saturday"):
            # Friday
            current_altar = altar[4]

        elif(current_day == "Sunday"):
            # Saturday -> Weekend
            current_altar = altar[r.randint(0,4)]

    if(current_hour >= 6 and current_hour < 24):
        if(current_day == "Monday"):
            # Monday
            current_altar = altar[0]
        
        elif(current_day == "Tuesday"):
            # Tuesday
            current_altar = altar[1]

        elif(current_day == "Wednesday"):
            # Wednesday
            current_altar = altar[2]

        elif(current_day == "Thursday"):
            # Thursday
            current_altar = altar[3]
        
        elif(current_day == "Friday"):
            # Friday
            current_altar = altar[4]
        
        elif(current_day == "Saturday"):
            # Saturday -> Weekend
            current_altar = altar[r.randint(0,4)]
        
        elif(current_day == "Sunday"):
            # Sunday -> Weekend
            current_altar = altar[r.randint(0,4)]

    print(f"current day: [{current_day}] hour [{current_hour}] -> slected altar [{current_altar}]")
    times = r.randint(1,20)
    current = 1

    Timed_Stage(times, current, current_altar)
    Lobby()
#######################################################################
####################  BATTLE [Hunt] REQUIREMENTS  #####################
#######################################################################
def Hunt_Pick_Activity():
    option = r.randint(1,100)
    times = r.randint(1,20)
    current = 1

    if (option <= 30):
        Timed_Stage(times, current, "Wyvern Hunt")

    elif (option <= 40 and option >30):
        Timed_Stage(times, current, "Golem Hunt")
    
    elif (option <= 70 and option > 40):
        Timed_Stage(times, current, "Banshee Hunt")
    
    elif (option <= 85 and option > 70):
        Timed_Stage(times, current, "Azimanak Hunt")
    
    elif (option <100 and option >85):
        Timed_Stage(times, current, "Caides Hunt")

#######################################################################
#################  BATTLE [Labirinth] REQUIREMENTS  ###################
#######################################################################
def Azmakalis_Pick_Activity():
    option = r.randint(1,100)

    if (option <= 60):
        sleeping = r.randint(300, 600)
        Activity_Set("Normal Raid", "Azmakalis", "Normal Raid", sleeping)
    
    elif(option <= 100 and option > 60):
        sleeping = r.randint(300,600)
        Activity_Set("Hell Raid", "Azmakalis", "Hell Raid", sleeping)

def Labirinth_Pick_Activity():
    option = r.randint(1, 100)
    
    if (option <= 25):
       sleeping = r.randint(300, 600)
       Activity_Set("Tirel Castle", "Labirinth", "Tirel Castle", sleeping)
    
    elif (option <= 50 and option > 25):
        sleeping = r.randint(300, 600)
        Activity_Set("Great Frache", "Labirinth", "Great Frache", sleeping)
    
    elif (option <= 75 and option > 50):
        sleeping = r.randint(300, 600)
        Activity_Set("Nixied's Sanctum", "Labirinth", "Nixied's Sanctum", sleeping)
    
    elif (option <= 100 and option > 75):
        Azmakalis_Pick_Activity()

#######################################################################
#######################  BATTLE REQUIREMENTS  #########################
#######################################################################
def Battle_Pick_Activity():
    option = r.randint(1,100)
    if(option <= 10):
        # Side Story
        Side_Story_Pick_Activity() #####
    
    elif(option <= 40 and option > 10):
        # Spirit Altar
        Spirit_Altar_Pick_Activity() ####

    elif(option <= 45 and option > 40):
        sleeping = r.randint(200, 400)
        Activity_Set("Abyss", "Battle", "Abyss", sleeping)
    
    elif(option <= 85 and option > 40):
        # Hunt
        Hunt_Pick_Activity() ####
    
    elif(option <= 90 and option > 85):
        # Labirinth
        Labirinth_Pick_Activity() ####
    
    elif(option <= 95 and option > 90):
        sleeping = r.randint(120, 300)
        Activity_Set("Automaton Tower", "Battle", "Automaton Tower", sleeping)
    
    elif(option <= 100 and option > 95):
        sleeping = r.randint(120, 180)
        Activity_Set("Hall of Trials", "Battle", "Hall of Trials", sleeping)

#######################################################################
#####################  ADVENTURE REQUIREMENTS  ########################
#######################################################################
def Adventure_Pick_Activity():
    option = r.randint(1,100)

    if(option <= 10):
        sleeping = r.randint(500,1000)
        Activity_Set("Heir of the Covenant", "Adventure", "Heir of the Covenant", sleeping)
    
    elif(option <= 20 and option > 10):
        sleeping = r.randint(500, 1000)
        Activity_Set("Godkiller", "Adventure", "Godkiller", sleeping)
    
    elif(option <= 100 and option > 20):
        sleeping = r.randint(500, 1000)
        Activity_Set("Hymn of a Wailing Tundra", "Adventure", "Hymn of a Wailing Tundra", sleeping)

#######################################################################
#########   SANCTUARY [Alchemist's Steple] REQUIREMENTS  ##############
#######################################################################
def Alchemist_Steple_Pick_Activity():
    option = r.randint(1,100)

    if(option <= 12):
        sleeping = r.randint(100,300)
        Activity_Set("Charm Crafting", "Achemist's Steple", "Charm Crafting", sleeping)
    
    elif(option <= 54 and option >12):
        sleeping = r.randint(100,300)
        Activity_Set("Material Crafting", "Achemist's Steple", "Material Crafting", sleeping)

    elif(option <= 64 and option >54):
        sleeping = r.randint(100,300)
        Activity_Set("Equipment Conversion", "Achemist's Steple", "Equipment Conversion", sleeping)
 
    elif(option <= 76 and option >64):
        sleeping = r.randint(100,300)
        Activity_Set("Catalyst Conversion", "Achemist's Steple", "Catalyst Conversion", sleeping)
     
    elif(option <= 88 and option >76):
        sleeping = r.randint(100,300)
        Activity_Set("Exclusive Equipment", "Achemist's Steple", "Exclusive Equipment", sleeping)
     
    elif(option <= 100 and option >88):
        sleeping = r.randint(100,300)
        Activity_Set("Modification Gem", "Achemist's Steple", "Modification Gem", sleeping)
 
#######################################################################
##########   SANCTUARY [Steel Workshop] REQUIREMENTS  #################
#######################################################################
def Steel_Workshop_Pick_Activity():
    option = r.randint(1,100)

    if(option <= 50):
        sleeping = r.randint(100,300)
        Activity_Set("Crafting", "Steel Workshop", "Crafting", sleeping)
    
    elif(option <= 100 and option >50):
        sleeping = r.randint(100,300)
        Activity_Set("Reforging", "Steel Workshop", "Reforging", sleeping)

#######################################################################
##################    SANCTUARY REQUIREMENTS   ########################
#######################################################################
def Sanctuary_Pick_Activity():
    option = r.randint(1,100)

    if(option <= 10):
        sleeping = r.randint(100, 300)
        Activity_Set("High Command", "Sanctuary", "High Command", sleeping)
    
    elif(option <= 20 and option > 10):
        sleeping = r.randint(100, 300)
        Activity_Set("Forest of Souls", "Sanctuary", "Forest of Souls", sleeping)
    
    elif(option <= 30 and option > 20):
        sleeping = r.randint(100, 300)
        Activity_Set("Heart of Orbis", "Sanctuary", "Heart of Orbis", sleeping)

    elif(option <= 65 and option > 30):
        Alchemist_Steple_Pick_Activity()

    elif(option <= 100 and option > 65):
        Steel_Workshop_Pick_Activity()

#######################################################################
####################    ARENA REQUIREMENTS   ##########################
#######################################################################
def Arena_Pick_Activity():
    option = r.randint(1,100)
    
    if(option <= 50):
        sleeping = r.randint(100, 300)
        Activity_Set("Arena", "Arena", "Arena", sleeping)
    
    elif(option <= 90 and option > 50):
        sleeping = r.randint(100, 300)
        Activity_Set("World Arena", "Arena", "World Arena", sleeping)
    
    elif(option <= 100 and option > 90):
        sleeping = r.randint(100, 300)
        Activity_Set("NPC Challenge", "Arena", "NPC Challenge", sleeping)

#######################################################################
######################        ARENA       #############################
#######################################################################
def Pick_Activity():
    option = r.randint(1,100)
    if(option <= 40):
        print("(Battle 40% ?)")
        Battle_Pick_Activity()

    elif(option <= 60 and option > 40):
        print("(Adventure 20% ?)")
        Adventure_Pick_Activity()

    elif(option <= 80 and option > 60):
        print("(Sanctuary 20% ?)")
        Sanctuary_Pick_Activity()

    elif(option <= 85 and option > 80):
        print("(Arena 5% ?)")
        Arena_Pick_Activity()

    elif(option <= 88 and option > 85):
        print("(Inventory 3% ?)")
        sleeping = r.randint(40, 200)
        Activity_Set("Browsing Inventory", "In Lobby", "Browsing Inventory", sleeping)

    elif(option <= 90 and option > 88):
        print("(Shop 2% ?)")
        sleeping = r.randint(40, 200)
        Activity_Set("Browsing Shop", "In Lobby", "Browsing Shop", sleeping)

    elif(option <= 92 and option > 90):
        print("(Heroes 2% ?)")
        sleeping = r.randint(40, 200)
        Activity_Set("Browsing Heroes", "In Lobby", "Browsing Heroes", sleeping)

    elif(option <= 94 and option > 92):
        print("(Summon 2% ?)")
        sleeping = r.randint(40, 200)
        Activity_Set("Summon", "In Lobby", "Summon", sleeping)

    elif(option <= 96 and option > 94):
        print("(Reputation 2% ?)")
        sleeping = r.randint(40, 200)
        Activity_Set("Checking Reputation", "In Lobby", "Checking Reputation", sleeping)

    elif(option <= 98 and option > 96):
        print("(Pets 2% ?)")
        sleeping = r.randint(50, 100)
        Activity_Set("Checking Pets", "In Lobby", "Checking Pets", sleeping)

    elif(option <= 100 and option > 98):
        print("(Guild 2 % ?)")
        sleeping = r.randint(40, 200)
        Activity_Set("Checking Guild", "In Lobby", "Checking Guild", sleeping)

#######################################################################
######################     SCRIPT CORE     ############################
#######################################################################
def Init(): # Re-initialize the file to avoid corruption
    f = open("config.ini", "w")
    global lines
    lines = ["[Identifiers]\n", "ClientID=873973085936709632\n",
    "\n", "State=Idle\n", "Details=In Lobby\n", "StartTimestamp=\n",
    "EndTimestamp=\n", "\n", "[Images]\n", "LargeImage=e7_large\n",
    "LargeImageTooltip=Epic Seven\n", "SmallImage=\n", "SmallImageTooltip=\n"]
    f.writelines(lines)
    f.close()

def Update(status, details): # Update the file with the new status
    f = open("config.ini", "w")
    global lines
    lines[3] = f"State={status}\n"
    lines[4] = f"Details={details}\n"
    f.writelines(lines)
    f.close()
    print("Lines Written!")
    label_Status_name.config(text=status)
    label_Details_name.config(text=details)

def Lobby(): # Call the Lobby activity
    sleeping = r.randint(40, 200)
    print("[Activity] > Calling back the Lobby...")
    label_CallStack_name.config(text="[Should Start] > [Lobby]")
    label_CallStack_details.config(text=f"> spending {sleeping} seconds in lobby.")
    print(f"[Lobby]   > spending {sleeping} seconds in lobby.")
    print("Updating the file")
    Update("In Lobby", "Idle")
    sleep_time(sleeping)

def Should_Start(): # Decide if it is time to leave the Lobby
    while(True):
        x = r.randint(1,3)
        if (x <= 1):
            print("[Should_Start] > sleep in Lobby.")
            Lobby()
        if (x > 1 and x <= 3):
            print("[Should_Start] > start any activity.")
            Pick_Activity()

Init() # reset the file to avoid corruption
# Tkinter
window = Tk()
window.geometry("450x90")
window.resizable(width=False, height=False)
window.iconbitmap('icon.ico')
window.title("E7 Rich Presence")


label_CallStackDEFAULT = Label(window, text="Call Stack: ")
label_CallStackDEFAULT.grid(column=0, row=0)

label_CallStack_name = Label(window)
label_CallStack_name.grid(column=1, row=0)

label_CallStack_details = Label(window)
label_CallStack_details.grid(column=2, row=0)

label_StatusDEFAULT = Label(window, text="Status: ")
label_StatusDEFAULT.grid(column=0, row=1)

label_Status_name = Label(window)
label_Status_name.grid(column=1, row=1)

label_DetailsDEFAULT = Label(window, text="Details: ")
label_DetailsDEFAULT.grid(column=0, row=2)

label_Details_name = Label(window)
label_Details_name.grid(column=1, row=2)

label_TimerDEFAULT = Label(window, text="Timer: ")
label_TimerDEFAULT.grid(column=0, row=3)

label_TimerDATA = Label(window)
label_TimerDATA.grid(column=1, row=3)

th = threading.Thread(target=Should_Start)
th.start()

window.mainloop()