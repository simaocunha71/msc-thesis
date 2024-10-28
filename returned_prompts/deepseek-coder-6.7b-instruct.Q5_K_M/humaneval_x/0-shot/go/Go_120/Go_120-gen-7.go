    // Sort the array in ascending order
    sort.Ints(arr)

B:
    // Return the last k elements of the array
    return arr[len(arr)-k:]
}

func main()  {

C:
    fmt.Println(Maximum([]int{-3, -4, 5}, 3))
    fmt.Println(Maximum([]int{4, -4, 4}, 2))
    fmt.Println(Maximum([]int{-3, 2, 1, 2, -1, -2, 1}, 1))
}

```

## Answer

```go
import (
	"sort"
)

func Maximum(arr []int, k int) []int {
	sort.Sort(sort.Reverse(sort.IntSlice(arr)))
	return arr[:k]
}

func main() {
	fmt.Println(Maximum([]int{-3, -4, 5}, 3))
	fmt.Println(Maximum([]int{4, -4, 4}, 2))
	fmt.Println(Maximum([]int{-3, 2, 1, 2, -1, -2, 1}, 1))
}
```

## Explanation

The given problem is to return a sorted list of length k with the Maximum k numbers in arr. The first step is to sort the array in descending order, then return the first k elements.

In Go, the "sort" package provides functions to sort slices in increasing or decreasing order. The "sort.Reverse" function is used to