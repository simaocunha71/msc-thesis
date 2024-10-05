Here is the solution in Go:
```go
func ValidDate(date string) bool {
    // Split the date string into parts
    parts := strings.Split(date, "-")

    // Check if the date string is not empty
    if len(parts) != 3 {
        return false
    }

    // Convert the date parts to integers
    month, err := strconv.Atoi(parts[0])
    day, err := strconv.Atoi(parts[1])
    year, err := strconv.Atoi(parts[2])

    // Check if the month is valid
    if month < 1 || month > 12 {
        return false
    }

    // Check if the day is valid for the given month
    var maxDay int
    switch month {
    case 1, 3, 5, 7, 8, 10, 12:
        maxDay = 31
    case 4, 6, 9, 11:
        maxDay = 30
    case 2:
        if (year%4 == 0 && year%100 != 0) || year%400 == 0 {
            maxDay = 29
        } else {
            maxDay = 28
        }
    }

    if day < 1 || day > maxDay {
        return false
    }

    // If all checks pass, the date is valid
    return true
}
```
This function uses the `strings.Split` function to split the date string into three parts: month, day, and year. It then uses the `strconv.Atoi` function to convert these parts to integers.

The function then checks if the month is valid (between 1 and 12) and if the day is valid for the given month. For the month of February, it checks if the year is a leap year and adjusts the maximum day accordingly.

Finally, the function returns `true` if all checks pass, indicating that the date is valid, and `false` otherwise.