
    for i := n - 1; i > 0; i-- {
        if n%i == 0 {
            return i
        }
    }
    return -1
}
```

Output:

```
>>> LargestDivisor(15)
5
```

This function starts from n-1 and iterates down to 1, checking each number to see if it divides n evenly (i.e., if n modulus i equals 0). If it finds such a number, it immediately returns it. If it doesn't find any such number, it returns -1 as a signal that n is a prime number.

This function has a time complexity of O(n), as in the worst-case scenario, it has to iterate through all the numbers from n to 1.

This function has a space complexity of O(1), as it only uses a single integer variable i and does not use any additional data structures that grow with the input size.

```go
