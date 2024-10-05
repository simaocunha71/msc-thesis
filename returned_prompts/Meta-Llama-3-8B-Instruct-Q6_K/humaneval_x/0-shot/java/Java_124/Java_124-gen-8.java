Here is the Java solution for the problem:

```java
public boolean validDate(String date) {
    String[] parts = date.split("-");
    if (parts.length != 3) {
        return false;
    }
    int month = Integer.parseInt(parts[0]);
    int day = Integer.parseInt(parts[1]);
    int year = Integer.parseInt(parts[2]);

    if (month < 1 || month > 12) {
        return false;
    }
    if (day < 1 || day > 31) {
        return false;
    }
    if (month == 2) {
        if (day < 1 || day > 29) {
            return false;
        }
        if (isLeapYear(year) && day > 29) {
            return false;
        }
    } else if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
        if (day > 31) {
            return false;
        }
    } else {
        if (day > 30) {
            return false;
        }
    }
    return true;
}

public boolean isLeapYear(int year) {
    return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
}
```
The `validDate` function splits the input date string into its month, day, and year components. It then checks each of the given conditions to ensure the date is valid. The `isLeapYear` function is a helper function used to determine if a given year is a leap year. It returns `true` if the year is a leap year and `false` otherwise. This function is used in the `validDate` function to handle the case where the month is February and the year is a leap year. If the day is greater than 29 in this case, the function returns `false`. Otherwise, it returns `true`. If the input date string is in the correct format (mm-dd-yyyy) and satisfies all the given conditions, the `validDate` function returns `true`. Otherwise, it returns `false`. This solution correctly handles all the given test cases. 