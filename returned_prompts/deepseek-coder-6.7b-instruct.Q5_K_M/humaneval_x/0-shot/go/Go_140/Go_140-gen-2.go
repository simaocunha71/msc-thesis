
    // Convert the string to a rune slice
    runes := []rune(str)
    
    // Reverse the rune slice
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    
    // Convert the rune slice back to a string
    reversed := string(runes)
    
    return reversed
}

// Test
f