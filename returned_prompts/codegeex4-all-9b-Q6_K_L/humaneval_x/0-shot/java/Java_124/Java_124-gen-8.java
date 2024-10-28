```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean validDate(String date) {
        if (date == null || date.length() != 10 || !date.contains("-")) {
            return false;
        }
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
        if (day < 1) {
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
        } else if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day > 30) {
                return false;
            }
        } else {
            if (day > 31) {
                return false;
            }
        }
        return true;
    }
}
```

This solution checks if the date string is valid according to the given rules. It splits the date string into three parts (month, day, and year), and then checks if each part is valid. It also checks if the date is in the correct format (mm-dd-yyyy).