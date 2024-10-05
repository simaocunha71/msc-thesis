Here is the solution in Java:

```java
public boolean validDate(String date) {
    if(date == null || date.length() < 10) {
        return false;
    }
    String[] parts = date.split("-");
    if(parts.length != 3) {
        return false;
    }
    int month = Integer.parseInt(parts[0]);
    int day = Integer.parseInt(parts[1]);
    int year = Integer.parseInt(parts[2]);
    if(month < 1 || month > 12) {
        return false;
    }
    if(year < 1) {
        return false;
    }
    if((month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) && day > 31) {
        return false;
    }
    if((month == 4 || month == 6 || month == 9 || month == 11) && day > 30) {
        return false;
    }
    if(month == 2) {
        if(day > 29 || (day == 29 && !isLeapYear(year))) {
            return false;
        }
    }
    return true;
}

public boolean isLeapYear(int year) {
    return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
}
```

In this solution, we first split the date string into three parts: month, day, and year. Then we validate the month, day, and year according to the rules given. We also have a helper function `isLeapYear` to check if a year is a leap year or not. If the date is valid according to the rules, we return true; otherwise, we return false.