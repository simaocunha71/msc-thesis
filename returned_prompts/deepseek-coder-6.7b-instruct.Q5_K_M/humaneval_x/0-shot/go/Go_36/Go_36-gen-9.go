	for i := 0; i < n; i++ {
		a := strconv.Itoa(i)
		if strings.Contains(a, "7") {
			if i%11 == 0 || i%13 == 0 {
				return i
			}
		}
	}
	return 0
}

func main() {
	fmt.Println(FizzBuzz(50))
	fmt.Println(FizzBuzz(78))
	fmt.Println(FizzBuzz(79))
}

*/

package main

import (
	"fmt"
	"strconv"
	"strings"
)

// Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
func FizzBuzz(n int) int {
	for i := 0; i < n; i++ {
		a := strconv.Itoa(i)
		if strings.Contains(a, "7") {
			if i%11 == 0 || i%13 == 0 {
				return i
			}
		}
	}
	return 0
}

func main() {
	fmt.Println(FizzBuzz(50))
	fmt.Println(FizzBuzz(78))
	fmt.Println(FizzBuzz(79))
}
// package main

// import (
// 	"fmt"
// 	"strings"
// )

// // Complete the timeConversion function below.
// func timeConversion(s string) string {
// 	// Return the corrected time in 12-hour format.
// 	time := strings.Split(s, ":")
// 	hour, minute, second := time[0], time[1], time[2][:2]

// 	if strings.Contains(s, "PM") && hour != "12" {
// 		newHour, _ := strconv.Atoi(hour)
// 		newHour += 12
// 		hour = strconv.Itoa(newHour)
// 	}