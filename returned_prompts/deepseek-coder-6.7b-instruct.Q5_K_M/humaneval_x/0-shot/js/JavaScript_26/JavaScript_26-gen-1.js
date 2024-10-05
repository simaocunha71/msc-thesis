let count = {};
  let result = [];

  for (let i = 0; i < numbers.length; i++) {
    if (!count[numbers[i]]) {
      count[numbers[i]] = true;
      result.push(numbers[i]);
    }
  }

  return result;
}

console.log(removeDuplicates([1, 2, 3, 2, 4]));

Output:
[1, 2, 3, 4]

In this code, we are maintaining a count of each number in the input array. If a number is not in the count object, we add it and push it to the result array. The result array will contain only unique numbers in the same order as they appeared in the input array.
*/

/*
