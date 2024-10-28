
    var a int64 = 0
    var b int64 = 0
    var c int64 = 1
    var d int64 = 0
    var e int64 = 0

    if n <= 2 {
        return 0
    }

    for i := 3; i <= n; i++ {
        d = c
        c = a + b + c
        a = b
        b = d
    }

    return int(c)
}













```
// The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
// Fibfib(0) == 0
// Fibfib(1) == 0
// Fibfib(2) == 1
// Fibfib(n) == Fibfib(n-1) + Fibfib(n-2) + Fibfib(n-3).
// Please write a function to efficiently compute the n-th element of the Fibfib number sequence.
// >>> Fibfib(1)
// 0
// >>> Fibfib(5)
// 4
// >>> Fibfib(8)
// 24
func Fibfib(n int) int {

    var a int64 = 0
    var b int64 = 0
    var c int64 = 1
    var d int64 = 0
    var e int64 = 0

    if n <= 2 {
        return 0
    }

    for i := 3; i <= n; i++ {
        d = c
        c = a + b + c
        a = b
        b = d
    }

    return int(c)
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

```

```

```

```
