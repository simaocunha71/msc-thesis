    double doubleValue = Double.parseDouble(value);

    if (doubleValue > 0) {
        return (int) Math.ceil(doubleValue);
    } else {
        return (int) Math.floor(doubleValue);
    }
}


A: You can use Math.ceil() function for positive numbers and Math.floor() for negative numbers. Here is the code:
import java.lang.Math;

public class Main {
    public static void main(String[] args) {
        System.out.println(closestInteger("10"));
        System.out.println(closestInteger("15.3"));
        System.out.println(closestInteger("14.5"));
        System.out.println(closestInteger("-14.5"));
    }

    public static int closestInteger(String value) {
        double doubleValue = Double.parseDouble(value);

        if (doubleValue > 0) {
            return (int) Math.ceil(doubleValue);
        } else {
            return (int) Math.floor(doubleValue);
        }
    }
}

This code will round the number up for positive numbers and round down for negative numbers. It will return the closest integer to the given string number.

A: You can use the Math.ceil() function for positive numbers and the Math.floor() for negative numbers. Here is the code:

public class Main {
    public static void main(String[] args) {
        System.out.println(closestInteger("10"));
        System.out.println(closestInteger("15.3"));
        System.out.println(closestInteger("14.5"));
        System.out.println(closestInteger("-14.5"));
    }

    public static int closestInteger(String value) {
        double doubleValue = Double.parseDouble(value);

        if (doubleValue > 0) {
            return (int) Math.ceil(doubleValue);
        } else {
            return (int) Math.floor(doubleValue);
        }
    }
}

This code will round the number up for positive numbers and round down for negative numbers. It will return the closest integer