
    for i := n / 2; i >= 1; i-- {
        if n%i == 0 {
            return i
        }
    }
    return 0
}


// QUESTION 2:

// Given two integers, return the sum of all the integers between them, inclusive.
// For example, sumBetween(2, 6) should return 2 + 3 + 4 + 5 + 6 = 18.

