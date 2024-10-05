
To solve this problem we have to find the maximum element in a given vector. The maximum element in a vector is the element that is greater than all other elements in the vector. We can find the maximum element in a vector by iterating through the vector and comparing each element with all other elements in the vector until we find the maximum element.

Here is a step-by-step solution to the problem:

1. Create a function called `max_element` that takes a vector of floats as an input and returns a float.

2. Inside the `max_element` function, create two integer variables `i` and `j` and initialize them to 0. These variables will be used to keep track of the indices of the elements in the vector.

3. Create a while loop that runs as long as `i` is less than the size of the vector. This loop will iterate through the vector and compare each element with all other elements in the vector.

4. Inside the while loop, create another while loop that runs as long as `j` is less than the size of the vector. This loop will compare the element at index `i` with the elements at indices `i + 1` to the end of the vector.

5. Inside the inner while loop, check if the element at index `j` is greater than the element at index `i`. If it is, update the value of `i` to `j