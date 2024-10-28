    xn := strings.Split(x, "/")
    dn := strings.Split(n, "/")

    xNum, _ := strconv.Atoi(xn[0])
    xDen, _ := strconv.Atoi(xn[1])
    nNum, _ := strconv.Atoi(dn[0])
    nDen, _ := strconv.Atoi(dn[1])

    if (xNum * nDen) % xDen == 0 && (nNum * xDen) % nDen == 0 {
        return true
    }

    return false
}

In this code, we first split the string representation of the fractions x and n by the "/". Then we convert these string representations to integers. 

After that, we check if the product of the numerator of the first fraction and the denominator of the second fraction is divisible by the denominator of the first fraction, and if the product of the numerator of the second fraction and the denominator of the first fraction is divisible by the denominator of the second fraction. If both conditions are met, we return true; otherwise, we return false.

This is because multiplying two fractions results in a fraction. If the result is a whole number, the numerator of that fraction is divisible by the denominator, and hence the original fractions can be simplified.
*/
package main

import (
	"fmt"
)

func main() {
	fmt.Println(Simplify("1/5", "5/1"))  // true
	fmt.Println(Simplify("1/6", "2/1"))  // false
	fmt.Println(Simplify("7/10", "10/2"))  // false
}

func Simplify(x, n string) bool  {
	xn := strings.Split(x, "/")
	dn := strings.Split(n, "/")

	xNum, _ := strconv.Atoi(xn[0])
	xDen, _ := strconv.Atoi(xn[1])
	nNum, _ := strconv.Atoi(dn[0