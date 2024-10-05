    for i := 0; i < len(strings); i++ {
        for j := 0; j < len(strings[i]); j++ {
            strings[i] = strings[i][len(strings[i])-j-1]
        }
    }
    return strings
}

// Given a slice of strings, returns a new slice with reversed