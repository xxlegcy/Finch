from BirdBrain import Finch
from time import sleep
bird=Finch()



def exercise1():
    bird.setMotors(50,50)
    sleep(1)
    bird.stop()


def exercise2():
    finch.wheels(0.5,0)
    sleep(1)
    finch.wheels(0,0)
    


def exercise3():
    bird.setMotors(0,50)
    sleep(3)
    bird.setMotors(50,50)
    sleep(3)
    bird.setMotors(0,50)
    sleep(3)
    bird.setMotors(50,50)
    sleep(6)
    bird.setMotors(50,0)
    sleep(3)
    bird.setMotors(50,50)
    sleep(3)
    bird.setMotors(50,0)
    sleep(3)
    bird.setMotors(50,0)
    bird.stop()


def exercise4():
    color = input("Please enter a letter: ")
    if (color == 'g'):
        birf.setBeak(0,100,0)
    else:
        print('Sorry, that is not my favorite letter!')
    sleep(1)
    bird.stopAll()

def exercise5():
    color = input("Please enter a letter:") #Allows the Program to ask the user
    if (color == 'r'): #Tells the program what letter the user wants
        bird.setTurn('R',70,50)#Turns the Finch to the Right


    else:
        print('Oh so close but you got it wrong')
        bird.setTurn('L',70,50)


def exercise6():
    valueRed = int(input("What is the amout of Red"))
    valueGreen = int(input("What is the amount of Green"))
    valueBlue = int(input("what is the amount of Blue"))
    bird.setBeak(valueRed,valueGreen,valueBlue)
    bird.setTail('all',valueRed,valueGreen,valueBlue)
    sleep(3)
    bird.stopAll()


def exercise7():
    sideLength = int(input("what is the side length"))
    bird.seTail(1,100,0,0)
    bird.setMove('F',sideLength,30)
    bird.setTurn('R',90,30)
    bird.setTail(2,0,100,0)
    bird.setMove('F',sideLength,30)
    bird.setTurn('R',90,30)
    bird.setTail(3,0,0,100)
    bird.setMove('F',sideLength,30)
    bird.setTurn('R',90,30)
    bird.setTail(4,50,0,70)
    bird.setMove('F',sideLength,30)
    bird.setTurn('R',90,30)
    bird.stopAll()
                        
    
    


#exercise1
#exercise2
#exercise3
#exercise4
#exercise5
#exercise6
#exercise7S
