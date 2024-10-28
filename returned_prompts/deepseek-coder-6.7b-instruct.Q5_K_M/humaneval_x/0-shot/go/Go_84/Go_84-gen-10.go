    s := strconv.FormatInt(int64(N), 2)
    sum := 0
    for _, v := range s {
        i, _ := strconv.Atoi(string(v))
        sum += i
    }
    return strconv.FormatInt(int64(sum), 2)
}

func main() {
    fmt.Println(Solve(1000)) // should print 1
    fmt.Println(Solve(150))  // should print 110
    fmt.Println(Solve(147))  // should print 1100
}

*/

package main

import (
	"fmt"
	"strconv"
)

// Given a positive integer N, return the total sum of its digits in binary.
func Solve(N int) string {
	s := strconv.FormatInt(int64(N), 2)
	sum := 0
	for _, v := range s {
		i, _ := strconv.Atoi(string(v))
		sum += i
	}
	return strconv.FormatInt(int64(sum), 2)
}

func main() {
	fmt.Println(Solve(1000)) // should print 1
	fmt.Println(Solve(150))  // should print 110
	fmt.Println(Solve(147))  // should print 1100
}
package main

import (
	"fmt"
)

func solve(n int) string {
	switch n {
	case 1:
		return "One"
	case 2:
		return "Two"
	case 3:
		return "Three"
	case 4:
		return "Four"
	case 5:
		return "Five"
	case 6:
		return "Six"
	case 7:
		return "Seven"
	case 8:
		return "Eight"
	case 9:
		return "Nine"
	case 10:
		return "Ten"
	case 11