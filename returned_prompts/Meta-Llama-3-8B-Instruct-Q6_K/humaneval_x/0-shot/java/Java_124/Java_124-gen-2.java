Here is the solution:

```java
import java.util.*;

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
            if (day < 1 || day > 29) {
                return false;
            }
        } else if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day < 1 || day > 30) {
                return false;
            }
        } else if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
            if (day < 1 || day > 31) {
                return false;
            }
        }
        return true;
    }
}
```

This solution works by splitting the date string into its constituent parts (month, day, year), then checking each part against the rules for a valid date. If any part fails to meet the rules, the function returns false. If all parts meet the rules, the function returns true. 

The rules are as follows:

* The month should be between 1 and 12.
* The day should be between 1 and 31.
* If the month is February, the day should be between 1 and 29.
* If the month is April, June, September, or November, the day should be between 1 and 30.
* If the month is January, March, May, July, August, October, or December, the day should be between 1 and 31.

The function uses a series of if-else statements to check each part of the date against these rules. If any part fails to meet the rules, the function returns false. If all parts meet the rules, the function returns true. 

This solution assumes that the input date string is in the format "mm-dd-yyyy". It does not handle dates in other formats, such as "dd-mm-yyyy" or "mm/dd