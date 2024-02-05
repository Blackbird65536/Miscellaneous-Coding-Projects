import math
import random 
newset = []
#The main idea of this is to try and find the least Euclidean distance to each of the points. This can be generalized to n entries, although I
#Blackbird, am too lazy.
#This generates a random set of a hundred ordered pairs.
def newntuple(length, number):
    tupleset = []
    for i in range(number):
        newtuple = []
        for i in range(length):
            newtuple.append(random.randint(1,10**6))
        tupleset.append(newtuple)
    return tupleset

newset = newntuple(2, 100)

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

#this will give the score of the clusters that we have. 

#k is the number of clusters.

def initialset(k, set):
    intial = []
    cluster = []
    for i in range(k):
        intial.append([])
    for j in range(len(set)):
        chosencluster = intial[j % k]
        chosencluster.append(set[j])
    return intial

def centroid(set):
    center = zerovector(len(set[0]))
    for i in range(len(set)):
        center = add(center, set[i])
    center = multiply(1/len(set), center)
    return center

def score(k,set):
    initializer = initialset(k, set)
    print("Intializer")
    print(initializer)
    means = []
    sums = 0
    for i in range(k):
        print(str(i+1) + " th cluster")
        centroid = zerovector(len(initializer[0][0]))
        for j in range(len(initializer[i])):
            centroid = add(centroid, initializer[i][j])
        centroid = multiply(1/len(initializer[i]), centroid)
        means.append(func(centroid,set))
        sums += func(centroid,set)
    return (sums, means)

def setscore(set):
    means = []
    sum = 0
    for i in range(len(set)):
        chosencluster = set[i]
        mean = centroid(set[i])
        sum += func(mean, set[i])
    return sum

print(setscore(initialset(10,newset)))

print(score(10, newset))

#Part II, initialize trading.

#We are trading from cluster a to cluster b, from a point vector.
def trade(vector,a,b,clusterset):
    clustersender = clusterset[a]
    clusterreceiver = clusterset[b]
    clustersender.remove(vector)
    clusterreceiver.append(vector)
    
def main(iterations, k, set):
    comparisoncluster = initialset(k, set)
    print(comparisoncluster)
    #We want to sweep this up iterations times.
    for i in range(iterations):
        #We want to look at every single cluster and every single elemnt of that cluster
        for j in range(len(comparisoncluster)):
            for t in range(len(comparisoncluster[j])):
                for l in range(len(comparisoncluster)):
                    negotiatingcluster = comparisoncluster
                    if l == j:
                        continue
                    else: 
                        newnegotiatingcluster = trade(negotiatingcluster[j][t], j, l, negotiatingcluster )
                        if score(k,newnegotiatingcluster) << score(k,negotiatingcluster):
                            negotiatingcluster = newnegotiatingcluster
                        else: continue
    means = []
    for m in range(len(comparisoncluster)):
        means.append(centroid(comparisoncluster[m]))        
    return (comparisoncluster,means)
            
print(main(200, 10, newset))            



                
        
        
    

#we then have a few parts. Part 1: We will then find the mean of the clusters, such that the clusters are 'sort of close together'.

#Part 2: We will then assign a scoring system based on the weighing of the means. 