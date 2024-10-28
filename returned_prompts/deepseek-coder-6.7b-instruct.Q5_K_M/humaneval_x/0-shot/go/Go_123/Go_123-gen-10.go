    var odds []int
    for n != 1 {
        if n%2 != 0 {
            odds = append(odds, n)
        }
        if n%2 == 0 {
            n = n / 2
        } else {
            n = 3*n + 1
        }
    }
    odds = append(