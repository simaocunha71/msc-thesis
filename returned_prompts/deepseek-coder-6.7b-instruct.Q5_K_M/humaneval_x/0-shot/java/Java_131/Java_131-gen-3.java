        int product = 1;
        boolean oddDigit = false;
        while (n > 0) {
            int digit = n % 10;
            if (digit % 2 != 0) {
                product *= digit;
                oddDigit = true;
            }
            n /= 10;
        }
        return oddDigit ? product : 0;
    }
}

This solution works by iterating through each digit of the number from right to left. If the digit is odd, we multiply the product by the digit. If at least one odd digit is found, we return the product. If no odd digit is found, we return 0.

The time complexity of this solution is O(log(n)) because we are processing each digit of the number once. The space complexity is O(1) because we are using a fixed amount of space to store the product and a flag.
    */
}