Here is a possible implementation of the `IsSorted` function in Go:
```go
func IsSorted(lst []int) bool {
    for i := 1; i < len(lst); i++ {
        if lst[i-1] >= lst[i] {
            if len(lst) > 2 && containsDuplicate(lst) {
                return false
            }
            return false
        }
    }
    return true
}

func containsDuplicate(lst []int) bool {
    m := make(map[int]bool)
    for _, v := range lst {
        if m[v] {
            return true
        }
        m[v] = true
    }
    return false
}
```
Here's an explanation of the code:

The `IsSorted` function iterates through the list, checking if each element is less than or equal to the previous one. If it finds an element that is not less than or equal to the previous one, it returns `false`. If it reaches the end of the list without finding any such element, it returns `true`.

The `containsDuplicate` function uses a map to keep track of the elements it has seen so far. It iterates through the list, and for each element, it checks if the map already contains that element. If it does, it returns `true`. If it reaches the end of the list without finding any duplicates, it returns `false`.

The `IsSorted` function calls `containsDuplicate` to check for duplicates after finding a non-sorted element. If `containsDuplicate` returns `true`, it means that there are duplicates in the list, and the function returns `false`. Otherwise, it returns `false`.

You can test this function with the examples you provided:
```go
fmt.Println(IsSorted([]int{5})) // true
fmt.Println(IsSorted([]int{1, 2, 3, 4, 5})) // true
fmt.Println(IsSorted([]int{1, 3, 2, 4, 5})) // false
fmt.Println(IsSorted([]int{1, 2, 3, 4, 5, 6})) // true
fmt.Println(IsSorted([]int{1, 2, 3, 4, 5, 6, 7})) // true
fmt.Println(IsSorted([]int{1, 3, 2, 4, 5, 6, 7})) // false
fmt.Println(IsSorted([]int{1, 