##################################################################################################################################
#
# Name: twixt_board.py
# Author: Alfredo Pena
# CSCI 6370 - Lab 1
# Purpose: Create a clickable board game application for the game Twixt (modified rules for Normal Play + Impartial)
# Last Modified: 9/8/2024
#
##################################################################################################################################

from graphics import *

# global variables  
boardSize = 7
lineWidth = 4
centers = []
clickAreas = []

def draw_board(window):
    # draw the board and save the clickable areas
    for i in range(50, 800, 100):
        for j in range(50, 800, 100):
            rect = Rectangle(Point(i - 50, j - 50), Point(i + 50, j + 50))
            rect.draw(window)
            clickAreas.append(rect)
    
    # draw the border lines
    line = Line(Point(120, 100), Point(580, 100)) # bottom
    line.setWidth(lineWidth)
    line.draw(window)
    line = Line(Point(100, 120), Point(100, 580)) # left
    line.setWidth(lineWidth)
    line.draw(window)
    line = Line(Point(120, 600), Point(580, 600)) # top
    line.setWidth(lineWidth)
    line.draw(window)
    line = Line(Point(600, 120), Point(600, 580)) # right
    line.setWidth(lineWidth)
    line.draw(window)
    
    # draw the peg holes
    for i in range(50, 800, 100):
        for j in range(50, 800, 100):
            centers.append(Point(i, j)) # save the center points of the peg holes
            circle = Circle(Point(i, j), 40)
            circle.draw(window)


def play_game(window):
    while True:
        # get the first click
        click1 = window.getMouse()
        # get the second click
        click2 = window.getMouse()
        # set up points for the pegs
        peg1 = Point(0, 0)
        peg2 = Point(0, 0)
        
        # draw a peg in the center corresponding to the clicked area
        for i in range(len(clickAreas)): 
            if clickAreas[i].getP1().getX() < click1.getX() < clickAreas[i].getP2().getX() and clickAreas[i].getP1().getY() < click1.getY() < clickAreas[i].getP2().getY():
                peg1 = Circle(centers[i], 10)
                peg = Circle(centers[i], 10)
                peg.setFill("black")
                peg.draw(window)
            if clickAreas[i].getP1().getX() < click2.getX() < clickAreas[i].getP2().getX() and clickAreas[i].getP1().getY() < click2.getY() < clickAreas[i].getP2().getY():
                peg2 = Circle(centers[i], 10)
                peg = Circle(centers[i], 10)
                peg.setFill("black")
                peg.draw(window)
        # draw a line between the two clicks
        line = Line(peg1.getCenter(), peg2.getCenter())
        line.draw(window)
        
        
        
def main():
    window = GraphWin("Twixt", 1000, 1000)
    window.setCoords(0, 0, boardSize * 100, boardSize * 100)
    window.setBackground("white")
    draw_board(window)
    play_game(window)
    
    
if __name__ == "__main__":
    main()