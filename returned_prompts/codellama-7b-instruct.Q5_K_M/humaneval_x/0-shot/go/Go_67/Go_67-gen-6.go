import (
	"strconv"
	"strings"
)

// In this task, you will be given a string that represents a number of apples and oranges
// that are distributed in a basket of fruit this basket contains
// apples, oranges, and mango fruits. Given the string that represents the total number of
// the oranges and apples and an integer that represent the total number of the fruits
// in the basket return the number of the mango fruits in the basket.
// for examble:
// FruitDistribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
// FruitDistribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
// FruitDistribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
// FruitDistribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
func FruitDistribution(s string, n int) int {

	// split the string into two parts
	// using the space as the separator
	parts := strings.Split(s, " ")

	// convert the first part of the string into a number
	apples, err := strconv.Atoi(parts[0])
	if err != nil {
		panic(err)
	}

	// convert the second part of the string into a number
	oranges, err := strconv.Atoi(parts[1])
	if err != nil {
		panic(err)
	}

	// calculate the total number of fruits
	total := apples + oranges

	// return the mango fruit count
	return n - total
}