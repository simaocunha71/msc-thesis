        int product = 1;
        boolean foundOdd = false;

        while (n > 0) {
            int digit = n % 10;
            if (digit % 2 != 0) {
                product *= digit;
                foundOdd = true;
            }
            n /= 10;
        }

        return foundOdd ? product : 0;
    }
}

The logic of the code is simple:
1. Initialize a variable "product" to 1 to store the product of the odd digits.
2. Initialize a boolean variable "foundOdd" to false. This will be used to check whether an odd digit is found.
3. While the input number is greater than 0, we get the last digit using n % 10.
4. If the digit is odd (checked by digit % 2 != 0), we update the product by multiplying it with the digit.
5. We also set "foundOdd" to true since we found an odd digit.
6. We then remove the last digit from the number n using n /= 10.
7. After the while loop, we check if "foundOdd" is true. If it is, we return the product. Otherwise, we return 0.
8. This is because if all digits are even, we did not multiply the product with any odd digits and hence the product remains 1. We then return 0 in such cases.
9. The time complexity of this solution is O(d), where d is the number of digits in n. This is because we are processing each digit in the number once.
10. The space complexity is O(1), as we are using a constant amount of space to store the product and the boolean variable.
*/

/*
The above solution works well for small input numbers. However, it may fail for very large numbers because the product can become very large and cause overflow.

A better approach can be to convert the number to a string and then iterate over the string. This approach will work for all positive numbers and is more efficient.

Here is the improved solution:

public int digits(int n) {
    String str = Integer.toString(n);
    int product = 1;
    boolean found