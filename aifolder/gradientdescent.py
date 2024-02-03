#So it turns out I did not do gradient descent.

import math
import random 
newset = []
#The main idea of this is to try and find the least Euclidean distance to each of the points. This can be generalized to n entries, although I
#Blackbird, am too lazy.
#This generates a random set of a hundred ordered pairs.
for i in range(10000):
  newpair = []
  newpair.append(random.randint(1,10**6))
  newpair.append(random.randint(1,10**6))
  newpair = tuple(newpair)
  newset.append(newpair)

testset = [(1,2), (3,4), (5,6)]
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

#This multiplies all of the numbers in a set.
def multiplysets(float, set):
  newset = []
  for i in range(len(set)):
    multipliedtuple = multiply(float,set[i])
    newset.append(multipliedtuple)
  return newset

def unitvector(i,dimensions):
    j = 0
    vector = []
    for j in range(dimensions):
        if j == i:
            vector.append(1)
        else:
            vector.append(0)
    return vector

def zerovector(dimensions):
    j = 0
    vector = []
    for j in range(dimensions):
            vector.append(0)
    return vector

#This talks about how 'bad' it is to try and deviate from that point. The worse it is trying to deviate from that point, the better.
def gradient(point, set, approximation):
    pointset = []
    for i in range(len(point)):
        pointset.append(add(point, multiply(approximation,unitvector(i, len(point)))))
    differences = []
    for i in range(len(point)):
        differences.append((func(point,set) - func(pointset[i],set))*-1/approximation)
    return differences

def normalized(vector):
    sum = (euclidean(zerovector(len(vector)), vector))
    return multiply(1/sum, vector)

def magnitude(vector):
    return euclidean(zerovector((len(vector))), vector)

print(normalized((3,4)))
    

print(gradient((0,0),testset, 1/100))

def main(iterations,set,approximation, learningspeed):
    comparisonpoint = (50,50)
    for i in range(iterations):
        derivative = gradient(comparisonpoint, set, approximation)
        if (i % 20 == 0):
            print(derivative)
        comparisonpoint = add(comparisonpoint, multiply(-approximation*learningspeed*func(comparisonpoint,set)/len(set),normalized(derivative)))
        if (i % 20 == 0):
            print(comparisonpoint, func(comparisonpoint, set),derivative)
    return (comparisonpoint, func(comparisonpoint, set))
        
print(main(200, newset, 1/1000, 20))
