

'''a= [5, 12, 7,11, 18]
b= []
for i in a: 
    if i > 10:
        b.append(i)

print("this is the elemets in", b)
        

avgb= sum(b)/ len(b)


print("this is the average of the b variable", avgb)'''



''''

t= [2, 4, 6, 8, 10]

avgt= sum(t)/len(t)
print(avgt, "this is the average of list t")
 # need number greater than 6 because it is the avg of the list t 
c = []
# c  to collect the numbers 

# conditition with loop 

for i in t:
    if i > 6:
        c.append(i)

print (c)
    
avgc = sum(c)/len(c)

print(avgc,"this is the average of c ")



m=[]

for i in c:
    if i > avgc:
        m.append(i)
  


print(m)

'''

'''
nums = [12, 5, 22, 9, 17]

max1 = float('-inf')
max2 = float('-inf')
max3 = float('-inf')

for n in nums:
    if n > max1:
        max3 = max2
        max2 = max1
        max1 = n
    elif n > max2:
        max3 = max2
        max2 = n
    elif n > max3:
        max3 = n

print(max3)

'''
      
"""

# find smallest and the second smallest form this list 
nums = [12, 5, 22, 9, 17]
min_num = nums[0]
sec_num = nums[0]

for n in nums: 
    if n < min_num:
        sec_num = min_num
        min_num = n
    elif n < sec_num and sec_num != min_num: 
        sec_num = n

print(min_num, sec_num)


"""
        
        
'''
    # Problem: Find the Top 3 Numbers in a List (Without sort() or max())
nums = [12, 5, 22, 9, 17]
max_1 = nums[0]
max_2 = nums [0]
max_3 = nums [0]
 
for n in nums:
    if n > max_1:
        max_2 = max_1
        max_3 = max_2
        max_1 = n
    elif n > max_3 and n != max_2:
        max_2 = n


print(max_3, max_1, max_2)
    
'''
'''
# Given a list of numbers, count how many of them are even.
nums =[3, 10, 7, 8, 12, 5]
count = 0
for n in nums:
    if n % 2 == 0:
            count+= 1 

print (count)
'''

'''        
Find the largest number manually

Find the smallest number manually

Print:
'''
'''
nums = [14, 3, 27, 8, 19]
largest= nums[0]
smallest = nums[0]

Dif = largest - smallest

for n in nums:
    if n > largest:
        largest = n 
    
    if n < smallest:
        smallest = n 
            
print("this is the largest value ",largest)
print(" this is the smallest value", smallest)  
print(" the difference between largest and smallest is ", Dif)

'''
'''
nums = [14, 3, 27, 8, 19]

max_1 = nums[0]
max_2 = nums[0]

for i in nums:
    if i > max_1:
        max_2 = max_1
        max_1 = i

    elif i > max_2:
        max_2 = i 


print(max_1, max_2)

'''
'''
nums = [14, 3, 27, 8, 19]

s1 = float('-inf')
s2 = float('-inf')
s3 = float('-inf')

for i in nums:
    if i > s1:
        s2 = s1
        s3 = s2 
        s1 = i 
    elif i  > s2:
        s3 = s2 
        s2 = i 
    elif i > s3: 
        s3 = i
print(s1,s2,s3)
'''

'''
nums = [3, 5, 3, 8, 5, 3]
count = {}

for n in nums:
    if n in count:
        count[n] += 1 

    else:
        count[n]= 1

     



for key in count:
    print(key, "appears", count[key], "times")
'''


"""
Given a list of numbers, find the first number that appears more than once (the first duplicate).
If no number repeats, print “No duplicates”.

Example:
nums = [3, 5, 2, 4, 5, 2] → output should be 5 (because 5 is the first number that repeats)
"""
'''
nums = [3, 5, 2, 4, 5, 2]

seen = set()

for n in nums:
    if n in seen:
        print("First duplicate:", n)
        break
    seen.add(n)
else:
    print("No duplicates")

    '''

    
'''
Given a list of numbers, count how many numbers appear exactly once.

Example:
nums = [3, 5, 3, 2, 8, 2, 9]
→ numbers that appear once = 5, 8, 9
→ output = 3


    
nums = [3, 5, 3, 2, 8, 2, 9]
once = []
count = {}

for n in nums:
    if n not in count:
        count[n] = 1        # FIRST TIME: create key
    else:
        count[n] += 1       # NEXT TIMES: incre

print(count)
        
for key in count:
    if count[key] == 1:
        once.append(key)

print("Numbers appearing once:", once)
    
    
print(once)'''

''' Given a list of numbers, find the first number that appears more than once.

If no number repeats, print "No duplicates".

Example:

nums = [3, 5, 2, 4, 5, 2]
# Output: 5 (because 5 is the first number that repeats)'''

'''

nums = [3, 5, 2, 4, 5, 2]

count={}

for n in nums:
    if n not in count:
        count[n] = 1 

    else : count[n] += 1
    


for key in count:
    if count[key]==2:
        print(key,count[key])
        break;
'''
'''
nums = [4, 3, 2, 3, 4, 8, 9]
count= {}

for n in nums:
    if n not in count:
        count[n] = 1 
        
    else: count[n] += 1 
high = 0
for i in count:
    if count[i]> high:
            high = count[i]

for key in count:
    if count[key] == high:
        print("Most frequent number is", key, "appearing", high, "times")

'''
'''
def print_greater_than_5():
    nums = [2, 7, 4, 9, 1, 6]
    # your loop here
    for n in nums:
        if n > 5:
            print(n)


print_greater_than_5()
'''

