# row,col = (6,6)
# arr = [[0 for i in range(col)] for i in range(row)]
# for i in range(0,row):
#     row = row - 1
#     arr[row][0] = 1
    
# print(arr)



# count = 0
# i = 0
# temp = i + 1
# while i < n-1:
#     if i > temp:
#         temp += 1
#         count += 1
#     i += 1
# print(i)        


# ================================================================
# DAY 2 - P_1

# Pascal Triangle
# ================================================================
# def Pascal(n):
#     arr = [[0 for x in range(n)] for y in range(n)]
    
#     for line in range(0,n):
#         for i in range(0, line + 1):
#             if(i is 0 or line is 0):
#                 arr[line-1][i] = 1
#                 print(arr[line-1][i], end = " ")
#             else:
#                 arr[line][i] = arr[line-1][i-1] + arr[line-1][i]
#                 print(arr[line][i], end = " ")
#         print("\n", end = "")                
                
# n = int(input("Enter the size of Pascal's Triangle : "))
# Pascal(n)


# ================================================================
# DAY 2 - P_1

# Rotate Matrix 
# ================================================================


def Rotate(Matrix):
    for i in range(len(Matrix)):
        for j in range(i, len(Matrix)):
            Matrix[i][j], Matrix[j][i] = Matrix[j][i], Matrix[i][j]
            
    Half = len(Matrix)
    for i in range(int(Half/2)):
        for i in range(Half):
            Matrix[j][i], Matrix[j][Half-1-i] = Matrix[j][Half-1-i], Matrix[j][i]
    
    return Matrix        
            
            



Matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(Rotate(Matrix))





