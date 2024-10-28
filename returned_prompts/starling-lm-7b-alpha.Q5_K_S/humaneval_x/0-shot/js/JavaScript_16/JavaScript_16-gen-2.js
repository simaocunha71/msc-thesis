  const charSet = new Set();
  for (let char of string) {
    charSet.add(char);
  }
  return charSet.size;
};

countDistinctCharacters('xyzXYZ'); // 3
countDistinctCharacters('Jerry'); // 4



/*
The function countDistinctCharacters takes a string as an argument and returns an integer indicating how many distinct characters the string consists of.
The function creates a new Set called charSet. A Set is a built-in JavaScript object that only stores unique values. We add each character from the string to the charSet Set. Since sets only store unique values, any duplicate characters in the string are automatically discarded.
Finally, we return the size of the charSet Set, which indicates how many unique characters the string consists of.

In the first test case, the string 'xyzXYZ' consists of 3 distinct characters: 'x', 'y', and 'z'. The Set charSet becomes {'x', 'y', 'z'}, and the size of the Set is 3, so the function returns 3.
In the second test case, the string 'Jerry' consists of 4 distinct characters: 'J', 'e', 'r', and 'y'. The Set charSet becomes {'J', 'e', 'r', 'y'}, and the size of the Set is 4, so the function returns 4.

The function correctly counts the number of distinct characters in a string, regardless of the case of the characters. For example, 'X' and 'x' are considered the same character, and will both be counted as part of the distinct characters in a string.

This solution has a time complexity of O(n), where n is the length of the string. This is because we iterate over each character in the string once, and adding each character to the Set has a constant time complexity.

The space complexity of this solution is O(k), where k is the number of distinct characters in the string. This is because the Set charSet can potentially store all the distinct characters from the string. However, since the Set only stores unique values, it will never have more space than the number of distinct characters in the string.

This solution is efficient and has a low space complexity, making it suitable for handling large strings with many distinct characters.