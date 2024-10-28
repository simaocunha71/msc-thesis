/*
This program takes in a vector of integers and generates a vector of rolling maximum element found until
given moment in the sequence.

It first initializes an empty vector to store the result. It then initializes a variable max to store the maximum
value found until the given moment. It sets the initial value of max to the first element in the input vector.

Next, it enters a for loop that starts at index 1 and goes until the end of the input vector. In each iteration, it
compares the current element to the value of max. If the current element is greater than max, it updates max to the
current element. Otherwise, it leaves max unchanged. After making this comparison, it appends the value of max to
the result vector.

Finally, it returns the result vector.

In the main function, it creates a vector a with the values {1, 2, 3, 2, 3, 4, 2}. It then calls the rolling_max function
with this vector and stores the result in a vector b. It then prints each element in b using a for loop and a printf statement.

The output of the program is: 1 2 3 3 3 4 4

This means that the rolling maximum element found until each given moment in the sequence is 1, 2, 3, 3, 3, 4, and 4.
*/
















