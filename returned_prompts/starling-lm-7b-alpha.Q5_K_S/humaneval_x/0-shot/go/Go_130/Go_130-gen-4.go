
```go
tribonacci := make([]float64, n+1)
tribonacci[0] = 3
tribonacci[1] = 1
tribonacci[2] = 2

for i := 3; i < n+1; i++ {
    if i%2 == 0 {
        tribonacci[i] = tribonacci[i-2]
    } else {
        tribonacci[i] = tribonacci[i-1] + tribonacci[i-2] + tribonacci[i-3]
    }
}
return tribonacci
```

In this function, we first initialize the first three tribonacci numbers as 3, 1, and 2. Then, we use a for loop to calculate the remaining tribonacci numbers. When `i` is even, we assign the `i`-th tribonacci number as the `i-2`-th tribonacci number. When `i` is odd, we assign the `i`-th tribonacci number as the sum of the `i-1`-th, `i-2`-th, and `i-3`-th tribonacci numbers. Finally, we return the tribonacci numbers as a slice.

```go
```
```

...
```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
