    result := make([]int, len(numbers))
    max := numbers[0]
    result[0] = max

    for i := 1; i < len(numbers); i++ {
        if numbers[i] > max {
            max = numbers[i]
        }
        result[i] = max
    }

    return result
}

// From a given list of integers, generate a list of rolling minimum element found until given moment
// in the sequence.
// >>> RollingMin([1, 2, 3, 2, 3, 4, 2])
// [1, 1, 1, 2, 2, 2, 2]
func RollingMin(numbers []int) []int {
    result := make([]int, len(numbers))
    min := numbers[0]
    result[0] = min

    for i := 1; i < len(numbers); i++ {
        if numbers[i] < min {
            min = numbers[i]
        }
        result[i] = min
    }

    return result
}

// From a given list of integers, generate a list of rolling sum of elements found until given moment
// in the sequence.
// >>> RollingSum([1, 2, 3, 4])
// [1, 3, 6, 10]
func RollingSum(numbers []int) []int {
    result := make([]int, len(numbers))
    sum := 0
    result[0] = sum

    for i := 1; i < len(numbers); i++ {
        sum += numbers[i]
        result[i] = sum
    }

    return result
}

func main() {
    fmt.Println(RollingMax([]int{1, 2, 3, 2, 3, 4, 2}))
    fmt.Println(RollingMin([]int{1, 2, 3, 2, 3, 4, 2}))
    fmt.Println(RollingSum([]int{1, 2, 3, 4}))
}
