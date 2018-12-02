from graphics import *

class welcomePlayer:

   
        
    def createTitle(self, win):
        
        self.title = Image(Point(250,200), "title.png")

        
        #   Draw title
        self.title.draw(win)
        
       

        #   Define play button
    def playButton(self, win):
        self.play = Rectangle(Point(115, 250), Point(215, 300))
        self.play.setFill("purple1")
        self.playText = Text(Point(165, 275), "Play")
        self.playText.setSize(24)
        self.playText.setStyle("bold")
        self.playText.setTextColor(color_rgb(200, 30, 30))

        #   Draw play button

        self.play.draw(win)
        self.playText.draw(win)


        #   Define high score button
    def highScoreButton(self, win):
        
        self.highScore = Rectangle(Point(300, 250), Point(400, 300))
        self.highScore.setFill("purple1")
        self.trophy = Image(Point(350, 275), "trophy.png")

        #   Draw high score button
        self.highScore.draw(win)
        self.trophy.draw(win)

    def checkPlay(self, win):
        
        clickPoint = win.getMouse()
        inPlayButtonX = False
        inPlayButtonY = False

        if self.play.getP1().getX() < clickPoint.getX() < self.play.getP2().getX():
            inPlayButtonX = True
            
        
        if self.play.getP1().getY() < clickPoint.getY() < self.play.getP2().getY():
            inPlayButtonY = True
            
        if inPlayButtonX and inPlayButtonY:
           
            return True
            
        
       
        
        

    def checkHS(self, win):
        clickPoint = win.getMouse()
        
        if self.highScore.getP1().getX() < clickPoint.getX() < self.highScore.getP2().getX():
            inButtonX = True
        
        if self.highScore.getP1().getY() < clickPoint.getY() < self.highScore.getP2().getY():
            inButtonY = True

        if inButtonX and inButtonY:
            return True
        






