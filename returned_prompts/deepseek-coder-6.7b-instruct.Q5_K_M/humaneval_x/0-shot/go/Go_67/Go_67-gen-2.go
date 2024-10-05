	apples := strings.Fields(s)[0]
	oranges := strings.Fields(s)[4]

	apple_num, _ := strconv.Atoi(apples)
	orange_num, _ := strconv.Atoi(oranges)

	total_fruits := apple_num + orange_num

	mango_fruits := n - total_fruits

	return mango_fruits
}

func main() {

}
*/

import (
	"strconv"
	"strings"
)

func FruitDistribution(s string, n int) int {
	apples := strings.Fields(s)[0]
	oranges := strings.Fields(s)[4]

	apple_num, _ := strconv.Atoi(apples)
	orange_num, _ := strconv.Atoi(oranges)

	total_fruits := apple_num + orange_num

	mango_fruits := n - total_fruits

	return mango_fruits
}

func main() {

}

/*
func FruitDistribution(s string, n int) int {
	split := strings.Split(s, " ")
	apples, _ := strconv.Atoi(split[2])
	oranges, _ := strconv.Atoi(split[6])
	fruits := apples + oranges
	return n - fruits
}

func main() {
	fmt.Println(FruitDistribution("5 apples and 6 oranges", 19))
}
*/
package main

import "fmt"

// 