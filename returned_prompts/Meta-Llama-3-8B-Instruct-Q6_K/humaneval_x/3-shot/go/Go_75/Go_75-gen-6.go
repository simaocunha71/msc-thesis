    for p := 2; p*p <= a; p++ {
        for q := p; q*q <= a; q++ {
            r := a / (p * q)
            if p*p + q*q == r*r {
                return true
            }
        }
    }
    return false
}  // Time Complexity: O(n^2) where n is the given number


