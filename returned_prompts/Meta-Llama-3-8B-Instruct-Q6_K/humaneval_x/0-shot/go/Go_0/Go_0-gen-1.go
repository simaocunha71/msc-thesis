Here is the solution in Go:

```go
import (
    "math"
)

func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i]-numbers[j]) < threshold {
                return true
            }
        }
    }
    return false
}
```


Explanation:
The function `HasCloseElements` takes two parameters: a slice of numbers and a threshold value. It iterates over the slice using two nested loops. The outer loop iterates over each element in the slice, and the inner loop iterates over each element that comes after the current element in the slice. It checks if the absolute difference between the current element and any element after it is less than the threshold. If it finds such a pair, it returns `true`. If it doesn't find any such pair after checking all elements, it returns `false`. 

Note: This function has a time complexity of O(n^2), where n is the length of the input slice, because it uses two nested loops to check all pairs of elements. For large inputs, this function may be slow. If you need a more efficient solution, you may want to consider using a data structure like a set or a binary search tree to store the elements and check for closeness in O(n log n) time. 