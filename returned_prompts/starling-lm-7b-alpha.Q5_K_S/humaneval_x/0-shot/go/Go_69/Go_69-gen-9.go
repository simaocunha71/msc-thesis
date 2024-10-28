
```go
m := make(map[int]int)

for _, v := range lst {
    m[v]++
}

var r int
for k, v := range m {
    if v >= k {
        if r == 0 || r < k {
            r = k
        }
    }
}

return r
```

The time complexity of this solution is O(n) because we have to go over each element in the map.
The space complexity is also O(n) because the number of entries in the map is linear with respect to the input size.

```go
func Search(lst []int) int {
    m := make(map[int]int)
    for _, v := range lst {
        m[v]++
    }
    var r int
    for k, v := range m {
        if v >= k {
            if r == 0 || r < k {
                r = k
            }
        }
    }
    return r
}
```

The time complexity of this solution is O(n) because we have to go over each element in the map.
The space complexity is also O(n) because the number of entries in the map is linear with respect to the input size.

```go
func Search(lst []int) int {
    m := make(map[int]int)
    for _, v := range lst {
        m[v]++
    }
    var r int
    for k, v := range m {
        if v >= k {
            if r == 0 || r < k {
                r = k
            }
        }
    }
    return r
}
```

The time complexity of this solution is O(n) because we have to go over each element in the map.
The space complexity is also O(n) because the number of entries in the map is linear with respect to the input size.

```go
func Search(lst []int) int {
    m := make(map[int]int)
    for _, v := range lst {
        m[v]++
    }
    var r int
    for k, v :=