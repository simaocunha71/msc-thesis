const findClosestElements = (numbers) => {
    // Sort the array in ascending order
    numbers.sort((a, b) => a - b);

    // Initialize the variables to store the closest pair of numbers
    let closestPair = [];
    let diff = Infinity;

    // Iterate through the array
    for (let i = 0; i < numbers.length - 1; i++) {
        // Calculate the difference between the current number and the next number
        const currentDiff = Math.abs(numbers[i] - numbers[i + 1]);

        // If the current difference is less than the stored difference, update the stored difference and pair
        if (currentDiff < diff) {
            diff = currentDiff;
            closestPair = [numbers[i], numbers[i + 1]];
        }
    }

    // Return the closest pair of numbers
    return closestPair;
};
