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
    validDate("03-11-2000") => true
    validDate("15-01-2012") => false
    validDate("04-0-2040") => false
    validDate("06-04-2020") => true
    validDate("06/04/2020") => false
     */
    public boolean validDate(String date) {
        if (date == null || date.length() < 10) return false;

        Map<Integer, String> months = new HashMap<>();

        for (int m = 1; m <= 12; m++) {
            months.put(m, "" + m);
        }

        // check month and day value are valid
        Set<String> invalidDaysOfMonths = new HashSet<>();
        invalidDaysOfMonths.add("04");
        invalidDaysOfMonths.add("05");
        invalidDaysOfMonths.add("06");
        invalidDaysOfMonths.add("07");
        invalidDaysOfMonths.add("08");
        invalidDaysOfMonths.add("09");
        invalidDaysOfMonths.add("11");
        invalidDaysOfMonths.add("1