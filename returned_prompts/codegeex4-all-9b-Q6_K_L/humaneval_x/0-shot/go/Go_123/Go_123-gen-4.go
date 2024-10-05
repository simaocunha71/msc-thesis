```go
func GetOddCollatz(n int) []int {
    // create a slice to store the odd numbers
    var oddNumbers []int
    // create a slice to store the collatz sequence
    var collatzSequence []int
    // add the initial number to the collatz sequence
    collatzSequence = append(collatzSequence, n)
    // while the last number in the collatz sequence is not 1
    for collatzSequence[len(collatzSequence)-1] != 1 {
        // get the last number in the collatz sequence
        lastNumber := collatzSequence[len(collatzSequence)-1]
        // if the last number is even
        if lastNumber%2 == 0 {
            // add half of the last number to the collatz sequence
            collatzSequence = append(collatzSequence, lastNumber/2)
        } else {
            // if the last number is odd
            // add 3 times the last number plus 1 to the collatz sequence
            collatzSequence = append(collatzSequence, lastNumber*3+1)
        }
    }
    // for each number in the collatz sequence
    for _, num := range collatzSequence {
        // if the number is odd
        if num%2 != 0 {
            // add the number to the odd numbers slice
            oddNumbers = append(oddNumbers, num)
        }
    }
    // sort the odd numbers slice
    sort.Ints(oddNumbers)
    // return the odd numbers slice
    return oddNumbers
}
```
