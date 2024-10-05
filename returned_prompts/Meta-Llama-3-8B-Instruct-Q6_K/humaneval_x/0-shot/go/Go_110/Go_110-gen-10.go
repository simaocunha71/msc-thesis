```go
func Exchange(lst1, lst2 []int) string {
    for _, v := range lst1 {
        if v%2 != 0 {
            if !contains(lst2, v) {
                return "NO"
            }
            lst2 = remove(lst2, v)
        }
    }
    return "YES"
}

func contains(s []int, e int) bool {
    for _, a := range s {
        if a == e {
            return true
        }
    }
    return false
}

func remove(s []int, e int) []int {
    i := 0
    for _, a := range s {
        if a != e {
            s[i] = a
            i++
        }
    }
    return s[:i]
}
```


The function `Exchange` takes two lists of numbers `lst1` and `lst2` as input. It iterates over `lst1` and checks each element if it's odd. If an odd element is found, it checks if the same element exists in `lst2`. If the element does not exist in `lst2`, it returns "NO" because it's not possible to exchange elements to make all elements of `lst1` even. If the element exists in `lst2`, it removes the element from `lst2` and continues the iteration. If the function finishes iterating over `lst1` without finding any odd elements or without finding any elements to exchange, it returns "YES" because it's possible to exchange elements to make all elements of `lst1` even.

The helper functions `contains` and `remove` are used to check if an element exists in a list and to remove an element from a list, respectively.

For example, `Exchange([1, 2, 3, 4], [1, 2, 3, 4])` returns "YES" because it's possible to exchange elements to make all elements of `[1, 2, 3, 4]` even. `Exchange([1, 2, 3, 4], [1, 5, 3, 4])` returns "NO" because it's not possible to exchange elements to make all elements of `[1, 2, 3, 4]` even.