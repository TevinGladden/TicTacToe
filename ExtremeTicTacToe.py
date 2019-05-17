from tkinter import *
import random
import math

class TTT:
    def __init__(self, symbol1, symbol2):
        self.player1 = symbol1
        self.player2 = symbol2
        self.score1 = self.score2 = 0
        self.playerTurn = symbol1
      
        #Add EXTREME contiguous deletion variable check
        self.extreme1 = 1
        self.extreme2 = 1
        
        #Defining window root
        self.root = Tk()
        self.root.title("Extreme Tic Tac Toe")
        self.root.geometry("800x150")
        self.root.resizable(width=False, height=False)
        
        #Grid array
        self.grid = ["blank","blank","blank","blank","blank","blank","blank","blank","blank"]
                
        #Canvas for game board, player information
        self.leftCanvas = Canvas(self.root, height = 100, width = 50)
        self.middleCanvas = Canvas(self.root, height = 50, width = 50)
        self.rightCanvas = Canvas(self.root, height = 100, width = 50)
        self.leftCanvas.place(relx = 0.1, rely = 0.5, anchor = W)
        self.middleCanvas.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        self.rightCanvas.place(relx = 0.9, rely = 0.5, anchor = E)    
        self.topCanvas = Canvas(self.root, height = 50, width = 50)
        self.topCanvas.place(relx = 0.5, rely = 0.1, anchor = N)
        
        #labels for canvases
        self.leftLabel = Label(self.leftCanvas, text = "Player 1: " + str(self.player1) + "'s", bg = "white")
        self.leftLabel.pack(side = TOP)
        self.rightLabel = Label(self.rightCanvas, text = "Player 2: " + str(self.player2) + "'s", bg = "white")
        self.rightLabel.pack(side = TOP)
        self.topLabel = Label(self.topCanvas, text = "Score: " + str(self.score1) + "-" + str(self.score2), bg = "white")
        self.topLabel.pack(side = TOP)        
        
        #Extreme buttons
        extreme1 = Button(self.leftCanvas, text = "Extreme Button", command = lambda: self.explosion())
        self.ent1 = Entry(self.leftCanvas)
        extreme1.pack()
        extreme2 = Button(self.rightCanvas, text = "Extreme Button", command = lambda: self.explosion())
        extreme2.pack()
        #self.ent1.pack(side = LEFT)
        self.ent1.bind("<Return>", self.wipe())
        
        #buttons for gameboard
        topLeft = Button(self.middleCanvas, text = self.grid[0], width = 10, command = lambda: self.playPiece(0))
        topLeft.grid(row = 0, column = 0)
        topMiddle = Button(self.middleCanvas, text = self.grid[1], width = 10, command = lambda: self.playPiece(1))
        topMiddle.grid(row = 0, column = 1)        
        topRight = Button(self.middleCanvas, text = self.grid[2], width = 10, command = lambda: self.playPiece(2))
        topRight.grid(row = 0, column = 2)
        middleLeft = Button(self.middleCanvas, text = self.grid[3], width = 10, command = lambda: self.playPiece(3))
        middleLeft.grid(row = 1, column = 0) 
        middleMiddle = Button(self.middleCanvas, text = self.grid[4], width = 10, command = lambda: self.playPiece(4))
        middleMiddle.grid(row = 1, column = 1)
        middleRight = Button(self.middleCanvas, text = self.grid[5], width = 10, command = lambda: self.playPiece(5))
        middleRight.grid(row = 1, column = 2) 
        bottomLeft = Button(self.middleCanvas, text = self.grid[6], width = 10, command = lambda: self.playPiece(6))
        bottomLeft.grid(row = 2, column = 0)
        bottomMiddle = Button(self.middleCanvas, text = self.grid[7], width = 10, command = lambda: self.playPiece(7))
        bottomMiddle.grid(row = 2, column = 1)  
        bottomRight = Button(self.middleCanvas, text = self.grid[8], width = 10, command = lambda: self.playPiece(8))
        bottomRight.grid(row = 2, column = 2)
        
        self.buttonArray = [topLeft, topMiddle, topRight, middleLeft, middleMiddle, middleRight, bottomLeft, bottomMiddle, bottomRight]
        self.extremeArray = [extreme1, extreme2]
        
    def playPiece(self, num):
        if self.playerTurn == self.player1:
            self.grid[num] = self.player1
            self.buttonArray[num].configure(text = self.player1)            
            self.winCheck()
            self.playerTurn = self.player2
            #print("YO")
        else:
            self.grid[num]= self.player2
            self.buttonArray[num].configure(text = self.player2) 
            self.winCheck()
            self.playerTurn = self.player1   
            
    def diagnolCheck(self):
        return (self.grid[0] == self.grid[4] == self.grid[8] != "blank"  or self.grid[2] == self.grid[4] == self.grid[6] != "blank")
    
    def rowCheck(self):
        return (self.grid[0] == self.grid[1] == self.grid[2] != "blank"  or self.grid[3] == self.grid[4] == self.grid[5] != "blank" or self.grid[6] == self.grid[7] == self.grid[8] != "blank")
   
    def columnCheck(self):
        #print self.grid
        return (self.grid[0] == self.grid[3] == self.grid[6] != "blank" or self.grid[1] == self.grid[4] == self.grid[7] != "blank" or self.grid[2] == self.grid[5] == self.grid[8] != "blank") 
    def drawCheck(self):
        if("blank" in self.grid):
            return False
        else:
            return True
    
    def winCheck(self):
        if (self.columnCheck() or self.rowCheck() or self.diagnolCheck()):
            self.topLabel.configure(text = "Player " + str(self.playerTurn) + " Wins")
            self.point()            
            self.clearBoard()
        elif (self.drawCheck()):
            self.topLabel.configure(text = "DRAW")
            self.clearBoard()
            
    def clearBoard(self):
        self.grid = ["blank","blank","blank","blank","blank","blank","blank","blank","blank"]
        for button in self.buttonArray:
            button.configure(text = "blank")        
        self.playerTurn = self.player1
        self.topLabel.configure(text = "Score: " + str(self.score1) + "-" + str(self.score2))
          
    def point(self):
        if(self.playerTurn == self.player1):
            self.score1 += 1
        else:
            self.score2 += 1       
            
    def wipe(self):
        pass
        #print("Hello")
        #wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,5]]
    
    def explosion(self):
        if self.playerTurn == self.player1:
            if self.extreme1 == 1:
                rand_array = list(range(9))
                size = math.floor(random.random()*8)
                
                #print(rand_array, size)
                random.shuffle(rand_array)
                #print(rand_array)
                return_array = rand_array[0:size]
                #print(return_array)
                for i in return_array[0:size]:
                    self.buttonArray[i].configure(text = 'blank') 
                    self.grid[i] = 'blank'
                self.playerTurn = self.player2
                
        elif self.playerTurn == self.player2:
            if self.extreme2 == 1:
                rand_array = list(range(9))
                size = math.floor(random.random()*8)
                
                #print(rand_array, size)
                random.shuffle(rand_array)
                #print(rand_array)
                return_array = rand_array[0:size]
                #print(return_array)
                for i in return_array[0:size]:
                    self.buttonArray[i].configure(text = 'blank')
                    self.grid[i] = 'blank'                    
                self.playerTurn = self.player1
                
                    
window = TTT("X", "O")
#print(window.explosion())
window.root.mainloop()
