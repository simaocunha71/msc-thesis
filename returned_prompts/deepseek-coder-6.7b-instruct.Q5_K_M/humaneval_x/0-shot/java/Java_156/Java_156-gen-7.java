        String[] symbols = {"i", "iv", "v", "ix", "x", "xl", "l", "xc", "c", "cd", "d", "cm", "m"};
        int[] values = {1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000};

        StringBuilder roman = new StringBuilder();

        for (int i = 12; i >= 0; i--) {
            while (number >= values[i]) {
                number -= values[i];
                roman.append(symbols[i]);
            }
        }

        return roman.toString();
    }
}

This solution uses a while loop to subtract the maximum possible value from the given number and append the corresponding roman numeral symbol to a StringBuilder. This continues until the number is less than the current value. This process is repeated for all possible roman numeral values in descending order. The final string is the roman numeral equivalent of the given number.

This solution works within the given restrictions, as it starts from the largest possible roman numeral value and works its way down, avoiding the need to calculate the roman numeral values for smaller numbers first.

This solution has a time complexity of O(1), as it only iterates over a fixed number of elements. The space complexity is also O(1), as it only uses a fixed amount of space to store the roman numeral symbols and values.

This solution assumes that the input number is always a positive integer within the given restrictions. If this is not the case, the solution should be modified to handle these edge cases.

This solution could be further optimized by using a more efficient algorithm or data structure, but it is generally efficient for the given range of input values.
    }
}

This code is a solution to the problem of converting an integer to its roman numeral equivalent. It uses a while loop to subtract the largest possible roman numeral value from the given number and append the corresponding roman numeral symbol to the result string. This process is repeated for all possible roman numeral values. The final string is the roman numeral equivalent of the given number.

This solution assumes