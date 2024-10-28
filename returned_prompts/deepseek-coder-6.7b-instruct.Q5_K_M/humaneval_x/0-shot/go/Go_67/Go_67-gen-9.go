	apples := strings.Fields(s)[1]
	oranges := strings.Fields(s)[4]

	appleInt,_ := strconv.Atoi(apples)
	orangeInt,_ := strconv.Atoi(oranges)

	totalApples := appleInt
	totalOranges := orangeInt
	totalFruits := n

	totalMangoes := totalFruits - totalApples - totalOranges

	return totalMangoes
}

*/

package main

import (
	"fmt"
	"strconv"
	"strings"
)

func FruitDistribution(s string, n int) int {
	apples := strings.Fields(s)[1]
	oranges := strings.Fields(s)[4]

	appleInt, _ := strconv.Atoi(apples)
	orangeInt, _ := strconv.Atoi(oranges)

	totalMangoes := n - appleInt - orangeInt

	return totalMangoes
}

func main() {
	fmt.Println(FruitDistribution("5 apples and 6 oranges", 19))
	fmt.Println(FruitDistribution("0 apples and 1 oranges", 3))
	fmt.Println(FruitDistribution("2 apples and 3 oranges", 100))
	fmt.Println(FruitDistribution("100 apples and 1 oranges", 120))
}

// 19  -  5 - 6 =  8
// 3  -  0 - 1 =  2
// 95 -  2 - 3 = 88
// 120 - 100 - 1 = 19
// Output: 8, 2, 88, 19
/*
