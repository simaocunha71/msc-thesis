    collatz := []int{}
    for n != 1 {
        if n % 2 != 0 {
            collatz = append(collatz, n)
        }
        if n % 2 == 0 {
            n = n / 2
        } else {
            n = 3 * n + 1
        }
    }
    collatz = append(collatz, 1)

B:
    sort.Ints(collatz)
    return collatz
}

// TestCases:
// GetOddCollatz(5) -> [1, 5]
// GetOddCollatz(10) -> [1, 5, 11]
// GetOddCollatz(15) -> [1, 5, 9, 13, 15]
// GetOddCollatz(20) -> [1, 5, 9, 13, 15, 19, 21, 25]
// GetOddCollatz(25) -> [1, 5, 9, 13, 15, 19, 21, 25]
// GetOddCollatz(30) -> [1, 5, 9, 13, 15, 19, 21, 25, 29, 31, 35, 37]
// GetOddCollatz(35) -> [1, 5, 9, 13, 15, 19, 21, 25, 29, 31, 35]
// GetOddCollatz(40) -> [1, 5, 9, 13, 15, 19, 21, 25, 29, 31, 35, 37, 41, 43, 47]
// GetOddCollatz(45) -> [1, 5, 9, 13, 15, 19, 21, 25,