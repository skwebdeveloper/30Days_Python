# ================================================================
# DAY 1 - P_1
# ================================================================


# listing = [0,0,0,0,1,1,1,2,2,2,2,2,2,0]

# listone = []


# for i in listing:
#     if i not in listone:
#          listone.append(i)
#     else:
#         continue 


# ================================================================
# DAY 1 - P_2
# ================================================================
# def sorted(listing, n):
#     count0 = 0
#     count1 = 0
#     count2 = 0
#     for i in range(0,n):
#         if listing[i] == 0:
#             count0 += 1
#         if listing[i] == 1:
#             count1 += 1            
#         if listing[i] == 2:
#             count2 += 1            
    
#     for i in range(0,count0):
#         listing[i] = 0
#     for i in range(count0, (count0+count1)):
#         listing[i] = 1
#     for i in range((count0+count1),n):
#         listing[i] = 2                
#     return


# def printing(listing,n):
#     for i in range(0,n):
#         print(listing[i], " ",end="")

# listing = [0,0,1,2,1,2,1,1,1,0,0,0]
# length = len(listing)
# sorted(listing, length)
# printing(listing,length)



# ================================================================
# DAY 1 - P_3
# ================================================================

# listing = [1,1,2,2,3,4,1,3]
# count = 1
# listing.sort()
# print(listing)

# for i in listing:
#     if count == 1:
#         print(i, " ", end=" ")
#         count += 1
#     else:
#          print(count, " ", end=" ")
#          count += 1



# ================================================================
# DAY 1 - P_4
# ================================================================






# ================================================================
# DAY 1 - P_5
# ================================================================

# def KadaneAlgo(list1, n):
#     max_size = 0
#     max_end_here = 0
#     for i  in range(0,n):
#         max_end_here = max_end_here + list1[i]
#         if max_end_here < 0:
#             max_end_here = 0
#         elif max_size < max_end_here:
#             max_size = max_end_here
#     return max_size        


# list1 = [-4,23,-90,34,2,8,34,-7,23,-34]
# print("Hell", KadaneAlgo(list1, len(list1)))


# ================================================================
# DAY 1 - P_6
# ================================================================

# Use of Stack Best Problem asked by Google, Microsoft