import (
	"strconv"
	"strings"
)

func FruitDistribution(s string, n int) int {
	str := strings.Split(s, " ")
	apples, _ := strconv.Atoi(str[0])
	oranges, _ := strconv.Atoi(str[4])
	return n - apples - oranges
}
