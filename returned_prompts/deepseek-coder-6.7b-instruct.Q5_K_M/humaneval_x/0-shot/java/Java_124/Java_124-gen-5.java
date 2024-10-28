        if (date.equals("")) {
            return false;
        }

        String[] parts = date.split("-");
        if (parts.length != 3) {
            return false;
        }

        int month, day, year;
        try {
            month = Integer.parseInt(parts[0]);
            day = Integer.parseInt(parts[1]);
            year = Integer.parseInt(parts[2]);
        } catch (NumberFormatException e) {
            return false;
        }

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
        } else if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day > 30) {
                return false;
            }
        }

        return true;
    }
}


A: Your code seems to be correct, but there are a few improvements that could be made.

*

*You can add the year validation. The year should be in the range of 1900 to 2099 for most cases. If you want to allow years from 1000 to 2999, you can update the code.

*You can add a check for the day of February. If the year is a leap year, February should have 29 days, otherwise it should have 28 days.

*You can add a check for the valid month-day combinations. For example, in April, there are only 30 days, not 31.

*You can add a check for the valid format. The date string should be in the format "mm-dd-yyyy".

Here's your code with the improvements:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean validDate(String date) {
        if (date.equals("")) {
            return false;
        }

        if (!date.matches("\\