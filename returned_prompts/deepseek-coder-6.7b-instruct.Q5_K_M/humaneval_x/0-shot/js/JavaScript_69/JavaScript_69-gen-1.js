  let max = -1;
  const counts = {};

  // 计算数字出现的次数
  for (let num of lst) {
      counts[num] = (counts[num] || 0) + 1;
  }

  // 如果出现次数大于或等于数字本身，则更新max
  for (let num in counts) {
      if (counts[num] >= num && num > max) {
          max = num;
      }
  }

  return max;
}

console.log(search([4, 1, 2, 2, 3, 1])); // 2
console.log(search([1, 2, 2, 3, 3, 3, 4, 4, 4])); // 3
console.log(search([5, 5, 4, 4, 4])); // -1

*/

/*
This function works by first creating an object to hold the count of each number in the list. 
Then it iterates over the counts, and if the count of a number is greater than or equal to the number itself, 
and greater than the current max, it updates max. The final max is then returned.
*/

/*
This solution has a time complexity of O(n), where n is the length of the input list, 
since it iterates over the list twice: once to count the numbers, and once to find the maximum. 
The space complexity is also O(n), because of the counts object.
*/

/*
The function is correct because it correctly identifies the greatest number that occurs more than 
itself number of times. It returns -1 if no such number exists.
*/

/*
Examples:

search([4, 1, 2, 2, 3, 1]) 
The counts are { '4': 1, '1': 2, '2': 2, '3': 1 }. 2 appears twice, which is greater than 2, and 3 appears once,
which is greater than 3, but 4 appears once, which is greater than 4. 2 and 3 are the only numbers that 
satisfy the condition