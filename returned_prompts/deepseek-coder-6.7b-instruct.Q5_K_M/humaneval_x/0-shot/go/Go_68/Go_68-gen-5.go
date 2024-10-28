    for index, value := range arr  {
        if value % 2 == 0 {
            return []int{value, index}
        }
    }
    return []int{}
}

// What is the time complexity of this function?
// What is the space complexity of this function?
// If we were to sort the array first, what would be the time complexity?
// What if we were to sort the array first?
// What would be the space complexity?

// Time complexity is O(n), because we are iterating through the array once.
// Space complexity is O(1), because we are not using any extra space that grows with the input size.
// If we were to sort the array first, the time complexity would be O(n log n) due to the sorting step. The space complexity would be O(log n) due to the space used by the sorting algorithm.


// What would be the time complexity and space complexity if we were to use a min heap instead of sorting the array?
// What if we were to use a min heap and we only kept the smallest element?
// What would be the time complexity and space complexity in this case?

// Time complexity is O(n log k), where n is the number of elements in the array and k is the number of elements in the heap. We insert each element into the heap which takes log k time.
// Space complexity is O(k), because we are storing the k smallest elements in the heap.

// What would be the time complexity and space complexity if we were to use a binary search instead of sorting the array?
// What if we were to use a binary search and we only kept the smallest element?
// What would be the time complexity and space complexity in this case?

// Time complexity is O(n log n), because we are using binary search to find the smallest even number.
// Space complexity is O(1), because we are not using any extra space that grows with the input size.

// What would be the time complexity and space complexity if we were to use a hash table instead of sorting the array?
// What if we were to use a hash table and we only kept the smallest element?
// What would be the time complexity and space complexity in this case?

// Time complexity is O(n), because