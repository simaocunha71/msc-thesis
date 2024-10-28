    if a == b {
        return nil
    } else if a.(int) > b.(int) {
        return a
    } else if a.(int) < b.(int) {
        return b
    } else if a.(float64) > b.(float64) {
        return a
    } else if a.(float64) < b.(float64) {
        return b
    } else if a.(string) == b.(string) {
        return nil
    } else if a.(string) > b.(string) {
        return a
    } else {
        return b
    }
}

// CompareTwo(1, 2.5) ➞ (2.5, nil)
// CompareTwo(1, "2,3") ➞ (2,3, nil)
// CompareTwo("5,1", "6") ➞ (6, nil)
// CompareTwo("1", 1) ➞ (1, nil)
func CompareTwo(a, b interface{}) (interface{}, interface{}) {
    if a == b {
        return nil, nil
    } else if a.(int) > b.(int) {
        return a, nil
    } else if a.(int) < b.(int) {
        return b, nil
    } else if a.(float64) > b.(float64) {
        return a, nil
    } else if a.(float64) < b.(float64) {
        return b, nil
    } else if a.(string) == b.(string) {
        return nil, nil
    } else if a.(string) > b.(string) {
        return a, nil
    } else {
        return nil, b
    }
}

func main() {
    fmt.Println(CompareOne(1, 2.5))           // 2.5
    fmt.Println(CompareOne(1, "2,3"))         // "2,3"
    fmt.Println(CompareOne("5,1", "6"))       // "6"
    fmt.Println(CompareOne("1", 1))           // nil

