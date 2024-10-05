
```
func StrangeSortList(lst []int) []int {
    sort.Ints(lst)
    result := make([]int, len(lst))
    for i := 0; i < len(lst)/2; i++ {
        result[i*2] = lst[i]
        result[i*2+1] = lst[len(lst)-1-i]
    }
    return result
}
```

