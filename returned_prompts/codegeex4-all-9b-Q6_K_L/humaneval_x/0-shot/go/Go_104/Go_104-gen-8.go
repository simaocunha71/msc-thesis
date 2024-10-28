```go
func UniqueDigits(x []int) []int {
    var res []int
    for _, num := range x {
        if hasEven(num) {
            continue
        }
        res = append(res, num)
    }
    sort.Ints(res)
    return res
}

func hasEven(num int) bool {
    for num > 0 {
        digit := num % 10
        if digit % 2 == 0 {
            return true
        }
        num /= 10
    }
    return false
}
```

The code checks each number in the input slice and appends it to the result slice if it does not have an even digit. After the loop, it sorts the result slice in increasing order.