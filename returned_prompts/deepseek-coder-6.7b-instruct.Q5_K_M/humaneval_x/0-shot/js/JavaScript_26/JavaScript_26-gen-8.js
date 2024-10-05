  let counts = {};
  let result = [];

  for (let num of numbers) {
    counts[num] = (counts[num] || 0) + 1;
  }

  for (let num of numbers) {
    if (counts[num] === 1) {
      result.push(num);
    }
  }

  return result;
}

console.log(removeDuplicates([1, 2, 3, 2, 4])); // [1, 3, 4]

*/

function removeDuplicates(numbers) {
  let counts = {};
  let result = [];

  for (let num of numbers) {
    counts[num] = (counts[num] || 0) + 1;
  }

  for (let num of numbers) {
    if (counts[num] === 1) {
      result.push(num);
    }
  }

  return result;
}

console.log(removeDuplicates([1, 2, 3, 2, 4])); // [1, 3, 4]

/*
