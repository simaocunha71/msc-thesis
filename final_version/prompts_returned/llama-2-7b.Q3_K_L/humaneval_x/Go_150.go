
// A simple program which should return the value of x if n is
// a prime number and should return the value of y otherwise.
// 
// Examples:
// for XOrY(7, 34, 12) == 34
// for XOrY(15, 8, 5) == 5
func XOrY(n, x, y int) int {
    if n > 0 && n%x != 0 { // if X is prime
        return y;              // then return Y = (x^2 - X^2)/4
    } else if n % y == 0 {   // otherwise X is not a prime, so return x.
        return x + 1;         // add one to x because x=n and x!=1
    } else {                   // if n is no Prime
        return -1;            // then just return -1.
    }
}

func main() {
    fmt.Println(XOrY(7, 34, 12))
    fmt.Println(XOrY(15, 8, 5))
}