```go
func GetOddCollatz(n int) []int {
    collatz := []int{n}
    for n != 1 {
        if n%2 == 0 {
            n /= 2
        } else {
            n = 3*n + 1
        }
        collatz = append(collatz, n)
    }
    oddCollatz := []int{}
    for _, num := range collatz {
        if num%2 != 0 {
            oddCollatz = append(oddCollatz, num)
        }
    }
    sort.Ints(oddCollatz)
    return oddCollatz
}
```