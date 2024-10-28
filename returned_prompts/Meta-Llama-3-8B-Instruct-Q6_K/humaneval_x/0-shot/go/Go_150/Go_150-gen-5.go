// Your solution here...
if n <= 1 {
    return y
}
for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
    if n%i == 0 {
        return y
    }
}
return x

}
// The function XOrY(n, x, y) should return x if n is a prime number
// and y otherwise. It should check if n is a prime number or not
// and return the appropriate value. The function is defined above.
// The function XOrY(n, x, y) has three parameters: n, x, and y.
// n is the number to be checked for primality.
// x is the value to be returned if n is a prime number.
// y is the value to be returned if n is not a prime number. 

// The function XOrY(n, x, y) should return the value of x if n is
// a prime number and should return the value of y otherwise.

// Example 1:
// for XOrY(7, 34, 12) == 34
// Explanation: 7 is a prime number, so the function should return 34.
// Example 2:
// for XOrY(15, 8, 5) == 5
// Explanation: 15 is not a prime number, so the function should return 5.
// Example 3:
// for XOrY(23, 9, 3) == 9
// Explanation: 23 is a prime number, so the function should return 9.

// The function XOrY(n, x, y) should return the value of x if n is
// a prime number and should return the value of y otherwise.
// It should check if n is a prime number or not and return the
// appropriate value. The function is defined above. 

// The function XOrY(n, x, y) has three parameters: n, x, and y.
// n is the number to be checked for primality.
// x is the value to be returned if n is a prime number.
// y is the value to be returned if n is not a prime number. 

// The function XOrY(n, x, y) should return the value of x if n is
// a prime number and should return the value of y otherwise.
// It should check if n is a prime number or not and return the
//