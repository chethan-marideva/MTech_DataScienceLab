# Assignment: Data Preprocessing and Feature Scaling

# Part A: File Importing and Display

# Q1. Upload a CSV file named student_data.csv which contains the following columns:
# Name, Age, Gender, Score, Attendance, Remarks
# Tip: Create a small dataset manually in Excel or Google Sheets and download as CSV.
# Q2. Read the file into a DataFrame using Pandas and display the first 5 rows.
#import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler, StandardScaler, MaxAbsScaler, Normalizer


df=pd.read_csv('/Users/cm/Desktop/MTech_Assignments/DS_Lab/MTech_DataScienceLab/June8_Lab/student_data.csv') # load csv

#current_dir = os.getcwd()
#print(current_dir)

print(df.head(5)) # Dsiplay first 5 rows 


# Part B: Handling Missing Data
# Q3. Check for missing values in all columns and print the total count.
# Q4. Replace missing values:
# • Numerical columns (Age, Score, Attendance) → Fill with mean
# • Categorical columns (Gender, Remarks) → Fill with mode

print('\n Missing values in columns:\n', df.isnull())  # Display missing values
print('\n Total Count:\n', df.isnull().sum())  #Total of missing values

for col in ['Age','Score','Attendance']:    #Fill with mean
    df[col].fillna(df[col].mean(),inplace=True)

for col in ['Gender', 'Remarks']:           #Fill with mode
    df[col].fillna(df[col].mode()[0], inplace=True)

print('\nMissing Values Filled\n',df)

# Part C: Categorical Data Encoding
# Q5. Convert the Gender column into numeric format using Label Encoding.
# Q6. Convert the Remarks column using One-Hot Encoding.

encodedData = LabelEncoder()
df['Gender_encoded'] = encodedData.fit_transform(df['Gender'])  #label encoding

df = pd.get_dummies(df, columns=['Remarks'], prefix='Remarks')   #one hot encoding

print('\nEncoded Data\n',df)

# Part D: Feature Scaling
# Q7. Apply Min-Max Scaling on Score and Attendance columns and print the scaled result.
# Q8. Apply Standardization (Z-score) on the same columns and print the result.
# Q9. Apply Max Absolute Scaling on these columns and print the result.
# Q10. Apply L2 Normalization row-wise on the original Score and Attendance columns.



features = df[['Score', 'Attendance']].copy()  # extract feature


minmax = MinMaxScaler()
scaled_minmax = minmax.fit_transform(features)
print('\nMin-Max Scaled\n', pd.DataFrame(scaled_minmax, columns=['Score', 'Attendance']))


standard = StandardScaler()
scaled_standard = standard.fit_transform(features)
print('\nStandardized \n', pd.DataFrame(scaled_standard, columns=['Score', 'Attendance']))


maxabs = MaxAbsScaler()
scaled_maxabs = maxabs.fit_transform(features)
print('\nMax Abs Scaled\n', pd.DataFrame(scaled_maxabs, columns=['Score', 'Attendance']))


normalizer = Normalizer(norm='l2')
normalized = normalizer.fit_transform(features)
print('\nL2 Normalized\n', pd.DataFrame(normalized, columns=['Score', 'Attendance']))



# Part E: Summary Statistics
# Q11. Calculate and display the mean and standard deviation for all numerical columns.
# Q12. Calculate the correlation matrix for numerical features in the dataset and explain what it
# means.

print('\nMeans\n', df[['Age', 'Score', 'Attendance']].mean())
print('\nStandard deviations\n', df[['Age', 'Score', 'Attendance']].std())

correlation = df[['Age', 'Score', 'Attendance']].corr()
print('\nCorrelation matrix\n', correlation)

# For the given data set, Based on the co relation matrix , we can conclude
# Attendance strongly linked to score
# May be age is inversely realted to both Score and Attendance