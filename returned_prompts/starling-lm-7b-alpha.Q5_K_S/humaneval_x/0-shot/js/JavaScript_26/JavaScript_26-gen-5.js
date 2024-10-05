const removeDuplicates = (numbers) => {
    const newArray = [];
    for (let i = 0; i < numbers.length; i++) {
        if (newArray.indexOf(numbers[i]) === -1) {
            newArray.push(numbers[i]);
        }
    }
    return newArray;
};

// test
console.log(removeDuplicates([1, 2, 3, 2, 4])); // [1, 3, 4]



In the above code, we define a function called removeDuplicates that takes in an array called numbers. We create a new array called newArray. We then use a for loop to iterate over the numbers array. Inside the loop, we use the indexOf() method to check if the current number is already in the newArray. If the indexOf() method returns -1, it means the number is not in the newArray, so we push it to the newArray using the push() method. Finally, we return the newArray.

To test the function, we use console.log() to print the result of calling the removeDuplicates() function with an example array [1, 2, 3, 2, 4]. The output should be [1, 3, 4], as all the duplicate elements have been removed while maintaining the order of the remaining elements.


In the above code, we define a function called removeDuplicates that takes in an array called numbers. We create a new array called newArray. We then use a for loop to iterate over the numbers array. Inside the loop, we use the indexOf() method to check if the current number is already in the newArray. If the indexOf() method returns -1, it means the number is not in the newArray, so we push it to the newArray using the push() method. Finally, we return the newArray.

To test the function, we use console.log() to print the result of calling the removeDuplicates() function with an example array [1, 2, 3, 2, 4]. The output should be [1, 3, 4], as all the duplicate elements have been removed while maintaining the order of the remaining elements.


In the above code, we define