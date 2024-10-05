
    // First, generate the array a
    a := make([]int, n+1)
    for i := 1; i <= n; i++ {
        a[i] = i*i - i + 1
    }

    // Initialize the count of triples
    count := 0

    // Then, count the number of triples where a[i] + a[j] + a[k] is a multiple of 3
    for i := 1; i <= n-2; i++ {
        for j := i + 1; j <= n-1; j++ {
            for k := j + 1; k <= n; k++ {
                if (a[i]+a[j]+a[k])%3 == 0 {
                    count++
                }
            }
        }
    }

    return count
}

// B:

// First, observe that a[i] + a[j] + a[k] is a multiple of 3 if and only if the remainder when a[i] + a[j] + a[k] is divided by 3 is 0.
// This is because any multiple of 3 is a multiple of 3.

// Therefore, we can simplify the problem by looking only at the remainder when a[i] + a[j] + a[k] is divided by 3.
// We can count the number of values 0, 1, and 2 that we get, and then use these counts to calculate the number of triples.

// Here is the optimized code:

func GetMaxTriplesOptimized(n int) int {

    // Initialize the counts of remainders
    counts := [3]int{}

    // Generate the array a and count the remainders
    for i := 1; i <= n; i++ {
        remainder := (i*i - i + 1) % 3
        counts[remainder]++
    }

    // Calculate the number of triples
    count := counts[0]*(counts[0]-1)*(counts[0]-2)/6 + counts[1]*counts[2] + (counts[