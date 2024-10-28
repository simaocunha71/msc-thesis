```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean validDate(String date) {
        // Check if the date string is empty
        if (date.isEmpty()) {
            return false;
        }

        // Check if the date string is in the correct format
        String[] parts = date.split("-");
        if (parts.length != 3) {
            return false;
        }

        // Check if the date string has the correct number of parts
        int month, day, year;
        try {
            month = Integer.parseInt(parts[0]);
            day = Integer.parseInt(parts[1]);
            year = Integer.parseInt(parts[2]);
        } catch (NumberFormatException e) {
            return false;
        }

        // Check if the month is valid
        if (month < 1 || month > 12) {
            return false;
        }

        // Check if the day is valid for the month
        if ((month == 4 || month == 6 || month == 9 || month == 11) && (day < 1 || day > 30)) {
            return false;
        } else if ((month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) && (day < 1 || day > 31)) {
            return false;
        } else if (month == 2) {
            // Check if the day is valid for February
            if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
                if (day < 1 || day > 29) {
                    return false;
                }
            } else {
                if (day < 1 || day > 28) {
                    return false;
                }
            }
        }

        // Check if the year is valid
        if (year < 1) {
            return false;
        }

        return true;
    }
}
```