# coding: utf-8

# #### 1. 加油站問題：從A到B，中間有n個加油站，每次加油後，可跑L公里，請問最少需要加多少次油？
# 

# In[14]:

x = [0,200,375,550,750,950]
L = 400 #distance with full tank
n = 4 #station

current_loc = 0
number_Refill = 0

while current_loc <= n:
    last_loc = current_loc
    while current_loc <= n and x[current_loc+1]-x[last_loc]<= L:
        current_loc += 1
    
    if x[current_loc] < x[len(x)-1]:
        print('Refill at %s'%(x[current_loc]))
    
    
    if current_loc == last_loc:
        print('impossible')
    
    if current_loc <=n:
        number_Refill += 1

print (number_Refill)


.....
....
.....