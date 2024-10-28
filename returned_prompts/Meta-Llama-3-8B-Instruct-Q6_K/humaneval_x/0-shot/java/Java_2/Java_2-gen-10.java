    public double truncateNumber(double number) {
        int intPart = (int) number; // integer part of the number
        double decimalPart = number - intPart; // decimal part of the number
        return decimalPart;
    }
}
In this solution, we first calculate the integer part of the number using the cast `(int)`.

Then, we calculate the decimal part by subtracting the integer part from the original number.

Finally, we return the decimal part.

The time complexity of this solution is O(1) as it involves a constant number of operations. The space complexity is O(1) as it only uses a constant amount of space to store the integer part and decimal part.