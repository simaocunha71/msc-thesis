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
    // Read date string into date variable.
    // Example: (mm-dd-yyyy)
    dateStr := strings.TrimSpace(date)
    if len(strings.Split(dateStr, "-")) == 0 || !isValidMonth(strings.ToInt(dateStr[:3])) {
        return false
    }
    // Add all the digits of the month and check whether it is within range of months as described in the question
    month := strings.TrimSpace(dateStr[3:6])
    if !isValidMonth(month) || len(strings.Split(dateStr, "-")) > 1 { // 2nd part of the test case
        return false
    } else {
        dateStr = strings.Join([]string{dateStr[:3], dateStr[6:]}, "")
   