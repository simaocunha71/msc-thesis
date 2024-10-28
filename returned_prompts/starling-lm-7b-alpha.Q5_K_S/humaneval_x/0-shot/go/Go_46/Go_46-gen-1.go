
func Fib4(n int) int {
    a, b, c, d := 0, 0, 2, 0
    for i := 0; i < n; i++ {
        a, b, c, d = b, c, d+b+a, b
    }
    return d
}








*/
import "fmt"

func Fib4(n int) int {
    a, b, c, d := 0, 0, 2, 0
    for i := 0; i < n; i++ {
        a, b, c, d = b, c, d+b+a, b
    }
    return d
}
func main() {
    fmt.Println(Fib4(5))
    fmt.Println(Fib4(6))
    fmt.Println(Fib4(7))
}








*/

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

```

```

```

```

```

```

```

