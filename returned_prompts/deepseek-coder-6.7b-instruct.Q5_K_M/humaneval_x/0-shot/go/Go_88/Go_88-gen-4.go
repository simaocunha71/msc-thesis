    length := len(array)
    if length == 0 {
        return []int{}
    }

    if length == 1 {
        return []int{array[0]}
    }

    if (array[0] + array[length-1]) % 2 == 0 {
        sort.Sort(sort.Reverse(sort.IntSlice(array)))
    } else {
        sort.Ints(array)
    }

    return array
}
```

## 解説

問題で与えられた条件を満たすようにソートする。ソート順序は、配列の最初と最後の要素の和が偶数の場合は降順、奇数の場合は昇順になる。

## 解答

以下のようなGoプログラムを作成した。

```go
package main

import (
	"fmt"
	"sort"
)

func SortArray(array []int) []int {
	length := len(array)
	if length == 0 {
		return []int{}
	}

	if length == 1 {
		return []int{array[0]}
	}

	if (array[0]+array[length-1])%2 == 0 {
		sort.Sort(sort.Reverse(sort.IntSlice(array)))
	} else {
		sort.Ints(array)
	}

	return array
}

func main() {
	fmt.Println(SortArray([]int{}))
	fmt.Println(SortArray([]int{5}))
	fmt.Println(SortArray([]int{2, 4, 3, 0, 1, 5}))
	fmt.Println(SortArray([]int{2, 4, 3, 0, 1, 5, 6}))
}
```

上記のプ