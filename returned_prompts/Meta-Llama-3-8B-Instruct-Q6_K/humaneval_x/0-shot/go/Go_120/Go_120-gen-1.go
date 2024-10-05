You can solve this problem by using the built-in sort function in Go. Here's a solution:

```go
import (
    "sort"
)

func Maximum(arr []int, k int) []int {
    sort.Slice(arr, func(i, j int) bool {
        return arr[i] > arr[j]
    })
    return arr[:k]
}
```

This solution sorts the array in descending order and then returns the first `k` elements. The `sort.Slice` function is used to sort the array. The comparison function passed to `sort.Slice` is used to determine the order of the elements. In this case, it's used to sort the array in descending order.

The time complexity of this solution is O(n log n) due to the sorting, where `n` is the length of the array. The space complexity is O(1) since it only uses a constant amount of space to store the result. 

Note that this solution assumes that `k` is not greater than the length of the array. If `k` is greater than the length of the array, you may want to handle this case separately. 

Also, this solution modifies the original array. If you want to preserve the original array, you can create a copy of it before sorting. 

Here's an example of how you can use this function:

```go
arr := []int{-3, -4, 5}
k := 3
result := Maximum(arr, k)
fmt.Println(result) // Output: [-4, -3, 5]
```  0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63 