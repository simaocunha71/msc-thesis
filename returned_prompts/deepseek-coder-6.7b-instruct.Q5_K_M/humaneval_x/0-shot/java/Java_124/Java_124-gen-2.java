        if(date.length() != 10 || date.charAt(2) != '-' || date.charAt(5) != '-') return false;

        String month = date.substring(0,2);
        String day = date.substring(3,5);
        String year = date.substring(6);

        if(Integer.parseInt(month) < 1 || Integer.parseInt(month) > 12) return false;

        if(Integer.parseInt(day) < 1) return false;

        if(Integer.parseInt(month) == 2){
            if(Integer.parseInt(day) > 29) return false;
        } else if(Integer.parseInt(month) == 4 || Integer.parseInt(month) == 6 || Integer.parseInt(month) == 9 || Integer.parseInt(month) == 11){
            if(Integer.parseInt(day) > 30) return false;
        } else {
            if(Integer.parseInt(day) > 31) return false;
        }

        return true;
    }
}


A: Here's an improved version of your code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    You have to write a function which validates a given date string and
    returns true if the date is valid otherwise false.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example:
    validDate("03-11-2000") ⇒