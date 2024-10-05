  let maxUniqueChars = 0;
  let maxWord = '';

  for(let word of words) {
    let uniqueChars = new Set(word.split('')).size;
    if(uniqueChars > maxUniqueChars) {
      maxUniqueChars = uniqueChars;
      maxWord = word;
    } else if(uniqueChars === maxUniqueChars) {
      maxWord = maxWord < word ? maxWord : word;
    }
  }

  return maxWord;
};

console.log(findMax(["name", "of", "string"])); // "string"
console.log(findMax(["name", "enam", "game"])); // "enam"
console.log(findMax(["aaaaaaa", "bb" ,"cc"])); // "aaaaaaa"
console.log(findMax(["hello", "world", "javascript", "java", "python"])); // "javascript"

```

Explanation:
First, we initialize two variables, maxUniqueChars and maxWord, to keep track of the word with the maximum number of unique characters and the word itself respectively.

Next, we loop through each word in the input array. For each word, we split it into characters and create a new Set from the resulting array. The size of the Set gives us the number of unique characters in the word.

We then compare this number with maxUniqueChars. If it is greater, we update maxUniqueChars and maxWord. If it is equal, we check which word comes first in lexicographical order and assign it to maxWord.

Finally, we return maxWord, which will be the word with the maximum number of unique characters. If there are multiple such words, the one that comes first lexicographically will be returned.
*/
```

### Code 2:

```javascript
