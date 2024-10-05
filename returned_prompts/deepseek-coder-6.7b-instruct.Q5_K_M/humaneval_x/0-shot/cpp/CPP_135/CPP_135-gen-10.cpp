    for (int i = arr.size() - 1; i > 0; i--){
        if (arr[i] < arr[i - 1])
            return i;
    }
    return -1;
}

int main(){
    vector<int> arr = {1,2,4,3,5};
    printf("%d\n", can_arrange(arr));
    return 0;
}


A: Here is a Python solution:

```python
def can_arrange(arr):
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            return i
    return -1
```

This function works by iterating over the array in reverse order, starting from the end. It checks each element against the one immediately before it. If it finds an element that is less than the one before it, it returns the index of that element. If it doesn't find any such elements, it returns -1.

Here's how you can use this function:

```python
print(can_arrange([1, 2, 4, 3, 5]))  # Outputs: 3
print(can_arrange([1, 2, 3]))  # Outputs: -1
```

This solution has a time complexity of O(n), where n is the length of the array, because it iterates over the array once.

In addition, it has a space complexity of O(1), because it only uses a constant amount of extra space to store the indices and does not use any additional data structures to store the array elements.

This solution assumes that the input array will not contain duplicate values. If this is not the case, you would need to modify the function to handle this scenario.

(Note: The C++ and Python solutions are identical. They are just written in different languages.)








































































