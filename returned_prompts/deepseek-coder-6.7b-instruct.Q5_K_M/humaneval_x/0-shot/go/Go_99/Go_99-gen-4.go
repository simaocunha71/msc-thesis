    floatValue, err := strconv.ParseFloat(value, 64)
    if err != nil {
        panic(err)
    }

B:
    roundedValue := math.Round(floatValue)
    if roundedValue == floatValue {
        return int(roundedValue)
    }

C:
    if strings.Contains(value, ".") {
        decimals := value[strings.Index(value, ".")+1:]
        if len(decimals) > 1 {
            deciPart, err := strconv.Atoi(decimals[:1])
            if err != nil {
                panic(err)
            }
            if deciPart >= 5 {
                if floatValue > 0 {
                    roundedValue = math.Ceil(floatValue)
                } else {
                    roundedValue = math.Floor(floatValue)
                }
            }
        }
    }

    return int(roundedValue)
}

func main() {
    fmt.Println(ClosestInteger("10")) // 10
    fmt.Println(ClosestInteger("15.3")) // 15
    fmt.Println(ClosestInteger("14.5")) // 15
    fmt.Println(ClosestInteger("-14.5")) // -15
}

*/
package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func ClosestInteger(value string) int {

	floatValue, err := strconv.ParseFloat(value, 64)
	if err != nil {
		panic(err)
	}

	roundedValue := math.Round(floatValue)
	if roundedValue == floatValue {
		return int(roundedValue)
	}

	if strings.Contains(value, ".") {
		decimals := value[strings.Index(value, ".")+1:]
		if len(decimals) > 1 {
			deciPart, err := strconv.Atoi(decimals[:1])
		