from BirdBrain import Finch
bird = Finch()


def exercise1():
    print("Distance: ", bird.getDistance())


def exercise2():
    print("Right Light Sensor", bird.getLight('R'))
    print("Left Light Sensor",bird.getLight('L'))
    print("Button A", bird.getButton('A'))
    print("Orientation", bird.getOrientation())
    print("Encoder", bird.getEncode('R'))


def exercise3():
    print(type(bird.getLight('R')))
    print(type(bird.getLight('L')))
    print(type(bird.getButton('A')))
    print(type(bird.getOrientation()))
    print(type(bird.getEncoder('R')))


def exercise4():
    currentDistance = bird.getDistance()
    print(currentDistance)
    print(2*currentDistance)
    print(4*currentDistance)
    


    
#exercise1()    
#exercise2()
#exercise3()
exercise4()
