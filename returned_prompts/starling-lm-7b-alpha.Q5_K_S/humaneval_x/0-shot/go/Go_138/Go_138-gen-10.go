
func IsEqualToSumEven(n int) bool {
    return n >= 4 && n%2 == 0 && n%4 == 0
}

    // Corner cases
    if n < 4 {
        return false
    }

    // If n is even and divisible by 4, we can directly return true
    if n%2 == 0 && n%4 == 0 {
        return true
    }

    // Initialize a cache to store the results of subproblems
    dp := make(map[int]bool)

    // Base case
    // If n is divisible by 4, we can express it as the sum of exactly 4 positive even numbers
    dp[n] = true

    // Iterate through all possible values of a, b, c, d
    for a := n / 4; a >= 0; a-- {
        for b := a * 2; b < n / 2; b += 2 * a {
            for c := b; c < n / 2; c++ {
                d := n - b - c
                if d < 0 {
                    break
                }
                if d < 4 {
                    continue
                }
                dp[d] = true
            }
        }
    }

    return dp[n]
}



// Time Complexity: O(n)
// We only need to consider all the possible values of a, b, c, d, which are all less than n.

// Space Complexity: O(n)
// We use a map to store the results of subproblems, which can have at most n distinct values.





















































































































