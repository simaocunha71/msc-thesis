
// Base case
if n <= 1 {
    return n
}

// Recursive case
return Fib(n-1) + Fib(n-2)
}


```

### Python

```python
def Fib(n):
    # Base case
    if n <= 1:
        return n
    # Recursive case
    else:
        return Fib(n-1) + Fib(n-2)

# Test cases
print(Fib(10)) # 55
print(Fib(1))  # 1
print(Fib(8))  # 21
```


### JavaScript

```javascript
function Fib(n){
    // Base case
    if(n <= 1){
        return n;
    }
    // Recursive case
    else{
        return Fib(n-1) + Fib(n-2);
    }
}

// Test cases
console.log(Fib(10)); // 55
console.log(Fib(1));  // 1
console.log(Fib(8));  // 21
```

## Iterative Approach

In this approach, we use a loop instead of recursion to calculate the n-th Fibonacci number. This makes it more memory efficient because it doesn't require the overhead of recursive function calls.

### Golang

```golang
package main

import "fmt"

func Fib(n int) int {
    a, b := 0, 1
    for i := 0; i < n; i++ {
        a, b = b, a+b
    }
    return a
}

func main() {
    fmt.Println(Fib(10)) // 55
    fmt.Println(Fib(1))  // 1
    fmt.Println(Fib(8))  // 21
}
```

### Python

```python
def Fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
