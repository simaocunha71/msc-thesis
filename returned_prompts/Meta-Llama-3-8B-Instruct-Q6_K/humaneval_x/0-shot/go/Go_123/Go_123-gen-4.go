Here is a Go function that generates the Collatz sequence for a given positive integer n and returns a sorted list of the odd numbers in the sequence:
```go
func GetOddCollatz(n int) []int {
    var result []int
    for n != 1 {
        if n%2 == 1 { // if n is odd
            result = append(result, n) // add n to the result
        }
        if n%2 == 0 { // if n is even
            n = n / 2
        } else {
            n = n*3 + 1
        }
    }
    sort.Ints(result)
    return result
}
```
This function uses a loop to generate the Collatz sequence for the given positive integer n. It checks if the current number is odd or even and adds it to the result list if it's odd. If the current number is even, it divides it by 2, and if it's odd, it multiplies it by 3 and adds 1. The loop continues until the sequence reaches 1. Finally, the function sorts the result list in increasing order and returns it.