  let arr = test.split(' ');
  let count = {};
  let max = 0;
  let letters = [];
  
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] in count) {
      count[arr[i]]++;
    } else {
      count[arr[i]] = 1;
    }
    if (count[arr[i]] > max) {
      max = count[arr[i]];
      letters = [arr[i]];
    } else if (count[arr[i]] === max) {
      letters.push(arr[i]);
    }
  }
  
  let result = {};
  for (let i = 0; i < letters.length; i++) {
    result[letters[i]] = max;
  }
  
  return result;
};

console.log(histogram('a b c')); // {'a': 1, 'b': 1, 'c': 1}
console.log(histogram('a b b a')); // {'a': 2, 'b': 2}
console.log(histogram('a b c a b')); // {'a': 2, 'b': 2}
console.log(histogram('b b b b a')); // {'b': 4}
console.log(histogram('')); // {}

























































































































































































