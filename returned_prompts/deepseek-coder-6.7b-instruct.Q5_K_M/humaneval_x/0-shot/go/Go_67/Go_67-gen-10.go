	split:= strings.Fields(s)
	apple,_ := strconv.Atoi(split[0])
	orange,_ := strconv.Atoi(split[2])

B:
	return n - apple - orange
}

func main() {
	fmt.Println(FruitDistribution("5 apples and 6 oranges", 19)) // should print 8
	fmt.Println(FruitDistribution("0 apples and 1 oranges",3)) // should print 2
	fmt.Println(FruitDistribution("2 apples and 3 oranges", 100)) // should print 95
	fmt.Println(FruitDistribution("100 apples and 1 oranges",120)) // should print 19
}

*/

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
// FruitDistribution("5 apples and 6 oranges", 19)  -> 8
// FruitDistribution("0 apples and 1 oranges",3)  -> 2
// FruitDistribution("2 apples and 3 oranges", 100)  -> 95
// FruitDistribution("100 apples and 1 oranges",120)  -> 19
func FruitDistribution(s string, n int) int {

	split := strings.Fields(s)
	apple, _ := strconv.Atoi(split[0])
	orange, _ := strconv.Atoi(split[2])

	return n - apple - orange
}

/*

