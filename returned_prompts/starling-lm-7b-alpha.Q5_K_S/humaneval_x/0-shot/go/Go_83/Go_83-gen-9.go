    // Handle edge cases.
    if n == 0 {
        return 0
    }
    // Initialize result.
    var result int = 0
    // Calculate the number of 1s that can be used to start the number.
    var leadingZeros int = (1 << (n-1))
    // Calculate the number of 1s that can be used to end the number.
    var trailingOnes int = 9*pow(10, n-1) - 1
    // Calculate the result.
    result = leadingZeros + trailingOnes
    // Return the result.
    return result
}

func pow(base, exponent int) int {
    result := 1
    for i := 0; i < exponent; i++ {
        result *= base
    }
    return result
}

// Test the StartsOneEnds function.
func TestStartsOneEnds(t *testing.T) {
    tests := []struct {
        N    int
        Want int
    }{
        {1, 9},
        {2, 90},
        {3, 900},
        {4, 9000},
    }
    for _, test := range tests {
        got := StartsOneEnds(test.N)
        if got != test.Want {
            t.Errorf("StartsOneEnds(%d) = %d; want %d", test.N, got, test.Want)
        }
    }
}



























































































































































