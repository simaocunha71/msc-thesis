```go
func GetOddCollatz(n int) []int {
    oddList := []int{}
    for n != 1 {
        if n % 2 == 1 {
            oddList = append(oddList, n)
        }
        if n % 2 == 0 {
            n = n / 2
        } else {
            n = 3 * n + 1
        }
    }
    oddList = append(oddList, 1)
    sort.Ints(oddList)
    return oddList
}
```
