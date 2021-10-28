from bearlibterminal import terminal
from time import sleep as s
import StoryTextandCreatureStats

def FormatTheText(playerName): #Adds the player name (when needed) to the string arrays held in the ther script
    StoryTextandCreatureStats.startText[3] = StoryTextandCreatureStats.startText[3].format(playerName)
    StoryTextandCreatureStats.pauirtgdyText[19] = StoryTextandCreatureStats.pauirtgdyText[19].format(playerName) 
    StoryTextandCreatureStats.pauirtgdyText[20] = StoryTextandCreatureStats.pauirtgdyText[20].format(playerName) 

def slp(sleepTime): #Time.sleep()s for a specific amount of time (parameter "sleepTime"), then refreshes the terminal.
    terminal.refresh()
    s(sleepTime)

def LoadGame(): #Loads a saved game. (NOT IMPLEMENTED YET)
    terminal.color(terminal.color_from_name("white"))
    terminal.printf(0, 0, "Sorry, but loading hasn't been implemented yet :(.")
    slp(1)
    terminal.printf(0, 0, " " * 60)
    terminal.printf(0, 1, " " * 4)
    Start()

def DoCombat(playerName, creatureName):
    enemy = StoryTextandCreatureStats.creatureStats[creatureName]
    terminal.clear()
    terminal.printf(0, 0, enemy["icon"])
    terminal.printf(10, 0, "[0xE000][color=playerColor]@")
    slp(5)

def Start(): #The stuff that happenes at the start of the game.
    i = 0
    name = " "
    terminal.open()
    terminal.set("window: title = 'Enter your name.', size = 80x30; palette.playerColor = #c2ffff")
    terminal.setf("0xE000: woodenSword.png, align=center; 0xE001: ironSword.png, align=center")
    terminal.printf(0, 0, "Enter name: ")
    terminal.color(terminal.color_from_name("playerColor"))
    terminal.refresh()

    while True: #Gets the name of the player
        key = terminal.read()
        if key != terminal.TK_RETURN:
            name += chr(key + 93)
            terminal.put(i, 1, chr(key + 93))
            i += 1
            terminal.refresh()
        else:
            name = name.title()
            break

    if name == " Load":
        LoadGame()
    elif name == " Skipone":
        terminal.color(terminal.color_from_name("white"))
        terminal.printf(0, 0, "[bkcolor=blue]Chapter 1: The Start[/bkcolor][bkcolor=black]")
        FormatTheText(" Test")
        ChapterOne(" Test") 
    elif name == " Cmbt":
        DoCombat(" Test", "fishKing")
    FormatTheText(name)
    terminal.set("window.title = The Backstory.")
    terminal.color(terminal.color_from_name("white"))
    terminal.printf(0, 0, "[bkcolor=darker purple]Hello,{}.[/bkcolor]  ".format(name))
    terminal.printf(0, 1, " " * len(name))
    slp(1)

    backstory = StoryTextandCreatureStats.backstory
    i = 1
    while i <= len(backstory): #Prints the backstory
        terminal.printf(0, i, backstory[i - 1])
        i += 1
        slp(1)

    terminal.printf(0, len(backstory) + 1, "[bkcolor=blue]Chapter 1: The Start[/bkcolor]")
    slp(2)

    i = len(backstory)
    while i >= 0: #Does the cool title thing.
        terminal.printf(0, i + 1, "[bkcolor=black]" + " " * 80 + "[/bkcolor]")
        terminal.printf(0, i, "[bkcolor=blue]Chapter 1: The Start[/bkcolor][bkcolor=black]" + " " * 60 + "[/bkcolor]")
        #The end bit is just to make sure that the whole line is cleared.
        i -= 1
        slp(0.2)

    slp(1)
    ChapterOne(name)

def ChapterOne(name):
    name = name
    i = 1
    terminal.set("window: title = Chapter 1: The Start.")

    startText = StoryTextandCreatureStats.startText
    kidnappedText = StoryTextandCreatureStats.kidnappedText
    pauirtgdyText = StoryTextandCreatureStats.pauirtgdyText

    while i <= len(startText):
        terminal.printf(0, i, startText[i - 1])
        slp(0.5)
        i += 1
    
    terminal.clear()
    terminal.printf(0, 0, "[bkcolor=blue]Chapter 1.1: A... Turbulent Begining.[/bkcolor]")
    terminal.set("window.title = Chapter 1.1: A... Turbulent Begining.")
    slp(2)
    i = 1
    terminal.color(terminal.color_from_name("playerColor"))
    while i <= len(kidnappedText):
        terminal.printf(0, i, kidnappedText[i - 1])
        slp(0.5)
        i += 1
    slp(1)
    terminal.color(terminal.color_from_name("white"))
    terminal.clear()
    terminal.printf(0, 0, "[bkcolor=blue]Chapter 1.2: Welcome to \"PaUiRtGdY\".[/bkcolor]")
    terminal.set("window.title = Chapter 1.2: Welcome to \"PaUiRtGdY\".")
    slp(2)
    i = 1
    while i <= len(pauirtgdyText):
        terminal.printf(0, i, pauirtgdyText[i - 1])
        slp(1)
        if i == 3:
            terminal.set("window.title = YOU WILL PAY.")
        elif i == 11:
            terminal.set("window.title = Sorry, Wrong Person.")
        i += 1
    terminal.clear()
    terminal.printf(0, 0, "[bkcolor=blue]Chapter 1.3: A Royal Fight.[/bkcolor]")
    terminal.set("window.title = Chapter 1.3: A Royal Fight.")
    slp(2)
    terminal.close()


if __name__ == "__main__": #Obligatory 'if __name__ == "__main__":'
    Start()       #thing to let people who are good at coding
                           #know that you are supposed to run this script.
