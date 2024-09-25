import pandas as pd
a = [1,7,2]
myvar = pd.Series(a)
print(myvar)

'''
0    1
1    7
2    2
dtype: int64
'''

import pandas as pd
a = [1,7,2]
myvar = pd.Series(a)
print(myvar[0])

#O/P - 1

import pandas as pd
df = pd.DataFrame({'A':[1,2,None,4],'B':[5,None,7,None]})
print(df)
print("\n")
df.fillna(0,inplace=True)
print(df)

'''
# -O/P

     A    B
0  1.0  5.0
1  2.0  NaN
2  NaN  7.0
3  4.0  NaN


     A    B
0  1.0  5.0
1  2.0  0.0
2  0.0  7.0
3  4.0  0.0

'''


import pandas as pd
df =pd.DataFrame({'A':[1,2,None,4],'B':[5,None,7,3]})
print(df)
print("\n")
df.dropna(inplace=True)
print(df)

'''
#-O/P

     A    B
0  1.0  5.0
1  2.0  NaN
2  NaN  7.0
3  4.0  3.0


     A    B
0  1.0  5.0
3  4.0  3.0

'''