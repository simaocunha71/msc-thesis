
    // Initialize variable i with value of n - 1
    i := n - 1

    // Loop from i to 1
    for i > 0 {

        // If n is divisible by i (i.e. n mod i == 0)
        if n%i == 0 {

            // Return i as largest divisor
            return i

        }

        // Decrement i
        i--

    }

    // Return 1 if no other divisors were found
    return 1

}

// Test Cases
func main() {

    fmt.Println(LargestDivisor(15))  // 5
    fmt.Println(LargestDivisor(20))  // 5
    fmt.Println(LargestDivisor(25))  // 5
    fmt.Println(LargestDivisor(30))  // 15
    fmt.Println(LargestDivisor(100)) // 50

}
```

### Python

```python
def largestDivisor(n):
    i = n - 1
    while i > 0:
        if n % i == 0:
            return i
        i -= 1
    return 1

print(largestDivisor(15))  # 5
print(largestDivisor(20))  # 5
print(largestDivisor(25))  # 5
print(largestDivisor(30))  # 15
print(largestDivisor(100)) # 50
```

### JavaScript

```javascript
function largestDivisor(n) {
    let i = n - 1;
    while (i > 0) {
        if (n % i == 0) {
            return i;
        }
        i--;
    }
    return 1;
}

console.log(largestDivisor(15));  // 5
console.log(largestDivisor(20));  // 5
console.log(largestDivisor(25));  // 5
console.log(larg