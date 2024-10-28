func Common(l1 []int,l2 []int) []int {
    // 1. Sort the input lists
    sort.Ints(l1)
    sort.Ints(l2)

    // 2. Initialize the result list
    var result []int

    // 3. Iterate over the first list
    for _, x := range l1 {
        // 4. Check if the element is present in the second list
        if contains(l2, x) {
            // 5. If yes, add the element to the result list
            result = append(result, x)
        }
    }

    // 6. Return the result list
    return result
}

// Helper function to check if a list contains a given element
func contains(l []int, x int) bool {
    for _, y := range l {
        if y == x {
            return true
        }
    }
    return false
}

