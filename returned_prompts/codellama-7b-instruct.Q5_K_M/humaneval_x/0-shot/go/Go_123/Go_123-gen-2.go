    for {
        // 1. Collatz(1) is [1].
        if n == 1 {
            return []int{1}
        }

        // 2. returned list sorted in increasing order.
        sort.Ints(collatz)

        // 3. The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
        // 4. For example:
        // 5. GetOddCollatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    }
}

func main() {
    fmt.Println(GetOddCollatz(5))
}

// 1. Collatz(1) is [1].
// 2. returned list sorted in increasing order.
// 3. The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
// 4. For example:
// 5. GetOddCollatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
