
    public static int closestInteger(String value) {
        double doubleValue = Double.parseDouble(value);
        int intValue = (int) doubleValue;
        double decimalValue = doubleValue - intValue;

        if (decimalValue < 0.5) {
            return intValue;
        } else {
            return intValue + (decimalValue < 0.5 ? -1 : 1);
        }
    }

    public static void main(String[] args) {
        System.out.println(closestInteger("10"));
        System.out.println(closestInteger("15.3"));
        System.out.println(closestInteger("14.5"));
        System.out.println(closestInteger("-14.5"));
    }
}


A: The problem is that you are trying to solve an invalid problem. It seems like you are trying to parse a string to an int, but the string can contain floating point numbers, and you want to round them.
However, in Java, the parseInt method can only parse strings that represent integers, and not floating point numbers. 
You should use parseDouble method to parse the string to a double, then use Math.round to round the double to the nearest integer.
Here is the corrected code:
public static int closestInteger(String value) {
    double doubleValue = Double.parseDouble(value);
    return Math.round(doubleValue);
}

public static void main(String[] args) {
    System.out.println(closestInteger("10")); // should print 10
    System.out.println(closestInteger("15.3")); // should print 15
    System.out.println(closestInteger("14.5")); // should print 15
    System.out.println(closestInteger("-14.5")); // should print -15
}


A: In the function, you're trying to convert a string to an integer, which is not possible. You need to use Double.parseDouble() to convert the string to a double, then use Math.round() to round the double to the nearest integer.
Here is the corrected code:
import java.lang.*;

public class S