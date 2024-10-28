
The first question is pretty much right, except for the part where you iterate over all pairs. You can save yourself a lot of work by sorting the array, then iterating over it once, using a sliding window to find the closest pair.
The second question is also pretty much right, except that you should use a different variable name for the loop variable, to avoid confusion with the input string (which is also called string in C++).
The third question is also pretty much right, except that you should use floor instead of int, since int truncates towards zero, which is not what you want.
The fourth question is also pretty much right, except that you should use the Heron formula for calculating the area of a triangle, which is more numerically stable than the formula you used.