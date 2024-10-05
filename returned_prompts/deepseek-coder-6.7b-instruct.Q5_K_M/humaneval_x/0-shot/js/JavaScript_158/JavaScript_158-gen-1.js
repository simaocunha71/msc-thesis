
  let maxUniqueChars = 0;
  let maxWord = '';

  words.forEach((word) => {
    let uniqueChars = new Set(word.split('')).size;
    if (uniqueChars > maxUniqueChars) {
      maxUniqueChars = uniqueChars;
      maxWord = word;
    } else if (uniqueChars === maxUniqueChars) {
      maxWord = word < maxWord ? word : maxWord;
    }
  });

  return maxWord;
};

console.log(findMax(["name", "of", "string"]));
console.log(findMax(["name", "enam", "game"]));
console.log(findMax(["aaaaaaa", "bb" ,"cc"]));

```

Output:
```
string
enam
aaaaaaa
```

Explanation:
The function findMax takes a list of words as input. It initializes two variables, maxUniqueChars and maxWord, to keep track of the word with the most unique characters and the word itself. It iterates over the words in the list, for each word it splits the word into an array of characters and uses the Set object to remove duplicates. The size of the Set gives the number of unique characters. If the number of unique characters is greater than maxUniqueChars, it updates maxUniqueChars and maxWord. If the number of unique characters is equal to maxUniqueChars, it compares the current word and maxWord lexicographically and updates maxWord if the current word comes first. Finally, it returns maxWord.

The time complexity of this solution is O(n*m), where n is the number of words and m is the length of the longest word. This is because for each word, we are splitting it into an array of characters and creating a Set, both of which are linear operations in terms of the number of characters in the word. The space complexity is O(n*m), again because of the space required to store the words as arrays and the Set objects.
```






































