import math
import random 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
newset = []
for i in range(100):
  newpair = []
  newpair.append(random.randint(1,100))
  newpair.append(random.randint(1,100))
  newpair = tuple(newpair)
  newset.append(newpair)

print(newset)
    
    
def euclidean(point1,point2):
    sum = 0
    for i in range(len(point1)):
        sum += (point1[i]-point2[i])**2
    return sum**(1/2)

def add(point1,point2):
    point3 = []
    for i in range(len(point1)):
        tupresult = []
        tupresult += [point1[i] + point2[i]]
        point3 += tupresult
    return tuple(point3)

def multiply(float, point1):
    newpoint = []
    for i in range(len(point1)):
        tupresult = []
        tupresult += [float*point1[i]]
        newpoint += tupresult
    return tuple(newpoint)

def func(point,set):
    distance = 0
    for i in range(len(set)):
        distance += euclidean(point, set[i])
    return distance

def cis(real):
    return (math.cos(2*math.pi*real),math.sin(2*math.pi*real))

def guess(origin, numberofpoints):
    finalset = []
    for i in range(numberofpoints):
        finalset += [add(origin,(math.cos(2*math.pi*i/numberofpoints), math.sin(2*math.pi*i/numberofpoints)))]
    return finalset

def multiplysets(float, set):
  newset = []
  for i in range(len(set)):
    multipliedtuple = multiply(float,set[i])
    newset.append(multipliedtuple)
  return newset

def indexedmax(array):
    maximum = -10**9
    for i in range(len(array)):
        if (array[i] > maximum):
            maximum = array[i]
            maximumindex = i
        else:
            continue
    return (maximum, maximumindex)

def error(point, numberofpoints, set):
    pointset = guess(point, numberofpoints)
    differences = []
    for i in range(numberofpoints):
        differences.append(func(point,set) - func(pointset[i],set))
    return indexedmax(differences)


def ai(iterations,set,guesses,learningspeed):
    comparisonpoint = (random.randint(1,100),random.randint(1,100))
    counter = 0
    for i in range(iterations):
        derivative = error(comparisonpoint, guesses, set)
        if (derivative[0] < 0):
            counter += 1
        else:
            direction = derivative[1]
            comparisonpoint = add(comparisonpoint, multiply((learningspeed)**(i+counter),multiply(func(comparisonpoint,set)/derivative[0],cis(derivative[1]/guesses))))
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
def ainograph(iterations,set,guesses,learningspeed):
  comparisonpoint = (random.randint(1,100),random.randint(1,100))
  counter = 0
  for i in range(iterations):
    derivative = error(comparisonpoint, guesses, set)
    if (derivative[0] < 0):
        counter += 1
    else:
        direction = derivative[1]
        comparisonpoint = add(comparisonpoint, multiply((learningspeed)**(i+counter),multiply(func(comparisonpoint,set)/derivative[0],cis(derivative[1]/guesses))))
        counter = 0
  return (comparisonpoint, func(comparisonpoint, set))

ai(800, newset, 20, 0.97)

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
                  
#some more numerical inconsistency

def inconsistency(iterations, set, guesses, alpha, approximation):
  counter = 0
  for i in range(approximation):
    randompoint = (random.randint(1,100),random.randint(1,100))
    if (ainograph(iterations, set, guesses, alpha)[1] > func(randompoint, set)):
      continue
    else:
      counter += 1
  return counter/approximation
  
print(inconsistency(800,newset, 20, 0.97, 50))
                        
