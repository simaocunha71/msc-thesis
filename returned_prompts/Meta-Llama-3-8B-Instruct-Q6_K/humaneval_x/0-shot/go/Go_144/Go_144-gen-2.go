```go
func Simplify(x, n string) bool {
    xNum, xDenom := parseFraction(x)
    nNum, nDenom := parseFraction(n)
    
    // Calculate the product of the fractions
    productNum := xNum * nNum
    productDenom := xDenom * nDenom
    
    // Check if the product is a whole number
    if productNum == productDenom {
        return true
    }
    
    // Check if the product is a whole number after simplification
    gcd := gcd(productNum, productDenom)
    return productNum/gcd == productDenom/gcd
}

func parseFraction(fraction string) (int, int) {
    parts := strings.Split(fraction, "/")
    numerator, _ := strconv.Atoi(parts[0])
    denominator, _ := strconv.Atoi(parts[1])
    return numerator, denominator
}

func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}
```
In this solution, we first parse the input fractions into their numerator and denominator components. We then calculate the product of the two fractions by multiplying their numerators and denominators separately. If the product is a whole number (i.e., its numerator is equal to its denominator), we return `true`. If not, we check if the product is a whole number after simplification by finding the greatest common divisor (GCD) of the product's numerator and denominator, and dividing both by the GCD. If the result is a whole number, we return `true`; otherwise, we return `false`.

The `parseFraction` function splits the input string into its numerator and denominator components using the `/` character as a separator, and then converts these components to integers using `strconv.Atoi`. The `gcd` function calculates the GCD of two integers using the Euclidean algorithm. This function is used to simplify the product of the two fractions by dividing both its numerator and denominator by their GCD.