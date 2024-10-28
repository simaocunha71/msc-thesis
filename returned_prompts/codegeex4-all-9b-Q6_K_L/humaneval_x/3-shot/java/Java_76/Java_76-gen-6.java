
Your code is correct and looks good.
A few minor suggestions:

Use a try-catch block to handle the case when the logarithm of the base is zero:
    return Math.pow(y, (int) Math.log(x) / (int) Math.log(n)) == x;

This will throw an ArithmeticException if the logarithm of the base is zero. You can catch this exception and return false in that case.

You can simplify your code by using the Math.log10() function instead of Math.log(). This will make your code more readable and easier to understand:
    return Math.pow(y, (int) Math.log10(x) / (int) Math.log10(n)) == x;

Also, you don't need to cast the result of Math.log10(x) and Math.log10(n) to int. You can simply use the int division operator (/) to get the integer part of the result:
    return Math.pow(y, Math.log10(x) / Math.log10(n)) == x;

This will make your code more concise and easier to read.