The function RemoveDuplicates takes an array of integers as input and returns a new array with all duplicate elements removed. It does this by iterating through the array and adding each element to a set. If the element is not already in the set, it is added to the set and to the result array. This way, the order of the elements is preserved.

Here is the solution:
```
func RemoveDuplicates(numbers []int) []int {
    seen := make(map[int]bool)
    result := []int{}
    for _, num := range numbers {
        if !seen[num] {
            seen[num] = true
            result = append(result, num)
        }
    }
    return result
}
```
This function uses a map (seen) to keep track of the elements that have been seen so far. It iterates through the input array (numbers), and for each element, it checks if it has been seen before by looking it up in the map. If it hasn't been seen, it adds it to the map and to the result array. This way, the order of the elements is preserved.

For example, if the input array is `[1, 2, 3, 2, 4]`, the function will return the array `[1, 3, 4]`, because these are the elements that occur only once in the original array. The element `2` occurs twice, so it is removed from the result array.

This function has a time complexity of O(n), where n is the length of the input array, because it iterates through the array once. The space complexity is also O(n), because in the worst case, the map and the result array could both be the size of the input array. However, in practice, the space complexity will usually be less than O(n) because many elements in the input array will be unique, so the map and the result array will be smaller.