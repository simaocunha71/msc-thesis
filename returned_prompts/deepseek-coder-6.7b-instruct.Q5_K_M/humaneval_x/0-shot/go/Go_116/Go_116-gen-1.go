sort.Slice(arr, func(i, j int) bool {
        // convert to binary and count ones
        binI := fmt.Sprintf("%b", arr[i])
        binJ := fmt.Sprintf("%b", arr[j])
        oneCountI := strings.Count(binI, "1")
        oneCountJ := strings.Count(binJ, "1")

        // if the number of ones are the same, compare the decimal value
        if oneCountI == oneCountJ {
            return arr[i] < arr[j]
        }

        return oneCountI < oneCountJ
    })

    return arr
}
```

This solution uses the built-in `sort.Slice` function in Go, which sorts the array in-place based on the provided less function. The less function checks the number of ones in the binary representation of each number, and if they are the same, it checks the decimal value of the numbers. The result is sorted array.

Please note that the `strings.Count` function is used to count the number of "1"s in the binary representation of each number.

This solution is efficient as it uses the `sort.Slice` function, which has a time complexity of O(n log n), where n is the length of the array.

Also note that the `sort.Slice` function sorts the array in-place, so no additional space is needed.

In summary, this solution satisfies the problem requirements and is efficient.

This solution assumes that the input array will only contain non-negative integers.

Note: This solution does not handle negative numbers as they are not comparable in this problem context.

Also note that, the binary representation of the number includes the sign bit for negative numbers in two's complement form, but as we are only concerned about the number of ones in binary representation of non-negative numbers, this does not affect the solution.

If you want to handle negative numbers as well, you would need to modify the solution to handle them separately and separately from non-negative numbers.
*/

package main

import (
	"fmt"
	"strings"
	"sort"
)

func SortArray(arr []int) []int {
	sort.Slice(arr, func