    switch a := a.(type) {
    case int:
        if b, ok := b.(int); ok {
            if a > b {
                return a
            } else if a == b {
                return nil
            } else {
                return b
            }
        }
    case float64:
        if b, ok := b.(float64); ok {
            if a > b {
                return a
            } else if a == b {
                return nil
            } else {
                return b
            }
        }
    case string:
        if b, ok := b.(string); ok {
            a = strings.Replace(a, ",", ".", -1)
            b = strings.Replace(b, ",", ".", -1)
            aFloat, _ := strconv.ParseFloat(a, 64)
            bFloat, _ := strconv.ParseFloat(b, 64)
            if aFloat > bFloat {
                return a
            } else if aFloat == bFloat {
                return nil
            } else {
                return b
            }
        }
    }
    return nil
}

func main() {
    fmt.Println(CompareOne(1, 2.5))
    fmt.Println(CompareOne(1, "2.3"))
    fmt.Println(CompareOne("5.1", "6"))
    fmt.Println(CompareOne("1", 1))
}

*/
package main

import (
	"fmt"
	"strconv"
	"strings"
)

func CompareOne(a, b interface{}) interface{} {

	switch a := a.(type) {
	case int:
		if b, ok := b.(int); ok {
			if a > b {
				return a
			} else if a == b {
				return nil
			} else {
				return b
			}
		}
	case float64:
		if b, ok := b.(float64); ok {
			if a > b {
				return a
			} else if a == b {
				return nil
			} else {
			