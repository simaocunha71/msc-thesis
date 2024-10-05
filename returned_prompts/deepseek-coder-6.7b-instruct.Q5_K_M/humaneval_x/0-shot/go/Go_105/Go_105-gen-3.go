    sort.Ints(arr)
    var result []string
    for i, _ := range arr {
        if arr[i] < 1 || arr[i] > 9 {
            continue A
        }
        switch arr[i] {
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
    for i, j := 0, len(result)-1; i < j; i, j = i+1, j-1 {
        result[i], result[j] = result[j], result[i]
    }
    return result
}
```

## Code Explanation
The code works by first sorting the input array and then iterating over it. If an element is not in the range 1-9, the iteration is skipped. The corresponding word for each number is then appended to the result array. Finally, the array is reversed before it is returned.

## Performance
The time complexity of this code is O(n log n) due to the sorting operation. The space complexity is O(n) as the code creates a new array to store the result. The code is efficient in terms of time and space complexity.

## Test Cases
```go
func TestByLength(t *testing.T) {
    t.Run("Test case 1", func(t *testing.T) {
        arr := []int{2, 1, 1, 4, 5, 8, 2, 3}
        expected := []string{"Eight", "Five", "Four", "Three", "Two", "Two", "