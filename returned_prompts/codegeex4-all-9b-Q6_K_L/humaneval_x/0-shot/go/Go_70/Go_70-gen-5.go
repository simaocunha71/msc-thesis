```go
func StrangeSortList(lst []int) []int {
    if len(lst) < 2 {
        return lst
    }
    sort.Ints(lst)
    result := make([]int, 0, len(lst))
    i, j := 0, len(lst)-1
    for i <= j {
        result = append(result, lst[i])
        if i != j {
            result = append(result, lst[j])
        }
        i++
        j--
    }
    return result
}
```
This solution first sorts the list in ascending order. Then it iterates over the sorted list, appending the smallest and largest remaining values alternately to the result list. If there are an odd number of elements, the last element is appended without a pair.