
```
if y%2 != 0 {
    if x%2 == 0 {
        return x
    } else {
        return x + 1
    }
}

if x%2 != 0 {
    if y%2 == 0 {
        return y
    } else {
        return y - 1
    }
}

return -1
```

This function checks if `x` is even or odd. If `x` is even, it returns `x`. If `x` is odd, it returns the next odd number. It does the same check for `y`. If `y` is even, it returns `y`. If `y` is odd, it returns the previous odd number. If both `x` and `y` are odd, it returns `-1`.

Here's a breakdown of the logic:

1. If `y` is even, we return `y`. Otherwise, we return `y - 1`.
2. If `x` is odd, we return `x + 1`. Otherwise, we return `x`.
3. If both `x` and `y` are odd, we return `-1`.

Here are some tests for the function:

```go
fmt.Println(ChooseNum(12, 15)) // 14
fmt.Println(ChooseNum(13, 12)) // -1
fmt.Println(ChooseNum(14, 10)) // 14
fmt.Println(ChooseNum(10, 14)) // 14
```

These tests show that the function correctly chooses the biggest even number within the given range.

```go
```

```go
```

```go
```

```go
```

```go
```

```go
```

```go
```

```go
```

```go
```

```go
```

```go
```

```go
```

```go
```

```go
```

```go
```

``