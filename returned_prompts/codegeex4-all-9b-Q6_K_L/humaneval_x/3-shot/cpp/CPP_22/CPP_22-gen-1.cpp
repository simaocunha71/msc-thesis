The largest divisor of a number n is the largest number that divides n evenly and is smaller than n.
The function LargestDivisor takes an integer n as input and returns the largest divisor of n.
The function iterates through all numbers from n-1 to 1 and checks if the number divides n evenly.
If a number divides n evenly, it is a divisor of n and the function returns it.
If no number divides n evenly, the function returns 1.
Here is the code:
```go
func LargestDivisor(n int) int {
    for i := n - 1; i > 1; i-- {
        if n % i == 0 {
            return i
        }
    }
    return 1
}
```
This code iterates through all numbers from n-1 to 1 and checks if the number divides n evenly.
If a number divides n evenly, it is a divisor of n and the function returns it.
If no number divides n evenly, the function returns 1.
This code has a time complexity of O(n), because it iterates through all numbers from n-1 to 1.