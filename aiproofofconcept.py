import math
sets = [(1,2), (3,4), (5,6), (1,7), (8,11)]

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
    comparisonpoint = (0,0)
    for i in range(iterations):
        derivative = error(comparisonpoint, guesses, set)
        if (derivative[0] <= 0):
            print(comparisonpoint)
            break
        else:
            direction = derivative[1]
            comparisonpoint = add(comparisonpoint, multiply((learningspeed)**i,multiply(func(comparisonpoint,set)/derivative[0],cis(derivative[1]/guesses))))
    return comparisonpoint

print(ai(800, sets, 200, 0.96))
                        
