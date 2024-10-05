```go
func ParseNestedParens(paren_string string) []int {
    // Split input string into groups
    groups := strings.Split(paren_string, " ")

    // Initialize an array to store the maximum nesting levels for each group
    max_levels := make([]int, 0, len(groups))

    // Iterate over each group
    for _, group := range groups {
        // Initialize variables to track the current level of nesting and the maximum level of nesting found
        current_level := 0
        max_level := 0

        // Iterate over each character in the group
        for _, char := range group {
            // If the character is an opening parenthesis, increment the current level of nesting
            if char == '(' {
                current_level++
                // Update the maximum level of nesting found if necessary
                max_level = int(math.Max(float64(max_level), float64(current_level)))
            // If the character is a closing parenthesis, decrement the current level of nesting
            } else if char == ')' {
                current_level--
            }
        }

        // Append the maximum level of nesting found for the group to the array
        max_levels = append(max_levels, max_level)
    }

    // Return the array of maximum nesting levels for each group
    return max_levels
}
```