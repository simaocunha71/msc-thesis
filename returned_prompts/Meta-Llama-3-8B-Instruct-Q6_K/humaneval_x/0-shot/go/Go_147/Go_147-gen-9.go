// Create an array a of length n
a := make([]int, n)
for i := 1; i <= n; i++ {
    a[i-1] = i*i - i + 1
}

// Initialize count of triples
count := 0

// Iterate over the array
for i := 0; i < n; i++ {
    for j := i + 1; j < n; j++ {
        for k := j + 1; k < n; k++ {
            // Check if a[i] + a[j] + a[k] is a multiple of 3
            if (a[i] + a[j] + a[k])%3 == 0 {
                count++
            }
        }
    }
}

// Return the count of triples
return count
}
