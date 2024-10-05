  let counter = {};
  
  for (let num of lst) {
    counter[num] = (counter[num] || 0) + 1;
  }
  
  let max = -1;
  
  for (let num in counter) {
    if (num > max && counter[num] >= num) {
      max = num;
    }
  }
  
  return max;
}

console.log(search([4, 1, 2, 2, 3, 1])); // 2
console.log(search([1, 2, 2, 3, 3, 3, 4, 4, 4])); // 3
console.log(search([5, 5, 4, 4, 4])); // -1
console.log(search([1, 2, 3, 3, 3])); // 3
console.log(search([3, 3, 3, 3, 2])); // 3
console.log(search([2, 2, 2, 2, 2])); // 2
console.log(search([1, 2, 3, 4, 5])); // -1
console.log(search([5, 5, 5, 5, 5])); // 5
console.log(search([1, 1, 2, 2, 2])); // 2
console.log(search([5, 5, 5, 5, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3])); // 5


*/

/*
  The question is asking for a number that is greater than zero and appears in the array at least as many times as the number itself. 
  The function first creates a dictionary/hashmap/object where the keys are the numbers in the array and the values are the counts of each number. 
  Then it iterates over the keys (numbers) in the dictionary. If a number is greater than the max and its count is at least as large as the number itself, it updates max.