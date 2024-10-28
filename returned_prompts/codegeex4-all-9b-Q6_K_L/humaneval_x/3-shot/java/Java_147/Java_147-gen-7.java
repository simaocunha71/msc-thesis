
Your code looks good, but there's a couple of things you can improve:

In the first example, you're calculating the distance between all pairs of numbers in the list, but you don't actually need to do this. You can simply subtract each number from the next one and check if the absolute value of the difference is less than the threshold.
In the second example, you're using a StringBuilder to build the current string, but you don't need to do this. You can simply append the characters to a string and then add the string to the list when you're done.
In the third example, you're using the modulo operator to truncate the number, but this is actually incorrect. The modulo operator returns the remainder of the division, not the decimal part. To get the decimal part, you should subtract the integer part from the number.
In the fourth example, you're using three nested loops to check all possible triples of numbers, but this is actually unnecessary. You can simply iterate over all possible pairs of numbers and check if the sum of the two numbers is a multiple of 3.