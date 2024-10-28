Here is the Java code that validates a given date string:

```java
import java.util.*;

class Solution {
    public boolean validDate(String date) {
        if(date.isEmpty()) {
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
        
        if(month == 2) {
            if(day < 1 || day > 29) {
                return false;
            }
        } else if(month == 4 || month == 6 || month == 9 || month == 11) {
            if(day < 1 || day > 30) {
                return false;
            }
        } else if(month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
            if(day < 1 || day > 31) {
                return false;
            }
        }
        
        return true;
    }
}
```

In this code, we first split the date string into three parts using the dash as a delimiter. Then we parse each part into an integer. We check if the month is between 1 and 12, and if the day is valid for that month. Finally, we return true if the date is valid, and false otherwise. 