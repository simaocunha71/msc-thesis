    xNum, _ := strconv.Atoi(xn[0])
    xDen, _ := strconv.Atoi(xn[1])
    nNum, _ := strconv.Atoi(nn[0])
    nDen, _ := strconv.Atoi(nn[1])

    resultNum := xNum * nNum
    resultDen := xDen * nDen

    for i := 2; i <= resultNum && i <= resultDen; i++ {
        if resultNum%i == 0 && resultDen%i == 0 {
            resultNum /= i
            resultDen /= i
            i--
        }
    }

    if resultNum%resultDen == 0 {
        return true
    } else {
        return false
    }
}

This function will Simplify the expression x * n. The function returns true if x * n evaluates to a whole number and false otherwise. Both x and n, are string representation of a fraction, and have the following format, <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

You can assume that x, and n are valid fractions, and do not have