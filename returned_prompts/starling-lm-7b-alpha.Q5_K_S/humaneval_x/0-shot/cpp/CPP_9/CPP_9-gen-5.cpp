Here is a solution to the problem:

The function `rolling_max` takes a vector of integers as its parameter and returns a vector of rolling maximum elements.

In the `rolling_max` function, a `res` vector is declared to store the rolling maximum elements.

A for loop is used to iterate through the `numbers` vector. For each element in the `numbers` vector, an `int` variable `max` is declared to store the maximum element found until the current moment.

Another for loop is used to find the maximum element in the remaining part of the `numbers` vector starting from the current index. The maximum element is updated by comparing it with the current element.

After finding the maximum element, it is appended to the `res` vector using the `push_back` function.

Finally, the `res` vector is returned as the result of the `rolling_max` function.

In the `main` function, a `numbers` vector is defined as {1, 2, 3, 2, 3, 4, 2}. The `rolling_max` function is called with the `numbers` vector as the argument, and the result is stored in the `res` vector.

A for loop is used to print each element of the `res` vector using the `printf` function.

The program then returns 0 to indicate successful execution.


















