Here is the solution:
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

    if ((month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) && day > 31) {
        return false;
    }
    if ((month == 4 || month == 6 || month == 9 || month == 11) && day > 30) {
        return false;
    }
    if (month == 2) {
        if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) {
            if (day > 29) {
                return false;
            }
        } else {
            if (day > 28) {
                return false;
            }
        }
    }
    return true;
}
```
This function splits the date string into month, day, and year parts. Then it checks each part for validity. If any part is invalid, it returns false. If all parts are valid, it returns true. The function also handles leap years for the month of February.