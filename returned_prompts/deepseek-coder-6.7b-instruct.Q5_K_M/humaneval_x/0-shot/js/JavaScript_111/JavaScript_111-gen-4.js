  const count = {};
  const words = test.split(' ');

  for(let word of words) {
    if(word in count) {
      count[word] += 1;
    } else {
      count[word] = 1;
    }
  }

  let max = Math.max(...Object.values(count));
  let result = {};

  for(let word in count) {
    if(count[word] === max) {
      result[word] = max;
    }
  }

  return result;
}

console.log(histogram('a b c')); // {'a': 1, 'b': 1, 'c': 1}
console.log(histogram('a b b a')); // {'a': 2, 'b': 2}
console.log(histogram('a b c a b')); // {'a': 2, 'b': 2}
console.log(histogram('b b b b a')); // {'b': 4}
console.log(histogram('')); // {}

module.exports = histogram;

//histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
//histogram('a b b a') == {'a': 2, 'b': 2}
//histogram('a b c a b') == {'a': 2, 'b': 2}
//histogram('b b b b a') == {'b': 4}
//histogram('') == {}

/*
This program creates a histogram of the letters in a given string. It first counts the occurrence of each letter, then determines the maximum occurrence. Finally, it returns a dictionary containing only the letters that have the maximum occurrence.
*/
```



## Answer 2
```javascript
