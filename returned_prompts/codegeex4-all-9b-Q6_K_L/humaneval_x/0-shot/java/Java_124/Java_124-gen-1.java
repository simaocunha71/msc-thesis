Here is the Java solution for the problem:

```java
import java.util.*;

class Solution {
    public static boolean validDate(String date) {
        // Check if the date string is not empty
        if (date.isEmpty()) return false;

        // Check if the date is in the format mm-dd-yyyy
        String[] parts = date.split("-");
        if (parts.length != 3) return false;

        // Parse the date parts
        int month = Integer.parseInt(parts[0]);
        int day = Integer.parseInt(parts[1]);
        int year = Integer.parseInt(parts[2]);

        // Check if the month is between 1 and 12
        if (month < 1 || month > 12) return false;

        // Check if the day is valid for the month
        if (month == 2) {
            if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) {
                if (day < 1 || day > 29) return false;
            } else {
                if (day < 1 || day > 28) return false;
            }
        } else if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day < 1 || day > 30) return false;
        } else {
            if (day < 1 || day > 31) return false;
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println(validDate("03-11-2000")); // true
        System.out.println(validDate("15-01-2012")); // false
        System.out.println(validDate("04-0-2040")); // false
        System.out.println(validDate("06-04-2020")); // true
        System.out.println(validDate("06/04/2020")); // false
    }
}
```

This solution first checks if the date string is not empty. Then, it checks if the date is in the format mm-dd-yyyy. If the date is in the correct format, it parses the date parts and checks if the month is between 1 and 12. Then, it checks if the day is valid for the month. If the day is valid for the month, it returns true. Otherwise, it returns false.