    result := make([]int, 0)

    for _, n := range numbers {
        if !contains(result, n) {
            result = append(result, n)
        }
    }

    return result
}

func contains(numbers []int, n int) bool {
    for _, x := range numbers {
        if x == n {
            return true
        }
    }
    return false
}



