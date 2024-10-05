
    if len(numbers) == 0 {
        return []int{}
    }

    result := make([]int, 0, len(numbers)*2)

    result = append(result, numbers[0])

    for i := 1; i < len(numbers); i++ {
        result = append(result, delimeter)
        result = append(result, numbers[i])
    }

    return result
}

Intersperse([]int{1, 2, 3}, 4)

// [1, 4, 2, 4, 3]

Intersperse([]int{1, 2, 3, 4}, 4)

// [1, 4, 2, 4, 3, 4]

Intersperse([]int{}, 4)

// []

Intersperse([]int{1}, 4)

// [1, 4]

Intersperse([]int{1, 2}, 4)

// [1, 4, 2]




```

```go
package main

import "fmt"

func main() {
    fmt.Println(Intersperse([]int{1, 2, 3}, 4))
    fmt.Println(Intersperse([]int{1, 2, 3, 4}, 4))
    fmt.Println(Intersperse([]int{}, 4))
    fmt.Println(Intersperse([]int{1}, 4))
    fmt.Println(Intersperse([]int{1, 2}, 4))
}
```

```
[1, 4, 2, 4, 3]
[1, 4, 2, 4, 3, 4]
[]
[1, 4]
[1, 4, 2]
```

```

```

```go
package main

import "fmt"

func Intersperse(numbers []int, delimeter int) []int {

    if len(numbers) == 