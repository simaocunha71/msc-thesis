import java.util.*;

public class Solution {

    public static int closestInteger(String value) {
        double num = Double.parseDouble(value);
        int integerPart = (int) num;
        if (num - integerPart < 0.5) {
            return integerPart;
        } else {
            return integerPart + 1;
        }
    }

    public static void main(String[] args) {
        System.out.println(closestInteger("10")); // prints 10
        System.out.println(closestInteger("15.3")); // prints 15
    }
}
