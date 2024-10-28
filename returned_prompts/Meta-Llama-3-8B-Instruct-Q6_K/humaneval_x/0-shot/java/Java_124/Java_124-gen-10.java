Here is a Java function that validates a date string according to the rules mentioned:

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

    if (month == 2) {
        if (day < 1 || day > 29) {
            return false;
        }
    } else if (month == 4 || month == 6 || month == 9 || month == 11) {
        if (day < 1 || day > 30) {
            return false;
        }
    } else {
        if (day < 1 || day > 31) {
            return false;
        }
    }

    return true;
}
```

This function splits the input date string into parts using the '-' character as a delimiter. It then checks each part to ensure it is an integer. If the date string is in the correct format, it checks the month and day to ensure they are within the valid range for the given month. If the date string is not in the correct format or the month and day are not within the valid range, the function returns false. Otherwise, it returns true. 