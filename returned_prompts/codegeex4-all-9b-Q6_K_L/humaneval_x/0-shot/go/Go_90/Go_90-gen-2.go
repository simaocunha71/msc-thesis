Here is a solution using Go:

```go
func NextSmallest(lst []int) interface{} {
    if len(lst) < 2 {
        return nil
    }
    
    // Remove duplicates
    lst = removeDuplicates(lst)
    
    if len(lst) < 2 {
        return nil
    }
    
    // Sort the list
    sort.Ints(lst)
    
    // Return the second element
    return lst[1]
}

// Remove duplicates from a slice of integers
func removeDuplicates(lst []int) []int {
    keys := make(map[int]bool)
    list := []int{}
    for _, entry := range lst {
        if _, value := keys[entry]; !value {
            keys[entry] = true
            list = append(list, entry)
        }
    }
    return list
}
```

The `NextSmallest` function first checks if the list has less than 2 elements. If so, it returns `nil`. 

Then, it removes the duplicates from the list using a helper function `removeDuplicates`.

If the list still has less than 2 elements after removing duplicates, it returns `nil`. 

If the list has at least 2 elements, it sorts the list in ascending order and returns the second element.

The `removeDuplicates` function uses a map to keep track of the unique elements in the list. It iterates over the list and checks if the element is already in the map. If not, it adds the element to the map and the result list. 

This solution has a time complexity of O(n log n) due to the sorting operation, where n is the length of the list.