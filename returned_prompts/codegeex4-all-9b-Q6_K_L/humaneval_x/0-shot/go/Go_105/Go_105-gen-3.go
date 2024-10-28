```go
func ByLength(arr []int)[]string {
    var s []int
    for _, a := range arr {
        if a >= 1 && a <= 9 {
            s = append(s, a)
        }
    }
    sort.Ints(s)
    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        s[i], s[j] = s[j], s[i]
    }
    var result []string
    for _, a := range s {
        result = append(result, map[int]string{1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}[a])
    }
    return result
}
```

B:
```go
func ByLength(arr []int)[]string {
    var s []int
    for _, a := range arr {
        if a >= 1 && a <= 9 {
            s = append(s, a)
        }
    }
    sort.Ints(s)
    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        s[i], s[j] = s[j], s[i]
    }
    var result []string
    for _, a := range s {
        result = append(result, map[int]string{1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}[a])
    }
    return result
}
```

C:
```go
func ByLength(arr []int)[]string {
    var s []int
    for _, a := range arr {
        if a >= 1 && a <= 9 {
            s = append(s, a)
        }
    }
    sort.Ints(s)
    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        s[i], s[j] = s[j], s[i]
    }
    var result []string
    for _, a := range s {
        result = append(result, map