```go
func GetOddCollatz(n int) []int {
    result := make([]int, 0)
    for n != 1 {
        if n % 2 == 1 {
            result = append(result, n)
        }
        if n%2 == 0 {
            n = n / 2
        } else {
            n = 3*n + 1
        }
    }
    sort.Ints(result)
    return result
}
```


This solution uses a loop to generate the Collatz sequence for the given number `n`. It keeps track of the odd numbers in the sequence and appends them to the `result` slice. After the loop, it sorts the `result` slice in ascending order using the `sort.Ints` function and returns it. The time complexity of this solution is O(logN), where N is the given number `n`, because the Collatz sequence tends to reach 1 in a logarithmic number of steps. The space complexity is O(N), where N is the number of odd numbers in the Collatz sequence.