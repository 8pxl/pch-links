import pyautogui as pg
import time

def save():
    pg.rightClick(1000,500)
    pg.click(1044,590)
    time.sleep(.8)
    pg.write('f')
    pg.click(830,605)
    pg.click(817,560)
    pg.click(1016,660)
    time.sleep(.3)
    pg.click(802,570)

def switchPage(sem,unit):
    offset = 45
    if sem==1:
        pg.moveTo(1304,131)
    else:
        pg.moveTo(1143,131)

    pg.moveRel(0,66+ unit * offset)
    pg.click()
        
def createFile(title):
    f = open('addison website scraper/' + title , "x")


def writeToFile(title,input):
    f = open('addison website scraper/' + title,'a')
    f.write(input+ "\n")

def searchLinks(path,title):
    f = open(path) 
    a = f.read()
    for i in range(len(a)):
        search = True
        length = 0
        if a[i:i+15] == "href=\"https://d":
            while search:
                if (a[i+46+length] == "\""):
                    print(a[i+6:i+46+length])
                    writeToFile(title, a[i+6:i+46+length])
                    search = False
                length+=1

units = 4
for i in range(2):
    for j in range(units):
        title = "sem " + str(i+1) + " unit"  + str(j+1) + '.txt'
        switchPage(i+1,j)
        time.sleep(3)
        save()
        createFile(title)
        searchLinks('addison website scraper/f.html', title)
        time.sleep(1)
    units = 5
    time.sleep(3)
