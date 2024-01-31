import math
import random 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
newset = []
#The main idea of this is to try and find the least Euclidean distance to each of the points. This can be generalized to n entries, although I
#Blackbird, am too lazy.
#This generates a random set of a hundred ordered pairs.
for i in range(100):
  newpair = []
  newpair.append(random.randint(1,100))
  newpair.append(random.randint(1,100))
  newpair = tuple(newpair)
  newset.append(newpair)

print(newset)
    
#This generates the euclidean distance between two points. (i.e regular pythagorean theorem.)
def euclidean(point1,point2):
    sum = 0
    for i in range(len(point1)):
        sum += (point1[i]-point2[i])**2
    return sum**(1/2)

#This adds the two coordinates of the points. 
def add(point1,point2):
    point3 = []
    for i in range(len(point1)):
        tupresult = []
        tupresult += [point1[i] + point2[i]]
        point3 += tupresult
    return tuple(point3)

#This multiplmies a vector by a scalar.
def multiply(float, point1):
    newpoint = []
    for i in range(len(point1)):
        tupresult = []
        tupresult += [float*point1[i]]
        newpoint += tupresult
    return tuple(newpoint)

#Takes the sum of the euclidean distances between each point in a set.
def func(point,set):
    distance = 0
    for i in range(len(set)):
        distance += euclidean(point, set[i])
    return distance

#This is the number that you get when you walk real times around a circle centered at the origin and with radius 1.
def cis(real):
    return (math.cos(2*math.pi*real),math.sin(2*math.pi*real))

#This gives different 'guesses' as to the lowest sum.
def guess(origin, numberofpoints):
    finalset = []
    for i in range(numberofpoints):
        finalset += [add(origin,(math.cos(2*math.pi*i/numberofpoints), math.sin(2*math.pi*i/numberofpoints)))]
    return finalset

#This multiplies all of the numbers in a set.
def multiplysets(float, set):
  newset = []
  for i in range(len(set)):
    multipliedtuple = multiply(float,set[i])
    newset.append(multipliedtuple)
  return newset

#This gives the index of the maximunm element of the array, as well as the maximum element itself.
def indexedmax(array):
    maximum = -10**9
    for i in range(len(array)):
        if (array[i] > maximum):
            maximum = array[i]
            maximumindex = i
        else:
            continue
    return (maximum, maximumindex)
#This talks about how 'bad' it is to try and deviate from that point. The worse it is trying to deviate from that point, the better.
def error(point, numberofpoints, set):
    pointset = guess(point, numberofpoints)
    differences = []
    for i in range(numberofpoints):
        differences.append(func(point,set) - func(pointset[i],set))
    return indexedmax(differences)

#Main AI, showing a graph. There is iterations, as well as the set itself, and a few different guesses from each origin point. There is also learning speed.
#There is also hyperlearning speed, a hyperparameter, that slows the learning. In this case, it is good, as we don't want the AI to overshoot
#on the minimal distance, and go haywire. (You can see this by setting hyper learning speed to 10.)
def ai(iterations,set,guesses,learningspeed,hyperlearningspeed):
    comparisonpoint = (random.randint(1,100),random.randint(1,100))
    counter = 0
    for i in range(iterations):
        derivative = error(comparisonpoint, guesses, set)
        if (derivative[0] < 0):
            counter += 1
        else:
            direction = derivative[1]
            comparisonpoint = add(comparisonpoint, multiply(hyperlearningspeed*(learningspeed)**(i+counter),multiply(func(comparisonpoint,set)/derivative[0],cis(derivative[1]/guesses))))
            counter = 0
        if (i % 20 == 0):
          xpoint = np.array(comparisonpoint[0])
          ypoint = np.array(comparisonpoint[1])
          plt.plot(xpoint,ypoint,'o')
          print((comparisonpoint, func(comparisonpoint,set)))
        else:
          continue
    plt.show()
    return (comparisonpoint, func(comparisonpoint, set))
#This has no graph.
def ainograph(iterations,set,guesses,learningspeed, hyperlearningspeed):
  comparisonpoint = (random.randint(1,100),random.randint(1,100))
  counter = 0
  for i in range(iterations):
    derivative = error(comparisonpoint, guesses, set)
    if (derivative[0] < 0):
        counter += 1
    else:
        direction = derivative[1]
        comparisonpoint = add(comparisonpoint, multiply(hyperlearningspeed*(learningspeed)**(i+counter),multiply(func(comparisonpoint,set)/derivative[0],cis(derivative[1]/guesses))))
        counter = 0
  return (comparisonpoint, func(comparisonpoint, set))

ai(800, newset, 20,0.05, 0.99)

def matplotlibsupport(set):
  xcoordinates = []
  ycoordinates = []
  for i in range(len(set)):
    xcoordinates.append(set[i][0])
    ycoordinates.append(set[i][1])
  return (xcoordinates, ycoordinates)


xpoints = np.array(matplotlibsupport(newset)[0])
ypoints = np.array(matplotlibsupport(newset)[1])
plt.plot(xpoints, ypoints, 'o')
plt.show()
                  
#some more numerical inconsistency, as well as different hyperparameters etc.

def inconsistency(iterations, set, guesses, alpha, beta, approximation):
  counter = 0
  for i in range(approximation):
    randompoint = (random.randint(1,100),random.randint(1,100))
    if (ainograph(iterations, set, guesses, alpha,beta)[1] > func(randompoint, set)):
      continue
    else:
      counter += 1
  return counter/approximation

                        
