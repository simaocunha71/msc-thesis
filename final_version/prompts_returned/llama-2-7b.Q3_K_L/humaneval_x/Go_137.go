import (
    "fmt"
    "strconv"
    "strings"
)

// Create a function that takes integers, floats, or strings representing
// real numbers, and returns the larger variable in its given variable type.
// Return nil if the values are equal.
// Note: If a real number is represented as a string, the floating point might be . or ,
// 
// CompareOne(1, 2.5) ➞ 2.5
// CompareOne(1, "2,3") ➞ "2,3"
// CompareOne("5,1", "6") ➞ "6"
// CompareOne("1", 1) ➞ nil
func CompareOne(a, b interface{}) interface{} {
    if v1, ok := a.(float64); ok && (v2 := b).(float64) != v1 { // if the types are a float64 and another type:
        return v2
    } else if v1, ok := a.(int); ok && (v2 := b).(int) != v1 { // if one of them is an int.
        return v2
    } else if v1, ok := a.(string); ok && v2 == "" {
        return v2
    }
    
    fmt.Println("The variable types are different")
    return nil
}