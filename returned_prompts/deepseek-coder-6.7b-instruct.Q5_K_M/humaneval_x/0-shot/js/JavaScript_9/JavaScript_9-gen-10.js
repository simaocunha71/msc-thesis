  let result = [];
  let max = numbers[0];

  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    result.push(max);
  }

  return result;
};

console.log(rollingMax([1, 2, 3, 2, 3, 4, 2])); // [1, 2, 3, 3, 3, 4, 4]



//This solution uses a single pass approach and only one for loop. The time complexity is O(n) and space complexity is O(n) as well. 
//It starts by initializing an array 'result' and a variable 'max' with the first element of the input array. 
//Then it iterates over the input array, if the current number is greater than 'max', it updates 'max'. After that it adds 'max' to the 'result' array. Finally, it returns the 'result' array.

//It will work by always keeping track of the maximum number seen so far, and pushing that maximum onto the result array each time.

//This solution is efficient and will work well for large inputs.

//I hope this helps explain how the solution works. Let me know if you have any further questions.


//Solution Explanation:

//The solution works by iterating through the input array and maintaining the maximum value seen so far. It updates the maximum whenever it encounters a larger number, and then adds the maximum to the result array.

//The time complexity of the solution is O(n), where n is the length of the input array, because it needs to iterate through the entire array once.

//The space complexity is also O(n), because the solution creates a new array that is the same length as the input array.

//This solution is efficient and should work well for large inputs.

//If you have any further questions, feel free to ask.

//Best of luck with your coding challenge.







































