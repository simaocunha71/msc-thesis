
func Fib4(n int) int {
    if n == 0 {
        return 0
    }
    if n == 1 {
        return 0
    }
    if n == 2 {
        return 2
    }
    if n == 3 {
        return 0
    }
    var a, b, c, d int = 0, 0, 2, 0
    for i := 4; i <= n; i++ {
        a, b, c, d = b, c, d+b+c+a, a
    }
    return d
}






func Fib4(n int) int {
    if n == 0 || n == 1 {
        return 0
    }
    if n == 2 {
        return 2
    }
    if n == 3 {
        return 0
    }
    var a, b, c, d int = 0, 0, 2, 0
    for i := 4; i <= n; i++ {
        a, b, c, d = b, c, d+b+c+a, a
    }
    return d
}



*/
func Fib4(n int) int {
    if n == 0 || n == 1 {
        return 0
    }
    if n == 2 {
        return 2
    }
    if n == 3 {
        return 0
    }
    var a, b, c, d int = 0, 0, 2, 0
    for i := 4; i <= n; i++ {
        a, b, c, d = b, c, d+b+c+a, a
    }
    return d
}

































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