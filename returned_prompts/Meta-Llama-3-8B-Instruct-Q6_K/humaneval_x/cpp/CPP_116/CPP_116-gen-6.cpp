



C++ solution using vector and pair

Explanation:

1.  The function `sort_array` takes a vector of integers `arr` as input.
2.  Create a new vector `arr_pair` to store pairs of integers, where each pair contains the count of 1's in the binary representation of the corresponding integer and the integer itself.
3.  Iterate through the input vector `arr` and calculate the number of 1's in each integer's binary representation.
4.  Store each integer with its corresponding count of 1's in the `arr_pair` vector as a pair.
5.  Sort the `arr_pair` vector in ascending order based on the count of 1's in the binary representation and then the decimal value of the integers.
6.  Create a new vector `result` to store the sorted integers.
7.  Iterate through the sorted `arr_pair` vector and push each integer into the `result` vector.
8.  Return the `result` vector, which contains the sorted integers.

The time complexity of this solution is O(n log n), where n is the size of the input vector `arr`, due to the sorting operation. The space complexity is O(n), as we are storing the input vector and the sorted result vector.