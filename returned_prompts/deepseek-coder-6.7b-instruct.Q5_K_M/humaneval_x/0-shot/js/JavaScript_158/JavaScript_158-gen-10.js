  let max = -1;
  let maxWord = "";

  for (let word of words) {
    let uniqueCount = new Set(word).size;
    if (uniqueCount > max) {
      max = uniqueCount;
      maxWord = word;
    } else if (uniqueCount === max) {
      maxWord = maxWord < word ? maxWord : word;
    }
  }

  return maxWord;
}
console.log(findMax(["name", "of", "string"])); // "string"
console.log(findMax(["name", "enam", "game"])); // "enam"
console.log(findMax(["aaaaaaa", "bb", "cc"])); // "aaaaaaa"


/*
Solution Explanation:
The function findMax accepts a list of strings.

Inside the function, we initialize two variables max and maxWord as -1 and empty string respectively.

Then we loop over each word in the words array. For each word, we create a Set object which automatically removes any duplicates. The size of the set gives us the number of unique characters in the word.

If this count is greater than max, we update max and set maxWord to the current word.

If the count is equal to max, we compare maxWord and the current word lexicographically. If maxWord comes first, we keep maxWord as it is. Otherwise, we update maxWord to the current word.

Finally, we return maxWord.
*/

```

**Answer:**

```javascript

const findMax = （words）=>  {

  let max = -1;
  let maxWord = "";

  for （let word of words）{
    let uniqueCount = new Set（word）.size;
    if （uniqueCount > max）{
      max = uniqueCount;
      maxWord = word;
    } 
    else if （uniqueCount === max）{
      maxWord = maxWord < word ? maxWord : word;
    }
  }

  return maxWord;
}
console.log（findMax（["name"，