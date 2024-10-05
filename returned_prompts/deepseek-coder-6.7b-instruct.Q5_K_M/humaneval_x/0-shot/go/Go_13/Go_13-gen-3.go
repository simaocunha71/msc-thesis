
// Initialize the variables
//  greatest common divisor
//  remainder
//  temporary variable
// 
// While b is not 0
//  remainder = a % b
//  a = b
//  b = remainder
// Return a

var gcd int
var remainder int
var temp int

if a == 0 {
    return b
}
if b == 0 {
    return a
}

for b != 0 {
    remainder = a % b
    a = b
    b = remainder
}

return a

}

// Main function
func main() {

// Print the Greatest Common Divisor of 3 and 5
fmt.Println(GreatestCommonDivisor(3, 5))

// Print the Greatest Common Divisor of 25 and 15
fmt.Println(GreatestCommonDivisor(25, 15))

}

```

The greatest common divisor (GCD) of two integers a and b is the largest number that divides both of them without leaving a remainder. The GCD is also known as the greatest common divisor, greatest common factor, highest common factor, or the greatest common measure.

The Euclidean algorithm is a method for quickly finding the greatest common divisor (GCD) of two numbers. In this algorithm, the larger number is divided by the smaller number and the remainder is found. This remainder is then divided by the remainder obtained in the previous step and so on, until the remainder is 0. The last non-zero remainder is the GCD of the two numbers.

In the code above, the Euclidean algorithm is implemented in the function GreatestCommonDivisor. The function takes two integers as input, calculates their GCD and returns the result.

The main function then tests the function with the numbers 3 and 5, and with the numbers 25 and 15, printing the results to the console.

The output of this program will be:

```
1
5
```

These are the greatest common divisors of the pairs (3, 5) and (25, 15), respectively.


## 3.3.2 Finding the Least Common Multiple (LCM)

In mathematics