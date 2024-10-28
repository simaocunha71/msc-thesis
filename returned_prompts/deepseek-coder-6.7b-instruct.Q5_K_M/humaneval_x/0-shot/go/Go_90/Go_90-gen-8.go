    sort.Ints(lst)
    m := math.MaxInt64
    for i:=0; i<len(lst)-1; i++ {
        if lst[i] < lst[i+1] && lst[i] < m {
            m = lst[i]
        }
    }
    if m == math.MaxInt64 {
        return nil
    }
    return m

}

// What is the time complexity of this solution?
// 
// A: The time complexity is O(nlogn) due to the sort operation. The for loop has a time complexity of O(n). Therefore, the overall time complexity is O(nlogn).
// 
// What is the space complexity of this solution?
// 
// A: The space complexity is O(1) since we are not using any additional space that scales with the input size.

// What would be a better approach to solve this problem?
// 
// A: A better approach would be to iterate through the list only once, keeping track of the smallest and second smallest elements as we go. This would reduce the time complexity to O(n).

// What would be a possible issue with the current solution?
// 
// A: A possible issue with the current solution is that it does not handle the case where there are duplicate elements in the input list. In this case, it would return the maximum value (the first smallest element in the sorted list), which is not the second smallest element.

// How can you modify the current solution to handle this case?
// 
// A: We can modify the current solution to skip duplicate elements while searching for the second smallest element. Here is the modified code:

func NextSmallest(lst []int) interface{} {
    sort.Ints(lst)
    m := math.MaxInt64
    for i:=0; i<len(lst)-1; i++ {
        if lst[i] < lst[i+1] && lst[i] < m {
            m = lst[i]
        }
    }
    if m == math.MaxInt64 {
        return nil
    }
    return m
}

