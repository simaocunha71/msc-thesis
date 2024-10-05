    f, _ := strconv.ParseFloat(value, 64)
    if f < 0 {
        return int(f - 0.5)
    } else {
        return int(f + 0.5)
    }
}

func main() {
    fmt.Println(ClosestInteger("10"))
    fmt.Println(ClosestInteger("15.3"))
    fmt.Println(ClosestInteger("14.5"))
    fmt.Println(ClosestInteger("-14.5"))
}

*/

import (
	"fmt"
	"strconv"
	"math"
)

func ClosestInteger(value string) int {
	f, _ := strconv.ParseFloat(value, 64)
	return int(math.Round(f))
}

func main() {
	fmt.Println(ClosestInteger("10"))
	fmt.Println(ClosestInteger("15.3"))
	fmt.Println(ClosestInteger("14.5"))
	fmt.Println(ClosestInteger("-14.5"))
}


// Note:
// In Go, the built-in strconv.ParseFloat function is used to convert the string value to a float64.
// Then, the math.Round function is used to round the float64 to the nearest integer.
// The resulting float64 is then converted back to an int using the int function.
// This is a more concise and efficient solution than the previous one.

// The math.Round function rounds to the nearest even number. 
// For example, math.Round(14.5) would return 15 and math.Round(-14.5) would return -15.
// This is because it rounds to the nearest even number, 
// which is why 15 is closer to 14.5 than -15 is to -14.5.
// This is the same behavior as the original problem statement.

// The use of math.Round ensures that the number is rounded to the nearest integer, 
// regardless of whether it is positive or negative.
// This