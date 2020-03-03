buttons = []
simonTones = None
simonSentence = []
positionInSentence = 0
currentLengthOfTheSentence = 0
talkTime = 420
timeOut = 0
isSimonsTurn = True
isWrong = False
class SimonSays:
    def setup():
        size(600,600)
        buttons[0] = Button(0,0,0,300,hex(65280))
        buttons[1] = Button(1,300,0,300,hex(16711680))
        buttons[2] = Button(2,0,300,300,hex(16776960))
        buttons[3] = Button(3,300,300,300,hex(255))
    
        simonTones = SimonToneGenerator(self)
        textSize(40)
        textAlign(CENTER,CENTER)
        simonStartsNewGame()
        
    def draw():
        simonTones.checkPlayTime()
        if (simonTones.isPlayingTone == False):
            setButtonLightsOff()
        if (isSimonsTurn == True):
            simonSays()
        for button in buttons:
            button.display()
        fill(255)
        
        if (isSimonsTurn == True):
            if (currentLengthOfTheSentence == 0):
                text("Simon Starts",width/2, height/2)
                
            else:
                text("Simon Turn",width/2, height/2)
                
        else:
            text("Your Turn",width/2, height/2)
            
    def simonSays():
        if (millis() >=timeOut):
            simonsWord = simonSentence[positionInSentence]
            simonTones.playTone(simonsWord,talkTime)
            buttons[simonsWord].isLightOn = True
            if (positionInSentence < currentLengthOfTheSentence): 
                positionInSentence = positionInSentence+1   
            else:
                isSimonsTurn = False
                positionInSentence = 0
            timeOut = millis() + talkTime+ 55
            
    def mousePressed():
        if (isSimonsTurn == True):
            for currentButton in buttons:
                if (currentbutton.isMouseOver()== True):
                    currentButton.isLightOn = True
                    if (simonSentence[positionInSentence]!= currentButton.myId):
                        simontones.playTone(4,420)
                        isWrong = True
                    else:
                        simonTones.playTone(currentButton.myId,420)
                
    def mouseReleased():
        if (isSimonsTurn == False):
            simonsTone.stopTone()
            setButtonsLightsOff() 
            if (isWrong == True):
                simonStartsNewGame()
                isWrong = False
            else:
                if (positionInSentence < currentLengthOfTheSentence):
                    positionInSentence = positionInSentence+1
                else:
                    if (currentLengthOfTheSentence == len(simonSentence)-1):
                        print("YOU WIN!!!")
                        simonStratsNewGame()
                    else:
                        currentLengthOfTheSentence =  currentLengthOfTheSentence+1
                        if (currentLengthOfTheSentence < 6):
                            talkTime = 420
                        elif(currentLengthOfTheSentence < 14):
                            talkTime = 320
                        else:
                            talkTime = 220
                        positionInsentence = 0
                        timeOut = millis() +1000
                        isSimonsTurn = True
                
    def setButtonsLightOff():
        for currentButton in buttons:
            currentButton.isLightOn = False
            
    def simonStartsNewGame():
        makeNewSentence()
        timeOut = millis() +1000
        isSimonsTurn = True 
        
    def makeNewSentence():
        for i in range(len (simonsSentence)):
            
            simonSentence[i] = int(random(0,4))
        
        positionInSentence = 0
        currentLengthOfTheSentence = 0
        
class Button:
    myX = 0
    myY = 0
    mySize = 0
    myColor = None
    myDarkColor = None
    isLightOn = False
    
    def __init__(self, tempID,tempX,tempY,tempSize,tempColor):
        myID = tempID
        myX = tempX
        myY = tempY
        mySize = tempSize
        myColor = hex(tempColor)
        myDarkColor = lerpColor(0,myColor,0.5)
        
    def display():
        if isLightOn == True:
            fill(myColor)
        else:
            fill(myDarkColor)
            
        rect(myX,myY,mySize,mySize)
        
    def isMouseOver():
        if(mouseX > myX and mouseX < (myX + mySize)and mouseY > myY and mouseY < (myY + mySize)):
            return True 
        else:
            return False
        

class SimonToneGenerator:
    simonTones = [391.995,325.628,261.626,195.998,48.9994]
    wave = None
    toneStopTime = -1
    isPlayingTone = False
    
    def __init__(self, p):
        wave = SqrOsc(p)
        wave.play()
        wave.amp(0.0)
        
    def playTone(index,toneDuration):
        wave.amp(0.6)
        wave.freq(simonTones[index])
        toneStopTime = millis()+toneDuration
        isPlayingTone = True
        
    def checkPlayTime():
        if isPlayingTone == True:
            if millis()>= toneStopTime:
                stopTone()
                
    def stopTone():
        if isPlayingTone == True:
            wave.amp(0.0)
            isPlayingTone = False
