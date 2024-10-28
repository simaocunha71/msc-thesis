    xn := strings.Split(x, "/")
    dn := strings.Split(n, "/")

    xNum, _ := strconv.Atoi(xn[0])
    xDen, _ := strconv.Atoi(xn[1])
    nNum, _ := strconv.Atoi(dn[0])
    nDen, _ := strconv.Atoi(dn[1])

    xNum = xNum * nDen
    xDen = xDen * nDen

    nNum = nNum * xDen
    nDen = nDen * xDen

    if nNum % xNum == 0 {
        return true
    }
    return false
}

The solution is to convert the string representation of the fractions into integers,
then multiply the numerators by the denominators of the other fraction.
Finally, check if the new numerator of the simplified fraction is a multiple of the
denominator. If it is, return true, else return false.
*/

package main

import (
	"fmt"
)

func main() {
	fmt.Println(Simplify("1/5", "5/1"))  // Expected: true
	fmt.Println(Simplify("1/6", "2/1"))  // Expected: false
	fmt.Println(Simplify("7/10", "10/2"))  // Expected: false
}

func Simplify(x, n string) bool {
	xn := strings.Split(x, "/")
	dn := strings.Split(n, "/")

	xNum, _ := strconv.Atoi(xn[0])
	xDen, _ := strconv.Atoi(xn[1])
	nNum, _ := strconv.Atoi(dn[0])
	nDen, _ := strconv.Atoi(dn[1])

	xNum = xNum * nDen
	xDen = xDen * nDen

	nNum = nNum * xDen
	nDen = nDen * xDen

	if nNum