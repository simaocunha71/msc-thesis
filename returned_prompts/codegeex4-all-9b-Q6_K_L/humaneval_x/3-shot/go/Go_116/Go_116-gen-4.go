    sort.Slice(arr, func(i, j int) bool {
        // Get the binary representation of the numbers
        binary_i := fmt.Sprintf("%b", arr[i])
        binary_j := fmt.Sprintf("%b", arr[j])

        // Count the number of ones in the binary representation
        ones_i := len([]rune(binary_i))
        ones_j := len([]rune(binary_j))

        // Sort by number of ones, then by decimal value
        if ones_i < ones_j {
            return true
        } else if ones_i > ones_j {
            return false
        } else {
            return arr[i] < arr[j]
        }
    })
    return arr
}

