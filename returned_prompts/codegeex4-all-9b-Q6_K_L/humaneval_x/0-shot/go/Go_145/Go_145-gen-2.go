```go
func OrderByPoints(nums []int) []int {
    if len(nums) == 0 {
        return []int{}
    }
    // Convert the input slice to string slice
    strNums := make([]string, len(nums))
    for i, num := range nums {
        strNums[i] = strconv.Itoa(num)
    }
    // Define a custom sort function
    sort.Slice(strNums, func(i, j int) bool {
        // Calculate the sum of digits for each number
        sumI := sumOfDigits(strNums[i])
        sumJ := sumOfDigits(strNums[j])
        // Sort based on the sum of digits
        if sumI != sumJ {
            return sumI < sumJ
        }
        // If sum of digits is the same, sort based on original index
        return i < j
    })
    // Convert the sorted string slice back to int slice
    sortedNums := make([]int, len(strNums))
    for i, strNum := range strNums {
        num, _ := strconv.Atoi(strNum)
        sortedNums[i] = num
    }
    return sortedNums
}

// Helper function to calculate the sum of digits of a number
func sumOfDigits(num string) int {
    sum := 0
    for _, digit := range num {
        digitInt, _ := strconv.Atoi(string(digit))
        sum += digitInt
    }
    return sum
}
```