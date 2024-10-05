
    for i := n - 1; i > 0; i-- {
        if n%i == 0 {
            return i
        }
    }
    return -1
}
```

## 3. 

Write a function that takes a number n as an argument and returns the sum of all the numbers from 1 to n.

```go
// sum of all the numbers from 1 to n
// 1 + 2 + 3 + ... + n
