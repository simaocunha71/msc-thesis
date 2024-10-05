    if len(l) < 3 {
        return false
    }
    return TriplesSumToZeroHelper(l, 0, 0, 0, 0, 0, 0)
}

func TriplesSumToZeroHelper(l []int, i int, a int, b int, c int, sum int, flag bool) bool {
    if i >= len(l) {
        return sum == 0
    }
    if flag {
        return TriplesSumToZeroHelper(l, i + 1, a, b, c, sum, false) && a + b + c == 0
    }

    if a > 0 {
        return TriplesSumToZeroHelper(l, i + 1, 0, b, c, sum, true) && b + c == 0
    }
    if b > 0 {
        return TriplesSumToZeroHelper(l, i + 1, a, 0, c, sum, true) && a + c == 0
    }
    if c > 0 {
        return TriplesSumToZeroHelper(l, i + 1, a, b, 0, sum, true) && a + b == 0
    }

    if a == 0 {
        return TriplesSumToZeroHelper(l, i + 1, 0, b, c, sum + l[i], false) && b + c == 0
    }
    if b == 0 {
        return TriplesSumToZeroHelper(l, i + 1, a, 0, c, sum + l[i], false) && a + c == 0
    }
    if c == 0 {
        return TriplesSumToZeroHelper(l, i + 1, a, b, 0, sum + l[i], false) && a + b == 0
    }

    return TriplesSumToZeroHelper(l, i + 1, a, b, c, sum, false)
}



