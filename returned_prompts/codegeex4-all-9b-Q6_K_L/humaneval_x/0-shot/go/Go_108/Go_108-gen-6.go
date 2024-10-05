import (
	"fmt"
	"math"
)

func CountNums(arr []int) int {
	count := 0
	for _, num := range arr {
		digits := int(math.Abs(float64(num)))
		sum := 0
		for digits != 0 {
			digit := digits % 10
			sum += digit
			digits /= 10
		}
		if sum > 0 {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(CountNums([]))          // 0
	fmt.Println(CountNums([]{-1, 11, -11})) // 1
	fmt.Println(CountNums([]{1, 1, 2})) // 3
}