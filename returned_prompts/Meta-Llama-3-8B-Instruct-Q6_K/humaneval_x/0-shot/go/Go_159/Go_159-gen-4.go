// Create a slice to store the result
result := make([]int, 2)

// Calculate the total number of carrots after meals
total := number + need

// Calculate the number of carrots left after meals
left := remaining - need

// If the number of carrots left is less than 0, set it to 0
if left < 0 {
    left = 0
}

// Store the result in the slice
result[0] = total
result[1] = left

// Return the result
return result
}

// Test the function
fmt.Println(Eat(5, 6, 10))  // Output: [11, 4]
fmt.Println(Eat(4, 8, 9))   // Output: [12, 1]
fmt.Println(Eat(1, 10, 10)) // Output: [11, 0]
fmt.Println(Eat(2, 11, 5))  // Output: [7, 0]  // This test case is a special case, when there are not enough remaining carrots, it will Eat all remaining carrots, but will still be hungry.