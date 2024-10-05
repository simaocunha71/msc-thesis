```java
import java.util.*;
import java.lang.*;

class Solution {
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
            if (day > 29) {
                return false;
            }
            if (day == 29 && !isLeapYear(year)) {
                return false;
            }
        } else if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day > 30) {
                return false;
            }
        }

        return true;
    }

    private boolean isLeapYear(int year) {
        if (year % 4 != 0) {
            return false;
        } else if (year % 100 != 0) {
            return true;
        } else if (year % 400 != 0) {
            return false;
        } else {
            return true;
        }
    }
}
```

The above code validates a given date string and returns true if the date is valid otherwise false. It checks if the date string is not empty, the number of days is within the valid range for the given month, the months should not be less than 1 or higher than 12, and the date should be in the format: mm-dd-yyyy. It also includes a helper method to check if a given year is a leap year.