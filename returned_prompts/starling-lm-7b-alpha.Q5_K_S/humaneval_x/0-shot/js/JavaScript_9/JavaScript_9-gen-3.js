    let max = [];
    let windowMax = [];
    let i = 0;

    while (i < numbers.length) {
        windowMax.push(numbers[i]);
        max.push(Math.max(...windowMax));
        i++;
    }

    return max;
};

rollingMax([1, 2, 3, 2, 3, 4, 2]); // [1, 2, 3, 3, 3, 4, 4]






/*
From a given list of integers, generate a list of rolling maximum element found until given moment
in the sequence.

Ex:

>>> rollingMax([1, 2, 3, 2, 3, 4, 2])
[1, 2, 3, 3, 3, 4, 4]

To solve this problem, we can use the following steps:

1. Initialize an empty array max to store the rolling maximums.
2. Initialize an empty array windowMax to store the current window of numbers.
3. Initialize a variable i to keep track of the index of the current number we are examining.
4. While i is less than the length of the input array:
   a. Add the current number to the windowMax array.
   b. Update the max array by adding the maximum value in the windowMax array.
   c. Increment i.
5. Return the max array.

With these steps, we can generate a list of rolling maximums for the given input array.

In the provided code, we define the rollingMax function that takes an array of numbers as input. Inside the function, we initialize the max and windowMax arrays, as well as the variable i. Then, we enter a while loop that runs as long as i is less than the length of the input array.

Inside the loop, we add the current number to the windowMax array using the push method. Then, we update the max array by finding the maximum value in the windowMax array using the spread operator (...) and the Math.max function. Finally, we increment i.

After the loop finishes, we return the max array, which contains the rolling maximums for the input array.

When we call