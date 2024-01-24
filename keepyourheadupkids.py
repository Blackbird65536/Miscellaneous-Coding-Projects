import math
import random
import numpy as np

nums1 = []
nums2 = []

for i in range(6000):
  skill = random.randint(1,10**9)
  luck = random.randint(1,10**9)
  nums1.append(0.95*skill + 0.05*luck)
  nums2.append(skill)

def maximum(n):
  highest = -1
  orderedpair = (-1,-1)
  for i in range(len(n)):
    if n[i] > highest:
      highest = n[i]
      orderedpair = (highest, i)
    else: 
      continue
  return orderedpair
  

def multimaximum(m,n):
  maximumset = []
  for i in range(m):
    relativemaximum = maximum(n)
    maximumset.append(relativemaximum)
    n[relativemaximum[1]] = -1
  return maximumset


pureskill = multimaximum(300, nums2)
tinyluck = multimaximum(300,nums1)
pureskillindex = []
tinyluckindex = []
i = 0
for i in range(len(pureskill)):
  pureskillindex.append(pureskill[i][1])
  tinyluckindex.append(tinyluck[i][1])
  
print(pureskillindex)
print(tinyluckindex)

        

concatenated = np.concatenate((pureskillindex, tinyluckindex))

print(600 - len(list(set(concatenated))))





    
    
      
      
    
  
