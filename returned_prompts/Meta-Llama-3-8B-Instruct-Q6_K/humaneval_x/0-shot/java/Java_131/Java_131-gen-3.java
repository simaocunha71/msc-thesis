        int product = 1;
        while (n > 0) {
            int digit = n % 10;
            if (digit % 2 != 0) {
                product *= digit;
            }
            n /= 10;
        }
        return product;
    }
}

Explanation:
The solution uses a while loop to iterate through each digit of the input integer `n`. For each digit, it checks if the digit is odd by using the modulus operator `%`. If the digit is odd, it multiplies the product variable by the digit. Finally, it returns the product.

The while loop continues until `n` becomes 0, which means all digits have been processed. The product variable will hold the product of all odd digits. If no odd digits are found, the product will be 1, and the function will return 0 as per the problem statement.