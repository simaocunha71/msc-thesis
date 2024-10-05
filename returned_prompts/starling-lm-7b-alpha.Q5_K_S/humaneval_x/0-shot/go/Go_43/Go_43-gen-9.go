
```go
m := make(map[int]bool)

for _, v := range l {
    if _, ok := m[v]; ok {
        return true
    } else {
        m[0-v] = true
    }
}
return false
```

This function uses a map to store the values that have already been encountered. It iterates over the input list, and for each element it checks whether its negation is in the map. If it is, then it means that there are two distinct elements that sum up to zero, and the function returns true. Otherwise, it adds the negation of the current element to the map. If the function reaches the end of the list without finding a pair of elements that sum to zero, it returns false.

This function has a time complexity of O(n), where n is the number of elements in the input list, since it only iterates over the list once. The space complexity is also O(n), as the map can contain at most n elements.

Here are some examples of how the function works:

```go
fmt.Println(PairsSumToZero([]int{1, 3, 5, 0})) // false
fmt.Println(PairsSumToZero([]int{1, 3, -2, 1})) // false
fmt.Println(PairsSumToZero([]int{1, 2, 3, 7}))  // false
fmt.Println(PairsSumToZero([]int{2, 4, -5, 3, 5, 7})) // true
fmt.Println(PairsSumToZero([]int{1})) // false
```

```

```

```go
```

```

```

```go
```

```
```
```

```
```
```

```
```
```
```

```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```