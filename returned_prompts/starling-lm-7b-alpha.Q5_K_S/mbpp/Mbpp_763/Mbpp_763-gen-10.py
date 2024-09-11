def find_min_diff(arr,val):
    arr = sorted(arr)
    diff = 99999999999999999999999999999999999
    for i in range(len(arr)):
        diff = min(diff,abs(arr[i]-val))
    return diff

print(find_min_diff((1,5,3,19,18,25),6))

#output: 1

"""
Explanation: 
In this program, we first sort the array using the sorted() function. Then we initialize the diff variable to a very large value. We then loop through each element in the array and check the distance between the current element and the value we want to compare. We update the diff variable if we find a smaller distance. Finally, we return the diff value, which is the minimum distance between any two elements in the array.
"""




# Python3 program to find the minimum difference
# between two elements in a given array

# Function to find the minimum difference
def find_min_diff(arr,val):
    # Sort the array
    arr = sorted(arr)

    # Initialize the difference
    diff = 99999999999999999999999999999999999

    # Loop through the array and find the minimum difference
    for i in range(len(arr)):
        diff = min(diff, abs(arr[i] - val))

    return diff

# Driver Code
if __name__ == "__main__":
    arr = [1, 5, 3, 19, 18, 25]
    val = 6
    print(find_min_diff(arr, val))

"""
Explanation: 
In this program, we first sort the array using the sorted() function. Then we initialize the diff variable to a very large value. We then loop through each element in the array and check the distance between the current element and the value we want to compare. We update the diff variable if we find a smaller distance. Finally, we return