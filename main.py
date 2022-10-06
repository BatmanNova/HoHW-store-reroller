from python_imagesearch.imagesearch import *
import pydirectinput
RerollReady = False
RerollPosition = False
howManyRolls = 20

#takes the the amount of rolls
#screen grabs with region_grabber
#Seachers the available region for the item icons
#if it finds 2 of the items you are looking for, it stops clicking

#the precision parameter in imagesearcharea() which is the 6th
# parameter(usuall decimal) may need.
#to be changed depending onthe item. Seal of souls is similar to others and
# a higher precision is needed.
time1 = time.clock()
for i in range(howManyRolls):
    im = region_grabber((0, 0, 1200, 1000))
    #blueItem1 = imagesearcharea("dwarvenpick.png", 690, 690, 730, 730, 0.8, im)
    #blueItem2 = imagesearcharea("luckyhat.png", 690, 690, 730, 730, 0.8, im)
    #blueItem3 = imagesearcharea("magebane.png", 690, 690, 730, 730, 0.8, im)
    #if (blueItem1[0] != -1 or blueItem2[0] != -1):
    greenItem1 = imagesearcharea("oldmap.png", 690, 600, 730, 680, 1, im)
    #    greenItem2 = imagesearcharea("shaftlocke.png", 690, 600, 730, 680, 0.8, im)
        #greenItem3 = imagesearcharea("assassindagger.png", 690, 600, 730, 680, 0.8, im)
    time2 = time.clock()
    print(str(time2 - time1) + " Seconds")
    if (greenItem1[0] != -1):
        print("found green item 1")
        break
    #if (blueItem1[0] != -1 or blueItem2[0] != -1) and (greenItem1[0] != -1 or greenItem2[0] != -1):
        #if (blueItem1[0] != -1):
        #    print("found blue item 1")
        #if (blueItem2[0] != -1):
        #   print("found blue item 2")
        #if (blueItem3[0] != -1):
        #    print("found blue item 3")
        #if (greenItem1[0] != -1):
        #    print("found green item 1")
        #if (greenItem2[0] != -1):
        #    print("found green item 2")
        #if (greenItem3[0] != -1):
        #    print("found green item 3")

    else:
        if not RerollPosition:
            #grabs the position of reroll button
            pos = imagesearcharea("reroll.png", 850, 730, 1074, 761, 0.2, im)
            RerollPosition = True
        if not RerollReady:
            #click image is only used to position mouse over reroll
            #for some reason it does not click
            click_image("reroll.png", pos, "right", 0.2, offset=5)
            RerollReady = True
        pydirectinput.mouseDown()
        pydirectinput.mouseUp()
        print("rerolling")
