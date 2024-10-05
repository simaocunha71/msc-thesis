
You have a few good things going on here:

You're using List<Double> instead of double[] which is nice.
You're using a StringBuilder, which is nice.

There are a few issues here:

You're using double as the return type of your function, but the question asks for a boolean. This is a small issue, but it's worth noting.
You're using the Math.abs function, which is fine, but you don't need to. The distance between two numbers is the absolute difference between them. So, you could simply use numbers.get(i) - numbers.get(j) instead of Math.abs(numbers.get(i) - numbers.get(j)).
Your for loop is a bit confusing. You're using i and j as loop variables, which is fine, but it's a bit unconventional. I'd prefer to use something like left and right instead.
You're using a magic number 0.5 as the threshold. It would be better to use a named constant, like double THRESHOLD = 0.5, so that it's clear what the threshold is.
Your code is a bit long and complex. It would be better to break it down into smaller functions. For example, you could have a function that calculates the distance between two numbers, and a function that checks if the distance is less than the threshold.
Your code is not very readable. You should add comments to explain what each part of the code does.
Your code is not very efficient. You're using a nested loop, which has a time complexity of O(n^2). This is fine for small values of n, but it's not efficient for large values of n. You could use a different algorithm that has a better time complexity, like sorting the list and then checking adjacent elements.

Here's a revised version of your code:
import java.util.*;

class Solution {
    /**
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    >>> hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5)
    false
    >>> hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 