  const letterCounts = {};
  const letters = test.split(' ');

  for (let letter of letters) {
    if (letterCounts[letter]) {
      letterCounts[letter]++;
    } else {
      letterCounts[letter] = 1;
    }
  }

  let maxCount = 0;
  for (let count of Object.values(letterCounts)) {
    if (count > maxCount) {
      maxCount = count;
    }
  }

  const result = {};
  for (let key of Object.keys(letterCounts)) {
    if (letterCounts[key] === maxCount) {
      result[key] = maxCount;
    }
  }
  
  return result;
};

console.log(histogram('a b c')) // ==> {a: 1, b: 1, c: 1}
console.log(histogram('a b b a')) // ==> {a: 2, b: 2}
console.log(histogram('a b c a b')) // ==> {a: 2, b: 2}
console.log(histogram('b b b b a')) // ==> {b: 4}
console.log(histogram('')) // ==> {}


The above function works by first splitting the input string into an array of letters. Then it goes through the array, incrementing the count of each letter in the letterCounts object. After that it goes through the counts to find the maximum count. Finally, it goes through the letterCounts object again, adding any letters with the maximum count to the result object.

*/





























































































































