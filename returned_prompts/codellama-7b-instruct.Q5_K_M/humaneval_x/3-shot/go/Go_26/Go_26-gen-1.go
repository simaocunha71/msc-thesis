    var result []int
    for _, number := range numbers {
        if !contains(result, number) {
            result = append(result, number)
        }
    }
    return result
}

// Check if a given element exists in the list.
func contains(numbers []int, element int) bool {
    for _, number := range numbers {
        if number == element {
            return true
        }
    }
    return false
}



