// Initialize an array 'a' of length 'n' with the given formula.
var a = make([]int, n)
for i := 1; i <= n; i++ {
    a[i-1] = i * i - i + 1
}

// Initialize a variable to store the count of valid triples.
var count int

// Iterate over the array 'a' with three nested loops to find valid triples.
for i := 0; i < n; i++ {
    for j := i + 1; j < n; j++ {
        for k := j + 1; k < n; k++ {
            // Calculate the sum of the current triple.
            sum := a[i] + a[j] + a[k]
            // Check if the sum is a multiple of 3 and increment the count if true.
            if sum%3 == 0 {
                count++
            }
        }
    }
}

// Return the count of valid triples.
return count
}