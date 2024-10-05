
// Initialize count to store number of triples
count := 0

// Initialize array a
a := make([]int, n)

// Populate array a
for i := 1; i <= n; i++ {
    a[i-1] = i*i - i + 1
}

// Check all possible triples
for i := 0; i < n; i++ {
    for j := i + 1; j < n; j++ {
        for k := j + 1; k < n; k++ {
            // If sum of a[i], a[j], a[k] is a multiple of 3, increment count
            if (a[i]+a[j]+a[k])%3 == 0 {
                count++
            }
        }
    }
}

return count
}

func main() {
    n := 5
    fmt.Println(GetMaxTriples(n))  // Output: 1
}

// In the given code, the function GetMaxTriples(n int) calculates the number of triples (a[i], a[j], a[k]) in an array a such that a[i] + a[j] + a[k] is a multiple of 3.
// The array a is populated with values of the form i*i - i + 1.
// Then, the function checks all possible combinations of i < j < k in the array and increments the counter if the sum of a[i], a[j], and a[k] is a multiple of 3.
// Finally, the function returns the count of such triples.
// The time complexity of this function is O(n^3) because of the three nested loops.
// The space complexity of this function is O(n) for the array a.

```

**Complexity Analysis:**

Time Complexity: The time complexity of this function is O(n^3) because of the three nested loops.

Space Complexity: The space complexity of this function is O(n) for the array a.

**Explanation:**

The function GetMaxTriples(n int) calculates the number of triples (