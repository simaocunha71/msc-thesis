    switch a.(type) {
    case string:
        if b.(string) > a.(string) {
            return b
        } else if b.(string) < a.(string) {
            return a
        } else {
            return nil
        }
    case int:
        if b.(int) > a.(int) {
            return b
        } else if b.(int) < a.(int) {
            return a
        } else {
            return nil
        }
    case float64:
        if b.(float64) > a.(float64) {
            return b
        } else if b.(float64) < a.(float64) {
            return a
        } else {
            return nil
        }
    default:
        fmt.Println("Error: invalid input")
        return nil
    }
}

// Create a function that takes in two numbers represented as strings, and returns the larger number.
// Note: if the strings are the same, return the original string.
// 
// CompareTwo("1", "2") ➞ "2"
// CompareTwo("1", "1") ➞ "1"
// CompareTwo("1", "1.0") ➞ "1.0"
func CompareTwo(a, b string) string {

    if a > b {
        return a
    } else if a < b {
        return b
    } else {
        return a
    }
}

// Create a function that takes in a string representing a float number, and returns the number rounded to the nearest integer.
// Note: if the number is already an integer, return the number as a string.
// 
// Round("5.5") ➞ "6"
// Round("-2.5") ➞ "-2"
// Round("10.1") ➞ "10"
func Round(f string) string {

    f, _ = strconv.ParseFloat(f, 64)
    r := math.Round(f)

    return fmt.Sprintf("%.0f", r)
}

// Create a function that takes in