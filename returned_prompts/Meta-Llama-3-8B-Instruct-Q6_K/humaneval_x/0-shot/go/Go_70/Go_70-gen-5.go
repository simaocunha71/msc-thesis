Here is the solution using a simple loop and two slices for min and max values. This solution assumes that the input list is not empty.

```go
import (
    "sort"
)

// Given list of integers, return list in strange order.
// Strange sorting, is when you start with the minimum value,
// then maximum of the remaining integers, then minimum and so on.
// 
// Examples:
// StrangeSortList([1, 2, 3, 4]) == [1, 4, 2, 3]
// StrangeSortList([5, 5, 5, 5]) == [5, 5, 5, 5]
// StrangeSortList([]) == []
func StrangeSortList(lst []int) []int {
    if len(lst) == 0 {
        return []int{}
    }
    sort.Slice(lst, func(i, j int) bool {
        return lst[i] < lst[j]
    })
    minIndex, maxIndex := 0, 0
    for i := 1; i < len(lst); i++ {
        if lst[i] < lst[minIndex] {
            minIndex = i
        }
        if lst[i] > lst[maxIndex] {
            maxIndex = i
        }
    }
    result := make([]int, len(lst))
    result[0] = lst[minIndex]
    result[1] = lst[maxIndex]
    minIndex, maxIndex = 0, 1
    for i := 2; i < len(lst); {
        if minIndex == maxIndex {
            minIndex = i
            maxIndex = i + 1
        } else if i == maxIndex {
            maxIndex = i + 1
        } else {
            if lst[i] < lst[minIndex] {
                minIndex = i
            }
            result[i] = lst[minIndex]
            i++
        }
    }
    return result
}

```



This solution sorts the input list first. Then it finds the minimum and maximum values in the list. It constructs the result list by adding the minimum value, then the maximum value, then the next minimum value, and so on. It uses two indices to keep track of the current minimum and maximum values. The time complexity of this solution is O(n log n) due to the sorting, where n is the length of the input list. The space complexity is O(n) for the result list.