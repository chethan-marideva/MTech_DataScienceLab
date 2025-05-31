import numpy as np
import pandas as pd

# Q1 : Create a 2D NumPy array and extract a subarray

inputArray = np.array([[10,20,30,40,50],[60,70,80,90,100]])  # 2X5  
sub_array = inputArray[0:2,1:4] # Extract

print('Given 2x5 Array : \n', inputArray)
print('\n Sub Array :\n',sub_array)


# Q2 : Modify elements using slicing and broadcasting


inputArray[0, :] = 99 #  set all elements in row 1 to 99
print('\n Row Modified \n ',inputArray)

inputArray[:,2]= -99
print('\n Column Modified \n',inputArray)


#Slice -
inputArray[1:, 1:4] = -1  # row 1 , index 1-3 with -1
print('\n Slice example',inputArray)

inputArray[1, :] = [1, 2, 3, 4, 5]  # replace row 2 
print('\n Broadcasting example',inputArray)

# Q 3: Create a dataframe with Name Age Marks

data = {
    'Name': ['Chethan M', 'Pavan', 'Sachin', 'Rajiv'],
    'Age': [37, 36, 35, 45],
    'Marks': [65, 100, 100, 35]
}


df = pd.DataFrame(data)

print('\n',df)

# Q4 : filter students with marks > 80 and sort by age

# Filter 
filtered_df = df[df['Marks'] > 80]

# Sort by Age
sorted_df = filtered_df.sort_values(by='Age')

print('\n Students with Marks > 80 and Sorted by thier Age\n')
# Display result
print(sorted_df)

#Q5 : # Export to CSV
sorted_df.to_csv('students.csv', index=False)
