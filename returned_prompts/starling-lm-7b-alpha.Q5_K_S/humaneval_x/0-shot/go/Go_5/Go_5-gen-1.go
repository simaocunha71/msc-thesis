
    var result []int
    result = append(result, numbers[0])
    for i := 0; i < len(numbers)-1; i++ {
        result = append(result, numbers[i], delimeter)
    }
    result = append(result, numbers[len(numbers)-1])
    return result
}





// 解释：
// 在这个函数中，我们首先创建一个空的切片，并将第一个数字添加到切片中。
// 然后我们通过循环遍历数字的剩余部分，并将每个数字与分隔符添加到切片中。
// 最后我们添加最后一个数字并返回结果切片。









```
```go

```
```

```go
package main

import "fmt"

func Intersperse(numbers []int, delimeter int) []int {

    var result []int
    result = append(result, numbers[0])
    for i := 0; i < len(numbers)-1; i++ {
        result = append(result, numbers[i], delimeter)
    }
    result = append(result, numbers[len(numbers)-1])
    return result
}

func main() {
    fmt.Println(Intersperse([]int{1, 2, 3}, 4))
    fmt.Println(Intersperse([]int{}, 4))
}
```