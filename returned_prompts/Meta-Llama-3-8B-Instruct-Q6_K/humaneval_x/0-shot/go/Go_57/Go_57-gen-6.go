// Initialize a flag
increasing := true
decreasing := true

// Iterate over the list
for i := 1; i < len(l); i++ {
    // Check if the list is increasing
    if l[i] < l[i-1] {
        increasing = false
    }
    // Check if the list is decreasing
    if l[i] > l[i-1] {
        decreasing = false
    }
}

// Check if the list is monotonic
return increasing || decreasing
}