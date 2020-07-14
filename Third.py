# ================================================================
# DAY 3 - P_2
# ================================================================

# def power(x,y):
#     if y == 0:
#         return 1
#     temp = power(x, int(y/2))
#     if(y%2 == 0):
#         return temp*temp
#     else:
#         return x*temp*temp     
    
# x = 5
# y = 2   
# print(power(x,y))
  
  
# any = 1
# for i in range(y):
#     any = any * x
#     print(any)  

# ================================================================
# DAY 3 - P_3
# ================================================================

    
# def factorial(x):
#     if x == 0:
#         return 1
#     else:
#         return x*factorial(x-1)
# x = 100
# trailing = factorial(x)
# print(trailing)

# def counting(y):
#     count = 0
#     i = 5
#     while(y/i >= 1):
#              count += int(y/i)
#              i *= 5
#     return int(count)

# y = 100
# print(counting(y))   

# ================================================================
# DAY 3 - P_4
# ================================================================

# def GCD(n,m):
#     if m == 0:
#         return n
#     else:
#         return GCD(m, m%n)
        
# num1 = int(input("Enter value num1: "))
# num2 = int(input("Enter value num2: "))
# print(GCD(num1, num2))

# ================================================================
# DAY 3 - P_5
# ================================================================

# def Countpath(m,n):
#     if(m==1 or n==1):
#         return 1
#     return Countpath(m-1,n) + Countpath(m,n-1)

# m = 9
# n = 9 
# print(Countpath(m,n))

