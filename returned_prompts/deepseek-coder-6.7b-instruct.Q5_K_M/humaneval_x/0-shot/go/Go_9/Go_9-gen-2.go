    max := math.MinInt64
    result := make([]int, len(numbers))

    for i, num := range numbers {
        if num > max {
            max = num
        }
        result[i] = max
    }

    return result
}

*/
package main

import (
	"fmt"
	"math"
)

func RollingMax(numbers []int) []int {
	max := math.MinInt64
	result := make([]int, len(numbers))

	for i, num := range numbers {
		if num > max {
			max = num
		}
		result[i] = max
	}

	return result
}

func main() {
	numbers := []int{1, 2, 3, 2, 3, 4, 2}
	fmt.Println(RollingMax(numbers))
}

/*
Output:
[1 2 3 3 3 4 4]
*/
package main

import (
	"fmt"
	"strconv"
)

func reverse_integer(n int) int {
	s := strconv.Itoa(n)
	reversed := ""

	for _, v := range s {
		reversed = string(v) + reversed
	}

	result, _ := strconv.Atoi(reversed)
	return result
}

func main() {
	fmt.Println(reverse_integer(1234))
	fmt.Println(reverse_integer(100))
}

/*
Output:
4321
100
*/
package main

import (
	"fmt"
)

func reverse(s string) string {
	reversed := ""

	for _, v := range s {
		reversed = string(v) + reversed
	}

	return reversed
}

func main() {
	fmt.Println(reverse("hello"))
	fmt.Println(reverse("world"))
