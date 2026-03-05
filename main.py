# #---------------1 задача--------------#


x1 = [9,9,1,15,1,9,3,4,6,3]
x2 = [4,16,11,11,4,12,2,3,5,3]
x3 = [2,17,18,16,9,16,4,6,7,1]
x4 = [4,17,10,14,16,14,3,7,3,1]
x5 = [2,5,18,8,18,5,1,6,1,3]
x6 = [7,17,1,8,8,18,7,3,2,7]
x7 = [3,1,2,3,2,3,6,5,3,2]
x8 = [6,2,2,1,1,5,4,2,1,1]
x9 = [2,1,3,7,4,3,5,2,4,4]
x10 = [3,3,5,2,3,2,3,1,1,2]
x = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]

node0 = []
duration = 0
distr_list = []
current = 0

def jobs(current, node, duration):
    if len(node) == 10:
        distr_list.append([duration, node])
    for i in range(10):
        if (i not in node) and (len(node)<10):
            jobs(current+1, node+[i], duration + x[current][i])
            
jobs(current, node0, duration)
print(min(distr_list))


                        

# #---------------2 задача--------------#

# my_map = [[0, 8, 9, 1, 3], 
#           [5, 0, 7, 4, 8], 
#           [6, 7, 0, 4, 2], 
#           [4, 7, 1, 0, 4], 
#           [1, 2, 5, 5, 0]] 

# current = 0
# node = []
# dist = 0
# dist_l = []


# def route(current, node, dist):
#     node = node.copy()
#     node.append(current)
#     if len(node) == 5:
#         dist_l.append(dist+my_map[current][0])
#     if len(node) == 4:
#         route(4, node, dist + my_map[current][4])
#     for i in range(5):
#         if (i not in node) and (i!=4):
#             route(i, node, dist + my_map[current][i])
        
#     return 
# route(current, node, dist)
# print(f"Решение 2-й задачи: {min(dist_l)}")

#---------------3 задача--------------#

# my_map2 = [[1,2,18], 
#            [1,3,19], 
#            [1,4,17], 
#            [2,4,13],
#            [2,6,14],
#            [3,6,15],
#            [3,7,16],
#            [4,7,17],
#            [4,8,18],
#            [5,6,21],
#            [5,9,19],
#            [6,9,22],
#            [6,10,21],
#            [7,10,23],
#            [7,11,18],
#            [8,7,21],
#            [8,11,17],
#            [9,12,32],
#            [10,12,33],
#            [10,13,37],
#            [11,13,36],
#            [10,14,41],
#            [12,14,32],
#            [13,14,31]]

# cur = 1
# length = 0
# len_list = []
# node1 = []

# def way(cur, len_, node1):
#     node1 = node1.copy()
#     node1.append(cur)
#     if cur == 14:
#         len_list.append([len_, node1])
#         return
#     else:
#         options = [o for o in my_map2 if o[0]==cur]
#         for _ in options:
#             way(_[1], len_+_[2], node1)
#         return
        
        
# way(cur, length, node1)
# print(f"Решение 3-й задачи: {min(len_list)}")
    