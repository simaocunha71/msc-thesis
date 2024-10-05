    seen := make(map[int]bool)
    result := make([]int, 0)

    for _, num := range numbers {
        if !seen[num] {
            seen[num] = true
            result = append(result, num)
        }
    }
    return result
}  // or
func RemoveDuplicates(numbers []int) []int {
    m := make(map[int]bool)
    result := make([]int, 0)
    for _, num := range numbers {
        if !m[num] {
            m[num] = true
            result = append(result, num)
        }
    }
    return result
}  // or
func RemoveDuplicates(numbers []int) []int {
    result := make([]int, 0)
    for _, num := range numbers {
        if !contains(result, num) {
            result = append(result, num)
        }
    }
    return result
}

func contains(arr []int, target int) bool {
    for _, num := range arr {
        if num == target {
            return true
        }
    }
    return false
}  // or
func RemoveDuplicates(numbers []int) []int {
    result := []int{}
    for _, num := range numbers {
        if !contains(result, num) {
            result = append(result, num)
        }
    }
    return result
}

func contains(arr []int, target int) bool {
    for _, num := range arr {
        if num == target {
            return true
        }
    }
    return false
}  // or
func RemoveDuplicates(numbers []int) []int {
    result := make([]int, 0, len(numbers))
    for _, num := range numbers {
        if !contains(result, num) {
            result = append(result, num)
        }
    }
    return result
}

func contains(arr []int, target int) bool {
    for _, num := range arr {
        if num == target {
            return true
        }
    }
    return false
}  // or
func RemoveDuplicates(numbers []int) []int {
    m := map[int]bool{}
    result := make([]int, 0)
    for _, num := range numbers {
        if !m[num] {
            m[num] = true
            result = append(result, num)
        }
    }
    return result
}  // or
func RemoveDuplicates(numbers []int) []int {
    m := map[int]bool{}
    result := []int{}
