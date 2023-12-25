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
    switch a := a.(type) {
        case int:
            return IntCompare1(a, b)
        default:
            return fmt.Errorf("%s and %s are incompatible types", reflect.TypeOf(b).GoString(), reflect.TypeOf(a))
    }
}
func IntCompare1(i int, j int) interface{} {
    ival, err := strconv.ParseInt(strconv.Itoa(j), 10, 64)
    if err != nil {
        panic(err.Error())
    }
    if i == ival { return "" } else { return ">" + IntCompare1(i, j+1) } // j++ doesn't work in golang
}