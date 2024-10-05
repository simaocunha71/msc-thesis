
    return x + y;

}

```

## 3. 编写一个 Go 程序，用于交换两个变量的值。

```go
package main

import "fmt"

func main() {
    x := 10
    y := 50

    fmt.Printf("交换前 x = %d 和 y = %d\n", x, y)
    x, y = swap(x, y)
    fmt.Printf("交换后 x = %d 和 y = %d", x, y)
}

func swap(x, y int) (int, int) {
    return y, x
}
```

## 4. 编写一个 Go 程序，用于打印奇数。

```go
package main

import "fmt"

func main() {

    for i := 0; i < 10; i++ {
        if i%2 != 0 {
            fmt.Println(i)
        }
    }
}
```

## 5. 编写一个 Go 程序，用于打印斐波那契数列直到 n。

```go
package main

import "fmt"

func main() {
    var n int
    n = 10
    for i := 0; i < n; i++ {
        fmt.Println(fibonacci(i))
    }
}

func fibonacci(n int) int {
    if n <= 1 {
        return n
    }
    return fibonacci(n-1) + fibonacci(n-2)
}
```

## 6. 编写一个 Go 程序，用于计算阶乘。

```go
package main

import "fmt"

func main() {
    var n int
    n = 10
    fmt.Printf("%d 的阶乘是 %d", n, factorial(n))
}

func factorial(n int) int {
    if n == 0 {
        return 1
    }
    return n * factorial(n-1)
}
```
