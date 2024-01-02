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
func FruitDistribution(s string,n int) int {
	var i,j,k,l int
	v :=strings.Split(s," ")
	for ;i<len(v);++{
		if (v[i] == "apples"){
			a = i+1
		}else if (v[i] == "oranges" ){
			o=i + 1
		} else {
			mangoes = i + 1
		}

		k = a - 1
		l = o-1
		n -= k+l
	}
	return n

}
func main() {
	var s string,n int
	s = "5 apples and 6 oranges"
	fmt.Println(FruitDistribution(s,19))
	s = "0 apples and 1 orange"
	fmt.Printf("FruitDistribution(\"%v\", %d) ->\n",s,13)
	s = "2 apples and 3 oranges