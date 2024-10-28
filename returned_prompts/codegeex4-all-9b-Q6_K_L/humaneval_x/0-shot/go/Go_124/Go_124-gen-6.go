```go
import (
	"strconv"
	"strings"
)

// You have to write a function which validates a given date string and
// returns true if the date is valid otherwise false.
// The date is valid if all of the following rules are satisfied:
// 1. The date string is not empty.
// 2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
// 3. The months should not be less than 1 or higher than 12.
// 4. The date should be in the format: mm-dd-yyyy
// 
// for example:
// ValidDate('03-11-2000') => true
// 
// ValidDate('15-01-2012') => false
// 
// ValidDate('04-0-2040') => false
// 
// ValidDate('06-04-2020') => true
// 
// ValidDate('06/04/2020') => false
func ValidDate(date string) bool {
	if date == "" {
		return false
	}

	parts := strings.Split(date, "-")
	if len(parts) != 3 {
		return false
	}

	month, err := strconv.Atoi(parts[0])
	if err != nil {
		return false
	}

	day, err := strconv.Atoi(parts[1])
	if err != nil {
		return false
	}

	year, err := strconv.Atoi(parts[2])
	if err != nil {
		return false
	}

	if month < 1 || month > 12 {
		return false
	}

	if day < 1 || day > 31 {
		return false
	}

	if month == 2 {
		if day > 29 {
			return false
		}
		if day == 29 {
			if year%4 != 0 || (year%100 == 0 && year%400 != 0) {
				return false
			}
		}
	} else if (month == 4 || month == 6 || month == 9 || month == 11) && day > 30 {
		return false
	}

	return true