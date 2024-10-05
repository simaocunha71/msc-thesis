    var e,o int
    var t = strconv.Itoa(num)
    for _,v := range t{
        if v%2 == 0 {
            e++
        }else{
            o++
        }
    }
    return [2]int{e,o}









```
```go

```
```

```go
```
```

EvenOddCount(-12) ==> (1, 1)
EvenOddCount(123) ==> (1, 2)
```

```go
package main

import (
    "fmt"
    "strconv"
)

func EvenOddCount(num int) (e, o int) {
    t := strconv.Itoa(num)
    for _, v := range t {
        if v%2 == 0 {
            e++
        } else {
            o++
        }
    }
    return
}

func main() {
    fmt.Println(EvenOddCount(-12))
    fmt.Println(EvenOddCount(123))
}
```

```
```

```go
```
```

```go
```
```

```go
package main

import (
    "strconv"
)

func EvenOddCount(num int) (e, o int) {
    t := strconv.Itoa(num)
    for _, v := range t {
        if v%2 == 0 {
            e++
        } else {
            o++
        }
    }
    return
}

func main() {
    fmt.Println(EvenOddCount(-12))
    fmt.Println(EvenOddCount(123))
}
```

```go
package main

import (
    "strconv"
)

func EvenOddCount(num int) [2]int {
    t := strconv.Itoa(num)
    e, o := 0, 0
    for _, v