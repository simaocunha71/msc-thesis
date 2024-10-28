Here is the solution for your problem.

We firstly find the min and max values of the input list using the built-in Math.min and Math.max methods respectively. We then calculate the range of the values.

Then, we use the Array.map method to transform each element of the input list to a new value. For each element, we subtract the min value from it and then divide the result by the range. This rescales the values such that the smallest value becomes 0 and the largest value becomes 1.

Finally, we return the new list.

This solution assumes that the input list is not empty and that it contains at least two elements.

In the given example, the input list [1.0, 2.0, 3.0, 4.0, 5.0] is transformed to [0.0, 0.25, 0.5, 0.75, 1.0].

This is because the min value is 1.0 and the max value is 5.0, the range is 4.0. So each element is rescaled as (element - 1.0) / 4.0.

The rescaled values are then [(1.0 - 1.0) / 4.0 = 0.0, (2.0 - 1.0) / 4.0 = 0.25, (3.0 - 1.0) / 4.0 = 0.5, (4.0 - 1.0) / 4.0 = 0.75, (5.0 - 1.0) / 4.0 = 1.0].

So the function rescaleToUnit returns the correct rescaled list [0.0, 0.25, 0.5, 0.75, 1