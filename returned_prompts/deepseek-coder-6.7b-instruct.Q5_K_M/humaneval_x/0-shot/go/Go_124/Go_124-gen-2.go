    if date == "" {
        return false
    }

B:
    splitDate := strings.Split(date, "-")
    if len(splitDate) != 3 {
        return false
    }

C:
    month, errM := strconv.Atoi(splitDate[0])
    day, errD := strconv.Atoi(splitDate[1])
    year, errY := strconv.Atoi(splitDate[2])

    if errM != nil || errD != nil || errY != nil {
        return false
    }

D:
    if month < 1 || month > 12 {
        return false
    }

E:
    if month == 2 {
        if day < 1 || day > 29 {
            return false
        }
    } else if month == 4 || month == 6 || month == 9 || month == 11 {
        if day < 1 || day > 30 {
            return false
        }
    } else {
        if day < 1 || day > 31 {
            return false
        }
    }

F:
    if year < 1 {
        return false
    }

G:
    return true
}

*/

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
// ValidDate