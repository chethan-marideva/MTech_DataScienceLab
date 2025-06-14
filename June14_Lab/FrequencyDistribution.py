#Example 1: Suppose we have a series with mean of 20 and a variance of 100. Find out the Coefficient of Variation.

import math 

mean=20
variance=100

standard_deviation =math.sqrt(variance)
#print(standard_deviation)

cv = (standard_deviation/mean)*100

print('Co effiecnt of variation is:',cv)


#Example 2: Given two series with Coefficients of Variation 70 and 80. The means are 20 and 30. Find the values of standard deviation for both series.

cv1= 70
cv2 =80

mean1=20
mean2=30

sd_1= (cv1/100)*mean1
sd_2=(cv2/100)*mean2

print('\n standard deviation of 1st series:',sd_1)
print('\n standard deviation of 1st series:',sd_2)


#Example 3: Draw the frequency distribution table for the following data: 2, 3, 1, 4, 2, 2, 3, 1, 4, 4, 4, 2, 2,2


from collections import Counter

data = [2, 3, 1, 4, 2, 2, 3, 1, 4, 4, 4, 2, 2]

frequency = Counter(data)

print('\nFrequency')

for n, f in sorted(frequency.items()):
    print(n,'\t',f)


#Example 4: The table below gives the values of temperature recorded in Bangalore for 25 days in summer. Represent the data in the form of less-than-type cumulative frequency distribution:

data = [22, 23, 21, 27, 20, 25, 20, 24, 23, 27,
        37, 25, 34, 32, 26, 29, 29, 38, 34, 29,
        23, 31, 20, 29, 22]

sorted_data = sorted(data)
#print(sorted_data)

from collections import Counter

frequency = Counter(data)
print('\n',frequency)



unique_vals = sorted(frequency.keys())  

cumulative = 0
cumulative_table = []

for val in unique_vals:
    cumulative += frequency[val]
    cumulative_table.append((f"Less than {val+1}", cumulative))    


print("Class Cumulative Frequency")
for row in cumulative_table:
    print(f"{row[0]}\t{row[1]}")


