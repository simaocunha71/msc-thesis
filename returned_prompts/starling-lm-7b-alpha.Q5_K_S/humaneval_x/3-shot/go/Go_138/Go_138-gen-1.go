    if n%2 != 0 {
        return false
    }
    return n == sumOfEvens(n, 4)
}

func sumOfEvens(n, k int) int {
    if k == 0 {
        return 0
    }
    return sumOfEvens(n, k-1) + 2
}



