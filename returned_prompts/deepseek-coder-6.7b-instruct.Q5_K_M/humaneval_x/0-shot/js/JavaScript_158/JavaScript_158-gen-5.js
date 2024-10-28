  let maxWord = '';
  let maxCount = 0;

  for (let word of words) {
    const uniqueCount = new Set(word).size;
    if (uniqueCount > maxCount) {
      maxCount = uniqueCount;
      maxWord = word;
    } else if (uniqueCount === maxCount) {
      maxWord = maxWord < word ? maxWord : word;
    }
  }

  return maxWord;
};
console.log(findMax(["name", "of", "string"])); // "string"
console.log(findMax(["name", "enam", "game"])); // "enam"
console.log(findMax(["aaaaaaa", "bb", "cc"])); // "aaaaaaa"

//Explanation:
//In the first case, "string" has maximum unique characters i.e 6 and it is the first word in the given list.
//In the second case, "enam" has maximum unique characters i.e 4 and it is the first word in the given list which appears first in lexicographical order.
//In the third case, all words have same number of unique characters i.e 1, so we return the one which comes first in lexicographical order.
//The word "aaaaaaa" comes first in lexicographical order.

//Note: 
//The function uses a Set to count the number of unique characters in each word.
//It then compares the size of the set to the maximum count found so far.
//If the set is larger, it updates the maximum count and the maximum word.
//If the set is the same size as the maximum count, it compares the word to the maximum word and updates if the word comes first in lexicographical order.
//Finally, it returns the maximum word.

//Time complexity: O(n*m) where n is the number of words and m is the length of the longest word.
//Space complexity: O(1) as it uses a constant amount of space.
//Note: The space complexity of the Set is not considered in this case as it depends on the number of unique characters in the words.
//In the worst case, it can be O(m), where m is the length of the longest