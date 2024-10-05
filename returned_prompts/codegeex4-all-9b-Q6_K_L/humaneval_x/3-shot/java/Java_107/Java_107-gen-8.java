
hasCloseElements
Your for loops can be combined into a single loop as the second loop is just an increment of the first loop's index by 1.
    for (int i = 0; i < numbers.size() - 1; i++) {
        double distance = Math.abs(numbers.get(i) - numbers.get(i + 1));
        if (distance < threshold) return true;
    }
    return false;

separateParenGroups
This solution looks good. You could use a Stack to keep track of the parentheses to make it more readable, but it would be more complex and probably not necessary.
truncateNumber
You could use Math.floor() instead of using % 1.0. Also, you should check if the number is not an integer before returning the result.
    if (number == (int) number) {
        return 0;
    }
    return number - (int) number;

evenOddPalindrome
This looks good. I would use String.valueOf(number) instead of Integer.toString(number) as the former is more efficient. Also, you could use a StringBuilder instead of a String to build the reversed number.

