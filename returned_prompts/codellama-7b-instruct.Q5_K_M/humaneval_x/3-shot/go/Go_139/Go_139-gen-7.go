    result := 1

    for i := 1; i <= n; i++ {
        result *= i
        result *= SpecialFactorial(i-1)
    }
    return result
}



