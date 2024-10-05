// Initialize an array of size n
a := make([]int, n)
// Initialize count of triples
count := 0
// Iterate over the array
for i := 1; i <= n; i++ {
    // Calculate the value of a[i]
    a[i-1] = i * i - i + 1
}
// Iterate over the array
for i := 0; i < n; i++ {
    // Iterate over the array from i+1 to n-1
    for j := i + 1; j < n; j++ {
        // Iterate over the array from j+1 to n-1
        for k := j + 1; k < n; k++ {
            // Check if a[i] + a[j] + a[k] is a multiple of 3
            if (a[i] + a[j] + a[k])%3 == 0 {
                // Increment the count of triples
                count++
            }
        }
    }
}
// Return the count of triples
return count
}
B:

// You are given a positive integer n. You have to create an integer array a of length n.
// For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
// Return the number of triples (a[i], a[j], a[k]) of a where i < j < k,
// and a[i] + a[j] + a[k] is a multiple of 3.
// 
// Example :
// Input: n = 5
// Output: 1
// Explanation:
// a = [1, 3, 7, 13, 21]
// The only valid triple is (1, 7, 13).
func GetMaxTriples(n int) int {
    a := make([]int, n)
    count := 0
    for i := 1; i <= n; i++ {
        a[i-1] = i * i - i + 1
    }
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            for k := j + 1; k < n; k++ {
                if (a[i] + a[j] + a[k])%3 == 0 {
                    count++
                }
            }
        }
    }
    return count
