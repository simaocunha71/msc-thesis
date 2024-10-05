        int product = 1;
        boolean found = false;

        while(n > 0){
            int digit = n % 10;
            if(digit % 2 != 0){
                product *= digit;
                found = true;
            }
            n /= 10;
        }

        return found ? product : 0;
    }
}

Here, the problem is solved by iterating through each digit of the integer, checking if the digit is odd, and if so, multiplying the product by that digit. If no odd digits are found, the function returns 0.

I have used the modulo operator (%) to get the last digit of the integer, and the integer division operator (/) to remove the last digit from the integer.

The variable "found" is used to check if any odd digits were found in the integer. If no odd digits were found, the function returns 0. If odd digits were found, the function returns the product of the odd digits.

This solution has a time complexity of O(d), where d is the number of digits in n. It also has a space complexity of O(1), as it only uses a constant amount of space to store the product and a boolean flag.

This solution assumes that the input integer n is positive. If the input could be negative, the solution would need to be modified to handle this case.

This solution also assumes that the input integer n is a positive integer. If the input could be a floating-point number or a string, the solution would need to be modified to handle this case.

This solution does not handle the case where the integer n is larger than the maximum integer that can be represented in Java. If the integer n is larger than the maximum integer, the solution would need to be modified to handle this case.

This solution does not handle the case where the