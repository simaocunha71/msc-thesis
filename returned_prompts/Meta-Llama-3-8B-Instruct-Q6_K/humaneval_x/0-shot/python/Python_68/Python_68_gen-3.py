```
def pluck(arr):
    even_nodes = [(node, i) for i, node in enumerate(arr) if node % 2 == 0]
    if not even_nodes:
        return []
    return min(even_nodes, key=lambda x: (x[0], x[1]))
```



This function first filters the array to get a list of tuples, where each tuple contains a node value and its index. It then checks if the list is empty. If it is, the function returns an empty list. If the list is not empty, it uses the built-in min function with a custom key function to find the tuple with the smallest even value. If there are multiple tuples with the same smallest even value, the function returns the one with the smallest index. The function then returns a list containing the smallest even value and its index. 

For example, if the input array is [4,2,3], the function will return [2, 1], which is the node with the smallest even value (2) and its index (1). If the input array is [1,2,3], the function will also return [2, 1], because 2 is the smallest even value and it has the smallest index. If the input array is [], the function will return [], because there are no even values. 

The time complexity of this function is O(n), where n is the length of the input array, because it needs to iterate over the array once to filter the even nodes and then again to find the smallest even node. The space complexity is O(n), because in the worst case, the function needs to store all the nodes in the even_nodes list. 





This solution uses a list comprehension to create a list of tuples, where each tuple contains a node value and its index. The list comprehension iterates over the input array and checks if each node is even by using the modulo operator. If a node is even, it is added to the list of tuples.

The function then checks if the list of tuples is empty. If it is, the function returns an empty list, because there are no even nodes.

If the list of tuples is not empty, the function uses the built-in min function with a custom key function to find the tuple with the smallest even value. The key function takes a tuple as input and returns a tuple containing the node value and its index. The min function uses this key function to compare the tuples and find the smallest one.

The function then returns