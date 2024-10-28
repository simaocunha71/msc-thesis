
```go
func CanArrange(arr []int) int {
    m := make(map[int]int)
    for _, v := range arr {
        m[v] = 1
    }
    for i := range arr {
        if _, ok := m[arr[i]]; !ok {
            return -1
        }
    }
    max := -1
    for i := range arr {
        if arr[i] > max {
            max = arr[i]
        } else if arr[i] == max {
            continue
        } else {
            return i
        }
    }
    return -1
}
```

In the solution, the function first creates a map to check if all the values in the array are unique. Then, it checks if all the values in the array are present in the map. If not, it immediately returns -1. Next, it initializes a max variable with -1 and iterates over the array. If the current element is greater than max, it updates max. If the current element is equal to max, it continues to the next element. Otherwise, it returns the index of the current element. If no element is found that is not greater than or equal to the previous element, it returns -1.

// Create a function which returns the largest index of an element which
// is not greater than or equal to the element immediately preceding it. If
// no such element exists then return -1. The given array will not contain
// duplicate values.
// 
// Examples:
// CanArrange([1,2,4,3,5]) = 3
// CanArrange([1,2,3]) = -1
func CanArrange(arr []int) int {

    m := make(map[int]int)
    for _, v := range arr {
        m[v] = 1
    }
    for i := range arr {
        if _, ok := m[arr[i]]; !ok {
            return -1
        }
    }
    max := -1
    for i := range arr {
        if arr[i] > max {
            max = arr[i]
        } else if arr[i] == max {
            continue
        }