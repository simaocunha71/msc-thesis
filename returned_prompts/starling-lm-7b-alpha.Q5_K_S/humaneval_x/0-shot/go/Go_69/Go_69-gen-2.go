
```go
m := make(map[int]int)
for _, v := range lst {
    m[v]++
}

for i := range lst {
    if m[lst[i]] >= lst[i] {
        return lst[i]
    }
}
return -1
```

The above code first creates a map with the frequency of each element in the list.
Then it goes through the list and checks if the frequency of each element is greater than or equal to the element itself.
If it is, the element is returned, otherwise, it continues to the next element. If no such element is found, it returns -1.

```
Search([]int{4, 1, 2, 2, 3, 1}) == 2
Search([]int{1, 2, 2, 3, 3, 3, 4, 4, 4}) == 3
Search([]int{5, 5, 4, 4, 4}) == -1
```

This solution is O(n), where n is the length of the input list.

```go
func Search(lst []int) int {
    m := make(map[int]int)
    for _, v := range lst {
        m[v]++
    }

    for i := range lst {
        if m[lst[i]] >= lst[i] {
            return lst[i]
        }
    }
    return -1
}
```

```
Search([]int{4, 1, 2, 2, 3, 1}) == 2
Search([]int{1, 2, 2, 3, 3, 3, 4, 4, 4}) == 3
Search([]int{5, 5, 4, 4, 4}) == -1
```

The above solution is O(n), where n is the length of the input list.

```go
func Search(lst []int) int {
    m := make(map[int]int)
    for _, v := range lst {
        m[v]++
    }