from BirdBrain import Finch
from time import sleep

robot = Finch()


def exercise1():
    robot.setBeak(100, 0, 0)
    sleep(1)
    robot.setBeak(0, 0, 0)

exercise1()


def exercise2():
    robot.setBeak(100, 0, 100)
    sleep(1)
    robot.setBeak(0, 100, 100)
    sleep(1)
    robot.setBeak(100, 100, 0)
    sleep(1)
    robot.setBeak(0, 0, 0)

def exercise3():
    robot.setTail(1, 0, 0, 100)
    robot.setTail(4, 0, 0, 100)
    sleep(2)
    robot.stopAll()


def exercise4():
    robot.setTail(1, 100, 0, 0)
    robot.setTail(2, 255, 165, 0)
    robot.setTail(3, 100, 100, 0)
    robot.setTail(4, 0, 100, 0)
    robot.setBeak(0, 0, 100)
    sleep(1)
    robot.setTail(1, 100, 0, 0)
    robot.setTail(2, 255, 165, 0)
    robot.setTail(3, 100, 100, 0)
    robot.setTail(4, 0, 100, 0)
    robot.setBeak(75, 0, 130)
    sleep(1)
    robot.setTail(1, 100, 0, 0)
    robot.setTail(2, 255, 165, 0)
    robot.setTail(3, 100, 100, 0)
    robot.setTail(4, 0, 100, 0)
    robot.setBeak(127, 0, 255)
    sleep(1)
    robot.stopAll()


def exercise5():
    userResponse = input("Which tail light (1-4) should be red?")
    number = int(userResponse)
    robot.setTail(number, 100, 0, 0)
    sleep(1)
    robot.stopAll()


#exercise1()
#exercise2()
#exercise3()
#exercise4()
#exercise5()
