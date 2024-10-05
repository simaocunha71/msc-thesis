  const lowerCaseString = string.toLowerCase();
  const uniqueCharacters = new Set(lowerCaseString);
  const count = uniqueCharacters.size;
  return count;
};

console.log(countDistinctCharacters('xyzXYZ'));
console.log(countDistinctCharacters('Jerry'));

// The Set object lets you store unique values of any type. It is a collection of values, where each value may occur only once.
// size property returns the number of elements in the set object.
```

In this code, we first convert the string to lowercase. Then, we create a new Set object with the characters from the string. Sets automatically remove any duplicate values, so we're left with a set of unique characters. Finally, we return the size of the set, which is the number of unique characters.

So, if you run this code with the string 'xyzXYZ', it will return 3 because there are 3 unique characters ('x', 'y', 'z'). If you run it with the string 'Jerry', it will return 4 because there are 4 unique characters ('j', 'e', 'r', 'y').

This code runs in O(n) time, where n is the length of the string. This is because we loop through the string once to add its characters to the set, and then we loop through the set once to count its size. So the total number of operations is proportional to the size of the string.

And also this code is pretty straightforward and easy to understand. It uses JavaScript's built-in Set object and the size property to count the number of unique characters in the string.

That's the solution you're looking for.
*/

const countDistinctCharacters = (string) => {
  const lowerCaseString = string.toLowerCase();
  const uniqueCharacters = new Set(lowerCaseString);
  const count = uniqueCharacters.size;
  return count;
};

console.log(countDistinctCharacters('xyzXYZ')); // 3
console.log(countDistinctCharacters('Jerry'));  // 4
```






























