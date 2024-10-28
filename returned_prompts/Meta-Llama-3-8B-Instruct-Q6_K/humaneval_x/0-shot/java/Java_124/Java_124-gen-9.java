Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public boolean validDate(String date) {
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
        } else {
            if(day < 1 || day > 31) {
                return false;
            }
        }

        return true;
    }
}
```
This solution splits the input date string into three parts using the `-` character as a separator. Then it checks the validity of the date according to the rules mentioned in the problem statement. It returns `true` if the date is valid, and `false` otherwise.

For example, if the input date is `"03-11-2000"`, the function will return `true` because the date is valid. If the input date is `"15-01-2012"`, the function will return `false` because the date is not valid (the month is January, which has only 31 days). If the input date is `"04-0-2040"`, the function will return `false` because the day is invalid (it should be between 1 and 31 inclusive). If the input date is `"06-04-2020"`, the function will return `true` because the date is valid. If the input date is `"06/04/2020"`, the function will return `false` because the date is not in the correct format.