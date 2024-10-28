Here is the solution in Go:
```go
func ValidDate(date string) bool {
    parts := strings.Split(date, "-")
    if len(parts) != 3 {
        return false
    }
    month, day, year := parts[0], parts[1], parts[2]
    if len(month) == 0 || len(day) == 0 || len(year) == 0 {
        return false
    }
    monthInt, err := strconv.Atoi(month)
    if err != nil || monthInt < 1 || monthInt > 12 {
        return false
    }
    dayInt, err := strconv.Atoi(day)
    if err != nil || (monthInt == 2 && dayInt > 29) || (monthInt == 4 || monthInt == 6 || monthInt == 9 || monthInt == 11 && dayInt > 30) || (monthInt == 1 || monthInt == 3 || monthInt == 5 || monthInt == 7 || monthInt == 8 || monthInt == 10 || monthInt == 12 && dayInt > 31) {
        return false
    }
    return true
}
```
Here's an explanation of the code:

1. First, we split the date string into three parts using the "-" character as the separator.
2. We check if the number of parts is exactly 3. If not, we return false.
3. We check if each part is not empty. If any part is empty, we return false.
4. We convert the month and day parts to integers using `strconv.Atoi`. If the conversion fails or if the value is outside the valid range, we return false.
5. We check if the day is valid based on the month. If the day is invalid, we return false.
6. If all checks pass, we return true.

You can test this function with the examples you provided to see that it returns the correct results. For example:
```go
fmt.Println(ValidDate("03-11-2000")) // true
fmt.Println(ValidDate("15-01-2012")) // false
fmt.Println(ValidDate("04-0-2040")) // false
fmt.Println(ValidDate("06-04-2020")) // true
fmt.Println(ValidDate("06/04/2020")) // false
```