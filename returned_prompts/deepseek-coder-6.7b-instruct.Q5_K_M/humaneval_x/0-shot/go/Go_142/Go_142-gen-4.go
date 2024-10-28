    sum := 0

B:
    for i, v := range lst {
        switch {
        case i%3 == 0:
            sum += int(math.Pow(float64(v), 2))
        case i%4 == 0:
            sum += int(math.Pow(float64(v), 3))
        default:
            sum += v
        }
    }

    return sum
}
```

## 2. 函数实现

```go
func SumSquares(lst []int) int {
    sum := 0
    for i, v := range lst {
        switch {
        case i%3 == 0:
            sum += int(math.Pow(float64(v), 2))
        case i%4 == 0:
            sum += int(math.Pow(float64(v), 3))
        default:
            sum += v
        }
    }
    return sum
}
```

## 3. 测试

```go
package main

import (
    "fmt"
)

func main() {
    fmt.Println(SumSquares([]int{1, 2, 3}))    // 6
    fmt.Println(SumSquares([]int{}))            // 0
    fmt.Println(SumSquares([]int{-1, -5, 2, -1, -5})) // -126
}
```

## 4. 运行结果

```
6
0
-126
```

## 5. 解释

该函数通过遍历输入的整数切片，对每个元素根据其索引进行处理，并将结果添加到总和中。如果索引是3的倍数，则对该元素进行平方运算；如果索引是4的倍数，则对该元素进行立方运算。如果既不是3的倍数也不是4的倍数，则直接将该元素加到总和中。最后，函数返回总和。

## 6. 注意事项

在Go语言中，切片