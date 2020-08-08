# Transpose a Matrix


X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

#  rows
for i in range(len(X)):
   #  columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)