let stringSet = new Set(string.toLowerCase());

  return stringSet.size;

};

console.log(countDistinctCharacters('xyzXYZ'));
console.log(countDistinctCharacters('Jerry'));

Explanation:
In the code above, a Set is created from the input string. In JavaScript, a Set is a collection of unique items. That means that if the same character appears more than once in the string, it will only count it as one instance of that character in the Set. 

The .toLowerCase() method is used to ensure the function is case-insensitive.

Then, the size property of the Set is returned, which gives the number of unique characters in the string.

In the first example, 'xyzXYZ' has 3 distinct characters (after converting all to lower case): 'x', 'y' and 'z'. In the second example, 'Jerry' has 4 distinct characters: 'j', 'e', 'r' and 'y'.


*/

// 