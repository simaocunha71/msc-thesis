    return res
}


The problem in your code is the return statement. You are returning the `res` variable before it is populated. You need to return `res` after it is populated.


```go
func StrangeSortList(lst  []int)  []int {
    sort.Ints(lst)
    res := make([]int, len(lst))
    for i := 0; i < len(lst)/2; i++ {
        res[i*2] = lst[i]
        res[i*2+1] = lst[len(lst)-i-1]
    }
    return res
}
```


This code sorts the input list, then populates the result list with the minimum and maximum values from the input list, interleaving them. If the input list has an even number of elements, the result list will have an even number of elements as well. If the input list has an odd number of elements, the result list will have an odd number of elements.


```go
func StrangeSortList(lst  []int)  []int {
    sort.Ints(lst)
    res := make([]int, len(lst))
    for i := 0; i <= len(lst)/2; i++ {
        if i == len(lst)/2 && len(lst)%2 != 0 {
            res[i] = lst[i]
            break
        }
        res[i*2] = lst[i]
        res[i*2+1] = lst[len(lst)-i-1]
    }
    return res
}
```


This version of the code handles the case where the input list has an odd number of elements