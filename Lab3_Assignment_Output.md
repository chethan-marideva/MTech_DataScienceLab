      Name   Age  Gender  Score  Attendance    Remarks
0    Alice  14.0  Female   85.0        90.0       Good
1      Bob  15.0    Male   78.0        85.0    Average
2  Charlie  14.0     NaN   92.0        95.0  Excellent
3    David   NaN    Male   88.0         NaN       Good
4      Eva  15.0  Female   80.0        88.0        NaN

 Missing values in columns:
     Name    Age  Gender  Score  Attendance  Remarks
0  False  False   False  False       False    False
1  False  False   False  False       False    False
2  False  False    True  False       False    False
3  False   True   False  False        True    False
4  False  False   False  False       False     True
5  False  False   False   True       False    False
6  False  False   False  False       False    False

 Total Count:
 Name          0
Age           1
Gender        1
Score         1
Attendance    1
Remarks       1
dtype: int64


Missing Values Filled
       Name   Age  Gender  Score  Attendance    Remarks
0    Alice  14.0  Female   85.0   90.000000       Good
1      Bob  15.0    Male   78.0   85.000000    Average
2  Charlie  14.0  Female   92.0   95.000000  Excellent
3    David  14.5    Male   88.0   90.666667       Good
4      Eva  15.0  Female   80.0   88.000000    Average
5    Frank  14.0    Male   85.5   92.000000    Average
6    Grace  15.0  Female   90.0   94.000000  Excellent

Encoded Data
       Name   Age  Gender  Score  Attendance  Gender_encoded  Remarks_Average  Remarks_Excellent  Remarks_Good
0    Alice  14.0  Female   85.0   90.000000               0            False              False          True
1      Bob  15.0    Male   78.0   85.000000               1             True              False         False
2  Charlie  14.0  Female   92.0   95.000000               0            False               True         False
3    David  14.5    Male   88.0   90.666667               1            False              False          True
4      Eva  15.0  Female   80.0   88.000000               0             True              False         False
5    Frank  14.0    Male   85.5   92.000000               1             True              False         False
6    Grace  15.0  Female   90.0   94.000000               0            False               True         False

Min-Max Scaled
       Score  Attendance
0  0.500000    0.500000
1  0.000000    0.000000
2  1.000000    1.000000
3  0.714286    0.566667
4  0.142857    0.300000
5  0.535714    0.700000
6  0.857143    0.900000

Standardized 
       Score  Attendance
0 -0.106085   -0.208839
1 -1.591274   -1.775131
2  1.379105    1.357453
3  0.530425    0.000000
4 -1.166935   -0.835356
5  0.000000    0.417678
6  0.954765    1.044195

Max Abs Scaled
       Score  Attendance
0  0.923913    0.947368
1  0.847826    0.894737
2  1.000000    1.000000
3  0.956522    0.954386
4  0.869565    0.926316
5  0.929348    0.968421
6  0.978261    0.989474

L2 Normalized
       Score  Attendance
0  0.686624    0.727013
1  0.676117    0.736794
2  0.695673    0.718358
3  0.696475    0.717581
4  0.672673    0.739940
5  0.680756    0.732510
6  0.691571    0.722308

Means
 Age           14.500000
Score         85.500000
Attendance    90.666667
dtype: float64

Standard deviations
 Age           0.500000
Score         5.090841
Attendance    3.448027
dtype: float64

Correlation matrix
                  Age     Score  Attendance
Age         1.000000 -0.474709   -0.483368
Score      -0.474709  1.000000    0.955816
Attendance -0.483368  0.955816    1.000000
