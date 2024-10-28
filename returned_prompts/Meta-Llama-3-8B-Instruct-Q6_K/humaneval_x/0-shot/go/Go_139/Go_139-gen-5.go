// Create an empty integer variable to store the result
result := 1

// Loop through each integer from n down to 1
for i := n; i >= 1; i-- {
    // Multiply the current result by the current integer
    result *= int64(i)
}

// Return the result
return int(result)
}
