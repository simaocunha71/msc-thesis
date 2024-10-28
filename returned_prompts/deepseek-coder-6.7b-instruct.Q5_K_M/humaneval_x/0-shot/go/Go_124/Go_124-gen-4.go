    if date == "" {
        return false
    }

B:
    parts := strings.Split(date, "-")
    if len(parts) != 3 || len(parts[0]) != 2 || len(parts[1]) != 2 || len(parts[2]) != 4 {
        return false
    }

C:
    month, err := strconv.Atoi(parts[0])
    if err != nil || month < 1 || month > 12 {
        return false
    }

D:
    day, err := strconv.Atoi(parts[1])
    if err != nil || day < 1 || day > 31 {
        return false
    }

E:
    year, err := strconv.Atoi(parts[2])
    if err != nil {
        return false
    }

F:
    if (month == 4 || month == 6 || month == 9 || month == 11) && day > 30 {
        return false
    }

G:
    if month == 2 && day > 29 {
        return false
    }

H:
    return true
}

Note: The function strconv.Atoi is used to convert string to integer. The strconv.Atoi function returns two values, the converted integer and an error if the conversion fails. If the conversion fails, we return false.

*/

import (
	"strconv"
	"strings"
)

func ValidDate(date string) bool {

	if date == "" {
		return false
	}

	parts := strings.Split(date, "-")
	if len(parts) != 3 || len(parts[0]) != 2 || len(parts[1]) != 2 || len(parts[2]) != 4 {
		return false
	}

	month, err := strconv.Atoi(parts[0])
	if err != nil || month < 1 || month > 12 {
		return false
	}

	day, err := strconv.Atoi(parts[1])
	if err != nil || day < 1 || day > 31 {
		return false