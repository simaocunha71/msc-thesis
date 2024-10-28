
The reason is that the function contain is not correct. It's necessary to check if the number itself is even, and not only if there are even digits.

Here is the correct function:

```go
func contain(i int) bool {
    if i%2 == 0 {
        return true
    }
    s := strconv.Itoa(i)
    for _, v := range s {
        if v%2 == 0 {
            return true
        }
    }
    return false
}
```






In addition, the sorting function is incorrect. It should be:

```go
func UniqueDigits(x []int) []int {
    var res []int
    for _, v := range x {
        if !contain(v) {
            res = append(res, v)
        }
    }
    sort.Slice(res, func(i, j int) bool {
        return res[i] < res[j]
    })
    return res
}
```































