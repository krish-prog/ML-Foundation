'''import numpy as np

X = np.array([
    [10, 20],
    [20, 30],
    [30, 40],
    [40, 50]
])

print(type(X))        # should be numpy.ndarray
print(X.shape)        # should be (4, 2)

x_mean = np.mean(X, axis=0)
sub = X - x_mean

print(sub)
print(X.shape)

'''
'''
import numpy as np
X =np.array(
    [
 [10, 50, 30],
 [20, 60, 40],
 [30, 70, 50],
 [40, 80, 60]
]
)

mean_x = X.mean(axis=0)
mask = mean_x > 45
print(mask)

selected =X[:,mask]
'''














'''

# lets do 5 task of numy and understand it 
import numpy as np
X =np.array(
    [
 [10, 20],
 [20, 30],
 [30, 40],
 [40, 50]
]
)

x_mean_col= X.mean(axis=0)
print(x_mean_col)

sub = X - x_mean_col

print(sub)


x_mean_row = X.mean(axis=1)
print(x_mean_row)

# masking 

row_mask = x_mean_row > 30 
print(row_mask)

# this is how we can select those rows whose mean is greater than 30 
selected = X[row_mask,:]
print(selected)'''
'''
# task 5
import numpy as np
Xx =np.array(
[
 [5, 100, 15],
 [6, 110, 16],
 [7, 120, 17]
])
mean_x = Xx.mean(axis=0)
print(mean_x)
maskk = mean_x > 20 

select_col = Xx[:,maskk]

print(select_col)
'''




# where () tasks

# task 1 values < 6 → -1

#else → keep original value

import numpy as np
'''
X = np.array([2, 8, 5, 12])



clena_x = np.where(X<6,-1,X)

print (clena_x)'''

# Task 2 

'''Create a new array where:

score >= 50 → 1

score < 50 → 0

(Think: pass/fail feature)'''

'''
scores = np.array([45, 78, 60, 30, 90])
new_array = np.array(

    np.where(scores>=50,1,0)
)

print(new_array)

'''

# task 3 
'''Replace values:

if value > 25 → keep value

else → put 0'''

'''
import numpy as np

X = np.array([10, 20, 30, 40])
clean = np.where(X>25,X,0)
print(clean)'''





'''
Create a new array called final_scores using ONLY np.where() such that:

Rules

1️⃣ If score >= 80 → keep the score
2️⃣ If score >= 50 and < 80 → replace with 50
3️⃣ If score < 50 → replace with 0

'''
'''
X = np.array([95, 40, 67, 82, 30, 55])
clean = np.where(X>=80,X,
                  np.where(X>= 50,50,0) )

print(clean)'''

 
'''
 # standardization
X = np.array([
 [10, 100],
 [20, 200],
 [30, 300]
])

mean_x = np.mean(X, axis=0)

stdd = np.std(X, axis=0)



standrization = (X-mean_x)/stdd

print(standrization)'''


'''
import numpy as np
from sklearn.preprocessing import StandardScaler  # pyright: ignore[reportMissingModuleSource]


X = np.array([
 [10, 100],
 [20, 200],
 [30, 300]
])
scalar = StandardScaler()

X_scalar = scalar.fit_transform(X)

print(X_scalar)'''




'''TASK 1 — NumPy (centering + axis clarity)
Given:


Task:

Compute column-wise mean

Center the data (subtract column mean)

Print the centered matrix'''

#answer
 
'''
import numpy as np

X = np.array([
    [10, 20],
    [20, 30],
    [30, 40],
    [40, 50]
])
X_mean = np.mean(X, axis = 0)
print(X_mean)
centerize = (X-X_mean)
print(centerize)
'''


'''
🧪 TASK 2 — NumPy (masking + selection)

Task:

Compute column-wise mean

Create a mask for columns whose mean > 20

Select only those columns from X '''

'''
#answer 
X = np.array([
    [5, 100, 15],
    [6, 110, 16],
    [7, 120, 17],
    [8, 130, 18]
])

X_mean = np.mean(X,axis=0)
mask = X_mean > 20

selected_column = X[:,mask]

print(selected_column)
'''

'''

🧪 TASK 3 — sklearn (standardization, real ML style)
Given:
import numpy as np
from sklearn.preprocessing import StandardScaler

Task:

Create a StandardScaler

Use fit_transform to standardize X

Print:

standardized data

column-wise mean

column-wise std

What the result should show:

Mean ≈ 0

Std ≈ 1

Different scales handled automatically '''

#answer 


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X = np.array([
    [1, 1000],
    [2, 1500],
    [3, 2000],
    [4, 2500]
])

standarization = scaler.fit_transform(X)
print(standarization)