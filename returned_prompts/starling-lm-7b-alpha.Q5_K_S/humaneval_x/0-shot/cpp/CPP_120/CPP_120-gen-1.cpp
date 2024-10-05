
/*
The maximum k numbers in an array are the k largest numbers.
To find the k largest numbers, we can sort the array in ascending order
and then pick the last k elements.

For example, consider the array {-3, -4, 5} and k = 3.
After sorting the array, we get {-4, -3, 5}.
The maximum 3 numbers in the array are -4, -3, and 5.

Similarly, for the array {4, -4, 4} and k = 2,
after sorting, we get {-4, 4, 4}.
The maximum 2 numbers in the array are 4 and 4.

For the array {-3, 2, 1, 2, -1, -2, 1} and k = 1,
after sorting, we get {-3, -2, -1, 1, 1, 2, 2}.
The maximum 1 number in the array is 2.

To find the maximum k numbers in an array, we can use the following steps:

1. Sort the array in ascending order using a sorting algorithm, such as selection sort or merge sort.
2. Pick the last k elements from the sorted array.
3. Return the picked elements as the result.

In the code provided, the maximum function takes an array and an integer k as input.
It sorts the array using the sort function from the algorithm library.
Then, it creates a new vector called res to store the maximum k numbers.
Finally, it loops through