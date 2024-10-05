```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean validDate(String date) {
        try {
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
                if (day == 29 && year % 4 != 0) {
                    return false;
                }
            }
            if ((month == 4 || month == 6 || month == 9 || month == 11) && day > 30) {
                return false;
            }
        } catch (NumberFormatException e) {
            return false;
        }
        return true;
    }
}
```