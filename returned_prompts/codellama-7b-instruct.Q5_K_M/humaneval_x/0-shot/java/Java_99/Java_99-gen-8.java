import java.util.*;
import java.lang.*;

class Solution {
    /**
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
     */
    public int countUpper(String value) {

        // If the value is null or empty, return 0
        if (value == null || value.isEmpty()) {
            return 0;
        }

        // Remove all non-digit characters from the string
        // and convert the remaining digits to int
        int number = Integer.parseInt(value.replaceAll("\\D", ""));

        // Return the number of uppercase characters in the string
        return number;
    }
}
