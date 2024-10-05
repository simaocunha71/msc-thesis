    public double truncateNumber(double number) {
        int integerPart = (int) Math.floor(number);
        double decimalPart = number - integerPart;
        return decimalPart;
    } // end of truncateNumber method

Explanation:
The given problem is asking to decompose a positive floating point number into its integer part and decimal part.
The integer part is the largest integer smaller than the given number.
The decimal part is the leftover part always smaller than 1.

In the above solution, we use the Math.floor() method to get the integer part of the number.
Then we subtract the integer part from the given number to get the decimal part.
Finally, we return the decimal part.

For example, if we call truncateNumber(3.5), the integer part will be 3 and the decimal part will be 0.5, so the method will return 0.5.