Here is the solution:
```go
import (
    "math"
)

func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i] - numbers[j]) < threshold {
                return true
            }
        }
    }
    return false
}
```
This function iterates over the list of numbers and checks each pair of numbers to see if the absolute difference between them is less than the given threshold. If it finds any pair of numbers that are closer than the threshold, it returns `true`. If it doesn't find any such pair after checking all pairs, it returns `false`. 

This function has a time complexity of O(n^2) where n is the length of the input list, because it needs to check each pair of numbers. This may not be efficient for very large lists. If you need a more efficient solution, you could consider using a data structure like a balanced binary search tree to store the numbers and then iterate over the tree to find close pairs. 