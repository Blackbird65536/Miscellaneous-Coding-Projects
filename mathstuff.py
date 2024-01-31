import math
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

#complex numbers

def cis(real):
    return (math.cos(2*math.pi*real),math.sin(2*math.pi*real))
def polar(radius, real):
    return multiply(radius, cis(real))

#matrices 

def vectormultiplication(matrix,vector):
  newvector = []
  for j in range(len(matrix)):
    sum = 0
    for i in range(len(vector)):
        sum += vector[i]*matrix[i][j]
    newvector.append(sum)
  return tuple(newvector)
  
identitymatrix = [(1,0,0),(0,1,0), (0,0,1)]
print(vectormultiplication(identitymatrix, (13,3,5)))
