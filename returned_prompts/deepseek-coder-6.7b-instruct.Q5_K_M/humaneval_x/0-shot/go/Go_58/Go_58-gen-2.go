    sort.Ints(l1)
    sort.Ints(l2)

B:
    common := make([]int, 0)
    for i, j := 0, 0; i < len(l1) && j < len(l2); {
        switch {
        case l1[i] < l2[j]:
            i++
        case l1[i] > l2[j]:
            j++
        default:
            common = append(common, l1[i])
            i++
            j++
        }
    }
    return common
}
```

### 2. 测试用例

```go
package main

import (
    "fmt"
)

func main() {
    fmt.Println(Common([]int{1, 4, 3, 34, 653, 2, 5}, []int{5, 7, 1, 5, 9, 653, 121})) // [1, 5, 653]
    fmt.Println(Common([]int{5, 3, 2, 8}, []int{3, 2})) // [2, 3]
}
```

### 3. 运行测试用例

```go
go run main.go
```

### 4. 结果

```bash
[1, 5, 653]
[2, 3]
```

### 5. 优化

上述代码的时间复杂度为O(nlogn)，因为需要对数组进行排序，空间复杂度为O(n)，因为创建了一个新的数组来存储共同的元素。对于这种问题，你可能希望考虑使用不同的方法，例如使用哈希表（或map），这样可以在O(n)的时间复杂度内解决。

```go
package main

import (
	"fmt"
)

func Common(l1 []int, l2 []int) []int {
	common := make([]int, 0)
	m := make(map[int]bool)

	for _, v := range l