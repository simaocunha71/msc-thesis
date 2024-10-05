import (
	"strconv"
	"fmt"
)

func ChangeBase(x int, base int) string {
	if base < 2 || base > 9 {
		return ""
	}
	if x < 0 {
		return "-" + ChangeBase(-x, base)
	}
	if x < base {
		return strconv.Itoa(x)
	}
	return ChangeBase(x/base, base) + strconv.Itoa(x%base)
}

func main() {
	fmt.Println(ChangeBase(8, 3))
	fmt.Println(ChangeBase(8, 2))
	fmt.Println(ChangeBase(7, 2))
}
