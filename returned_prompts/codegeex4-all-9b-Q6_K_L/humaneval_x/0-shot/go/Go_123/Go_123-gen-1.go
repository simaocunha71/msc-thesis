```go
func GetOddCollatz(n int) []int {
    oddCollatz := []int{}
    for n != 1 {
        if n % 2 != 0 {
            oddCollatz = append(oddCollatz, n)
        }
        if n % 2 == 0 {
            n = n / 2
        } else {
            n = n * 3 + 1
        }
    }
    oddCollatz = append(oddCollatz, 1)
    sort.Ints(oddCollatz)
    return oddCollatz
}
```
