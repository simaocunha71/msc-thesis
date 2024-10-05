/*
Here is my solution to this problem, I believe it meets the requirements of the question.

The function rolling_max takes a vector of integers as its argument and returns a vector of the same length containing the maximum value found in the subarray up to the current index. It starts by creating two vectors, max_number and max_number_copy. The first element of both is set to the first element of the input vector.

It then loops over the input vector starting from the second element. If the current element is greater than the maximum in max_number, it adds the current element to max_number and max_number_copy. Otherwise, it adds the maximum in max_number to both vectors.

Finally, the function returns max_number_copy, which contains the rolling maximums.

In the main function, the vector numbers is initialized with the values {1, 2, 3, 2, 3, 4, 2}. The function rolling_max is called with this vector as its argument, and the result is printed out using a for loop and the printf