    // First step is to convert both fractions to integers
    intX, _ := strconv.Atoi(x)
    intN, _ := strconv.Atoi(n)

    // Then, we divide the numerator of n by the numerator of x
    numerator := intX * intN

    // Then, we divide the denominator of n by the denominator of x
    denominator := intN / intX

    // Then, we simplify the fraction by dividing the numerator and the denominator by their greatest common divisor
    gcd := gcd(numerator, denominator)

    // Finally, we check if the simplified fraction is an integer
    if float64(numerator / gcd) / float64(denominator / gcd) == float64(numerator / gcd) / float64(denominator / gcd) {
        return true
    }
    return false
}

func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}

func main() {
    fmt.Println(Simplify("1/5", "5/1"))
    fmt.Println(Simplify("1/6", "2/1"))
    fmt.Println(Simplify("7/10", "10/2"))
}


















































































































































































