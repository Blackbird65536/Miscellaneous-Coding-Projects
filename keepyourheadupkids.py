import math
import random

print(random.randint(1, 10**6))

nums1 = []
nums2 = []

for i in range(35000):
  skill = random.randint(1,10**9)
  luck = random.randint(1,10**9)
  nums1.append(0.99*skill + 0.01*luck)
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
  
print(maximum([1,2,3,4,5,6]))
  

def multimaximum(m,n):
  maximumset = []
  for i in range(m):
    relativemaximum = maximum(n)
    maximumset.append(relativemaximum)
    n[relativemaximum[1]] = -1
  return maximumset
  
print(multimaximum(2, [1,2,16,4,5,3]))
print(multimaximum(12, nums1))
print(multimaximum(12, nums2))




    
    
      
      
    
  