'''
# average = 6
# output → [8, 10]

gum= [3,5,6,7,7]
    
def high(q):
    new_list= []


    for n in q:
        if n > 5:
            new_list.append(n)

    return (new_list)

print(high(gum))


'''
'''
list = [3,6,9,2]

def High_ave(q):
    new_list = []
    count = 0
    q_ave = sum(q)/len(q)
    
    for n in q: 
        if n > q_ave:
            new_list.append(n)
            count+=1

        

    return(new_list,count)
    
'''


'''
Write a function that:

takes a list of numbers

returns two things:

sum of even numbers

sum of odd numbers

'''
'''
num= [1, 2, 3, 4, 5]
    

def ri(q):
    
    sum_even = 0
    sum_odd = 0 

    for n in q:
        if n % 2 == 0 :
            sum_even += n

        else: sum_odd += n

    return(sum_even,sum_odd)


print(ri(num))

    
'''
    
'''   
Count of numbers greater than average

Sum of numbers less than or equal to average

'''

'''
nums = [2, 4, 6, 8, 10]

def ti(q):
    count = 0 
    sum_1 = 0 
    avg= sum(q)/len(q)



    for n in q: 
        if n <= avg:
            sum_1 = sum_1 + n

        else:
            count+=1


    return(avg,count,sum_1)



print("avg","count","sum", ti(nums))

'''

'''

# find min and max value then find difference between them avg and count num larger than average

nums = [7, 2, 9, 4, 1]

def find_max_min_difference(w):
    minn = w[0]
    maxx = w[0]
    avg = sum(w)/len(w)
    count = 0


    for n in w: 
        if n > maxx:
            maxx = n

        if n > avg:
            count += 1

        if n < minn: 
            minn = n

    difference = maxx - minn
        
    return maxx,minn,difference,count




print(find_max_min_difference(nums))

'''
'''
dataa = [ 1,4,5,7,12,54,67,75,45]

def normalize(v):
    minn =v[0]
    maxx = v[0]

    normalized = []

    for n in v:
        if n > maxx:
            maxx = n
        
        if n < minn:
            minn = n
    
    


    for n in v :
        
        gor = (n-minn)/(maxx-minn) 

        normalized.append(gor)

    return(normalized)






print(normalize(dataa))


'''
'''
#this is list comprihenson 
nums = [1, 2, 3, 4, 5, 6]


even_list = [n for n in nums if n % 2 == 0]

print(even_list)
'''

# Given a list of numbers,
#  return a list of (index, value) where the value is greater than the average of the list.
'''
nums = [1, 2, 3, 4, 5, 6]
avg = sum(nums)/ len(nums)



result = [(i, n) for i, n in enumerate(nums) if n > avg]

print(result)
'''
'''
nums = [1, 2, 3, 4]
squares = [1, 4, 9, 16]

for s in zip(nums,"squared is ",squares):
    print(s)
'''

'''
names = ["Ram", "Shyam", "Hari"]
scores = [78, 85, 92]

result = [(i, name, score) for i, (name, score) in enumerate(zip(names, scores)) if score > 80]


print(result)

    '''
'''
# task 2
#Return (index, value) for values greater than average.
# expected → [(3, 40), (4, 50)]
nums = [10, 20, 30, 40, 50]
avg = sum(nums)/len(nums)
for i,n in enumerate(nums):
    if  n > avg:
        print(i,n)
# one line result 
ts_2 =[(o,w) for o,w in enumerate(nums) if w > avg ]
print(ts_2)

# task 3 
#From two lists, return names with score > 80.
names = ["Ram", "Shyam", "Hari"]
scores = [78, 85, 92]

for (name,score) in zip(names,scores):
    if score> 80:
        print(name)
# one line result 
t3_result = [name for name,score in zip(names,scores) if score > 80 ]
print(t3_result)


# task 5

nums = [10, 20, 30]
minn =min(nums) 
maxx =max(nums)
result_task5 = [(g-minn)/(maxx-minn) for g in nums  ]
print("task 5 result " ,result_task5)
'''
'''nums = [5, 10, 15, 20, 25]

def re(q): 
    qavg = sum(q)/ len(q)
   
    selected = [n for n in q if n > qavg ]

    minn = min(q)
    maxx = max(q)
    norma = [(n-minn) / (maxx - minn) for n in selected] 
    count = len(selected)

    return(qavg,count,selected,norma)


avg, count, selected, normalizatied = re(nums)

print(avg,count,selected, normalizatied)
'''



"""The average

A list of (index, value) for values above the average

A normalized version of only those selected values (0–1 ) scale

"""
'''
nums = [4, 8, 15, 16, 23, 42]
avg = sum(nums)/ len(nums)
mmin = min(nums)
mmax = max(nums)
new_list =[n for i,n in enumerate(nums)if n > avg]
normalize = [(n-mmin)/ (mmax - mmin) for n in new_list]

print(new_list,normalize)'''


import numpy as np

X = np.array
[
 [10, 20],
 [20, 30],
 [30, 40],
 [40, 50]
]
 
x_mean = np.mean(X)

sub = X - x_mean


print(sub)


