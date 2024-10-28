
	for _, v := range l {
		if v >= t {
			return false
		}
	}
	return true
}

*/

package main

import (
	"fmt"
)

func BelowThreshold(l []int, t int) bool {

	for _, v := range l {
		if v >= t {
			return false
		}
	}
	return true
}

func main() {

	l := []int{1, 2, 4, 10}
	t := 100
	fmt.Println(BelowThreshold(l, t)) // true

	l2 := []int{1, 20, 4, 10}
	t2 := 5
	fmt.Println(BelowThreshold(l2, t2)) // false

}
package main

import (
	"fmt"
	"math"
)

func main() {

	var radius float64
	fmt.Print("Enter the radius of the circle: ")
	fmt.Scan(&radius)

	area := math.Pi * math.Pow(radius, 2)
	circumference := 2 * math.Pi * radius

	fmt.Printf("The area of the circle is: %.2f\n", area)
	fmt.Printf("The circumference of the circle is: %.2f\n", circumference)

}
package main

import (
	"fmt"
	"strconv"
)

func main() {

	var binary string
	fmt.Print("Enter a binary number: ")
	fmt.Scan(&binary)

	decimal, err := strconv.ParseInt(binary, 2, 64)
	if err != nil {
		fmt.Println("Invalid binary number")
		return
	}

	fmt.Printf("The decimal equivalent of the binary number %s is: %d\n", binary, decimal)

}
package main

import (
	"fmt"
	"strconv"
)

func main() {

	var decimal int
	fmt.Print("Enter a