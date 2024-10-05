import java.util.*;
import java.lang.*;

class Solution {
    /**
    In this task, you will be given a string that represents a number of apples and oranges
    that are distributed in a basket of fruit this basket contains
    apples, oranges, and mango fruits. Given the string that represents the total number of
    the oranges and apples and an integer that represent the total number of the fruits
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruitDistribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruitDistribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruitDistribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruitDistribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
     */
    public int fruitDistribution(String s, int n) {
        int mango = 0;
        int mangoCount = 0;
        int appleCount = 0;
        int orangeCount = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'a') {
                appleCount++;
            }
            if (s.charAt(i) == 'o') {
                orangeCount++;
            }
            if (s.charAt(i) == 'n') {
                mangoCount++;
            }
        }
        mango = n - appleCount - orangeCount;
        return mango;
    }
}
