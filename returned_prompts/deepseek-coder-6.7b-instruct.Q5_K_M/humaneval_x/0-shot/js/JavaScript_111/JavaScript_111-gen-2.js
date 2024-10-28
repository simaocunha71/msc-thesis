  let words = test.split(' ');
  let count = {};
  let max = 0;
  let letter = '';

  for (let word of words) {
    if (count[word] === undefined) {
      count[word] = 1;
    } else {
      count[word] += 1;
    }

    if (count[word] > max) {
      max = count[word];
      letter = word;
    }
  }

  return { [letter]: max };
}

console.log(histogram('a b c')); // {'a': 1, 'b': 1, 'c': 1}
console.log(histogram('a b b a')); // {'a': 2, 'b': 2}
console.log(histogram('a b c a b')); // {'a': 2, 'b': 2}
console.log(histogram('b b b b a')); // {'b': 4}
console.log(histogram('')); // {}


A: 
  let words = test.split(' ');
  let count = {};
  let max = 0;
  let letter = '';

  for (let word of words) {
    if (count[word] === undefined) {
      count[word] = 1;
    } else {
      count[word] += 1;
    }

    if (count[word] > max) {
      max = count[word];
      letter = word;
    }
  }

  return { [letter]: max };
}

console.log(histogram('a b c')); // {'a': 1, 'b': 1, 'c': 1}
console.log(histogram('a b b a')); // {'a': 2, 'b': 2}
console.log(histogram('a b c a b')); // {'a': 2, 'b': 2}
console.log(histogram('b b b b a')); // {'b': 4}
console.log(histogram('')); // {}


A: 
  let words = test.split(' ');
  let count = {};
 