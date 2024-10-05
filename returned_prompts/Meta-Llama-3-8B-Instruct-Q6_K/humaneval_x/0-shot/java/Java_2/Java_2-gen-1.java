        int intPart = (int) Math.floor(number);
        return number - intPart;
    }
}

Explanation:
In this code, we are using the Math.floor() function which returns the largest integer smaller than or equal to the given number.
We then subtract this integer part from the original number to get the decimal part.

For example, if the input number is 3.5, the integer part is 3 and the decimal part is 0.5. So, the function returns 0.5.

This function will work correctly for any positive floating point number.