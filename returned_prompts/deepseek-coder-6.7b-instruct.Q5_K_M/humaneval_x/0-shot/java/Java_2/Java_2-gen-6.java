        double decimal = number % 1;
        return decimal;
    }
}

public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution sol = new Solution();
        System.out.println(sol.truncateNumber(3.5));
    }
}

The above program takes a double as input and returns the decimal part of the number.
It uses the modulus operator to get the decimal part of the number.

*/

