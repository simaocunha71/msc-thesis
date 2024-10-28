  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  const range = max - min;

  return numbers.map((number) => (number - min) / range);
};

console.log(rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])); // [0, 0.25, 0.5, 0.75, 1]

// This function works by first finding the minimum and maximum of the input array. It then computes the range of the numbers (the difference between the max and min), and returns a new array where each number is transformed by subtracting the min and dividing by the range. This transforms the range of the numbers to be between 0 and 1.
// This is a common operation in machine learning and data science, where it's often useful to rescale data to have a known range.
// The spread operator (...) is used to pass the array elements as individual arguments to the Math.min and Math.max functions.
// The map method is used to create a new array where each element is a transformed version of the corresponding element in the original array.
// The result is an array where all numbers are between 0 and 1, representing the same data but rescaled.
// This function assumes that the input array contains only numbers. If the input array contains non-number elements, the function will throw a runtime error.
// In this case, the function will work correctly if the input array contains only numbers.
// If the input array contains non-number elements, you would need to add error checking code to handle this case.
// For example, you could modify the function to return an error message if the input array contains non-number elements, or you could modify the function to ignore non-number elements and only rescale the number elements.
// In general, it's a good idea to handle potential errors in your code to prevent runtime errors.
// This function does not mutate the original array. Instead, it creates a new array and returns that. If you want to modify the original array, you would need to assign the result to the original array.
// For example, numbers = rescaleToUnit(numbers);
// This function has a time