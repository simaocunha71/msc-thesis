    switch a.(type) {
    case float64:
        a = strconv.FormatFloat(a.(float64), 'f', -1, 64)
    case int:
        a = strconv.Itoa(a.(int))
    case string:
        a = a.(string)
    default:
        fmt.Println("Invalid type for a")
        return nil
    }

B:
    switch b.(type) {
    case float64:
        b = strconv.FormatFloat(b.(float64), 'f', -1, 64)
    case int:
        b = strconv.Itoa(b.(int))
    case string:
        b = b.(string)
    default:
        fmt.Println("Invalid type for b")
        return nil
    }

if strings.Replace(a.(string), ",", ".", -1) > strings.Replace(b.(string), ",", ".", -1) {
    return a
} else if strings.Replace(b.(string), ",", ".", -1) > strings.Replace(a.(string), ",", ".", -1) {
    return b
}

return nil
}

This function converts the given inputs to strings, and then compares the strings. If the string representation of the numbers contain "," as thousand separators, they are replaced with "." before comparison. If there is no string representation of the numbers, it returns an error message.
*/
package main

import (
	"fmt"
)

func CompareOne(a, b interface{}) interface{} {

	switch a := a.(type) {
	case float64:
		a = strconv.FormatFloat(a, 'f', -1, 64)
	case int:
		a = strconv.Itoa(a)
	case string:
		a = a
	default:
		fmt.Println("Invalid type for a")
		return nil
	}

	switch b := b.(type) {
	case float64:
		b = strconv.FormatFloat(b, 'f', -1, 64)
	case int:
