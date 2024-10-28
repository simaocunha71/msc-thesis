You can use a for loop to iterate from 2 to n-1 and check if n is divisible by the current number. If it is, then that number is the largest divisor of n. Here's how you can implement the LargestDivisor function:

```
func LargestDivisor(n int) int {
    for i := n - 1; i > 1; i-- {
        if n % i == 0 {
            return i
        }
    }
    return -1 // n is a prime number
}
```

In this function, we start from n-1 and go down to 2. If we find a number i such that n is divisible by i, then i is the largest divisor of n. If we reach 2 and still haven't found a divisor, then n is a prime number and we return -1.