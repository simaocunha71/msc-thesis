Here is a Go solution for the problem:

```go
func ByLength(arr []int) []string {
    var result []string
    var oneToNine = []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
    sort.Ints(arr)
    arr = reverse(arr)
    for _, num := range arr {
        if _, ok := contains(oneToNine, num); ok {
            switch num {
            case 1:
                result = append(result, "One")
            case 2:
                result = append(result, "Two")
            case 3:
                result = append(result, "Three")
            case 4:
                result = append(result, "Four")
            case 5:
                result = append(result, "Five")
            case 6:
                result = append(result, "Six")
            case 7:
                result = append(result, "Seven")
            case 8:
                result = append(result, "Eight")
            case 9:
                result = append(result, "Nine")
            }
        }
    }
    return result
}

func reverse(arr []int) []int {
    result := make([]int, len(arr))
    for i, num := range arr {
        result[len(arr)-i-1] = num
    }
    return result
}

func contains(arr []int, target int) (bool, int) {
    for i, num := range arr {
        if num == target {
            return true, i
        }
    }
    return false, -1
}
```

This program sorts the array of integers, reverses it, and then goes through the array to replace the numbers between 1 and 9 with their corresponding names. If the array contains any numbers outside the range of 1 to 9, they are ignored. The program also handles the case where the array is empty, in which case it returns an empty array. The `reverse` function reverses the array, and the `contains` function checks if a target number is in the array and returns its index if it is. The `ByLength` function calls these helper functions to solve the problem. 