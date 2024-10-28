```go
func StrangeSortList(lst []int) []int {
    // check if list is empty
    if len(lst) == 0 {
        return lst
    }

    // sort list in ascending order
    sort.Ints(lst)

    // create a new list to hold the result
    result := make([]int, 0, len(lst))

    // loop through the sorted list
    for i, v := range lst {
        // add the minimum or maximum value to the result list
        if i%2 == 0 {
            result = append(result, v)
        } else {
            result = append(result, lst[len(lst)-1-i])
        }
    }

    return result
}
```