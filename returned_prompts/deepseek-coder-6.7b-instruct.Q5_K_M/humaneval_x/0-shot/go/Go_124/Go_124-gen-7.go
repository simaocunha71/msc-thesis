    if date == ""{
        return false
    }

B:
    splitDate := strings.Split(date,"-")

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
    var maxDay int

    switch month {
    case 1, 3, 5, 7, 8, 10, 12:
        maxDay = 31
    case 4, 6, 9, 11:
        maxDay = 30
    case 2:
        if (year%4==0 && year%100 != 0) || (year%400 == 0) {
            maxDay = 29
        } else {
            maxDay = 28
        }
    default:
        return false
    }

F:
    if day < 1 || day > maxDay {
        return false
    }

G:
    return true
}


A: Check if the date is not empty. If it is empty return false.
B: Split the date string by "-" into three parts: month, day, and year. If the date string does not contain "-" or does not contain exactly two "-"s return false.
C: Convert the month and day into integers. If any of the conversions fail, return false.
D: Check if the month is between 1 and 12. If it's not, return false.
E: Determine the maximum number of days for the current month.
F: Check if the day is between 1 and maxDay. If it's not, return false.
G: If all the checks pass, return true.

*/

package main

import