
def can_arrange(arr):
    max_index = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            max_index = i
    return max_index

print(can_arrange([1,2,4,3,5]))  # 3
print(can_arrange([1,2,3]))  # -1
print(can_arrange([5,4,3,2,1]))  # 1
print(can_arrange([1,2,4,5,3]))  # 4
print(can_arrange([1,3,5,4,2]))  # 3
print(can_arrange([1,4,6,5,3,2]))  # 5
print(can_arrange([10,20,30,40,50]))  # -1
print(can_arrange([50,40,30,20,10]))  # 4
print(can_arrange([1,2,3,5,4]))  # 4
print(can_arrange([1,2,3,4,5]))  # -1
print(can_arrange([5,1,2,3,4]))  # 1
print(can_arrange([5,4,2,3,1]))  # 2
print(can_arrange([1,2,5,4,3]))  # 3
print(can_arrange([1,2,5,3,4]))  # 3
print(can_arrange([1,3,2,5,4]))  # 2
print(can_arrange([1,3,2,4,5]))  # 3
print(can_arrange([1,2,3,6,5,4]))  # 4
print(can_arrange([1,2,3,7,6,5,4]))  # 5
print(can_arrange([1,2,3,8,7,6,5,4]))  # 6
print(can_arrange([1,2,3,9