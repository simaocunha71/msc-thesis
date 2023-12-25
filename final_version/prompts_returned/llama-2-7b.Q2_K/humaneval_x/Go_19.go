import (
    "sort"
    "strings"
)

// Input is a space-delimited string of numberals from 'zero' to 'nine'.
// Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
// Return the string with numbers sorted from smallest to largest
// >>> SortNumbers('three one five')
// 'one three five'
func SortNumbers(numbers string) string{
    var str []string = strings.Split(numbers, " ")

    lenStr := 0
    for _, elm := range str {
        if num, _ := strconv.Atoi(elm); !strings.ContainsRune("-", num){
            str[lenStr] = elm
            lenStr++
        }
    }
    return strings.Join(str, "")
}
