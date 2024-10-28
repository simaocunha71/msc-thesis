    res := make([]int, n)

    for i := 0; i < n; i++ {
        if i%2 == 0 {
            res[i] = factorial(i)
        } else {
            res[i] = sum(i)
        }
    }

    return res
}

func factorial(n int) int {
    if n == 0 {
        return 1
    }
    return n * factorial(n-1)
}

func sum(n int) int {
    return n * (n + 1) / 2
}

































```

```

```
```

```go
package main

import "fmt"

func F(n int) []int {
    res := make([]int, n)

    for i := 0; i < n; i++ {
        if i%2 == 0 {
            res[i] = factorial(i)
        } else {
            res[i] = sum(i)
        }
    }

    return res
}

func factorial(n int) int {
    if n == 0 {
        return 1
    }
    return n * factorial(n-1)
}

func sum(n int) int {
    return n * (n + 1) / 2
}

func main() {
    fmt.Println(F(5))
}

```
```

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def sum(n):
    return n * (n + 1) / 2

def F(n):
    res = []
    for i in range(n):
        if i % 2 == 0:
            res.append(factorial(i))
        else:
            res.append(sum(i))
    return res

print(F(5))