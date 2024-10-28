  let count = 0
  let lowerCaseString = string.toLowerCase()
  let distinctCharacters = []
  
  for (let i = 0; i < lowerCaseString.length; i++) {
    if (!distinctCharacters.includes(lowerCaseString[i])) {
      distinctCharacters.push(lowerCaseString[i])
      count++
    }
  }
  return count
}

console.log(countDistinctCharacters('xyzXYZ')) // 3
console.log(countDistinctCharacters('Jerry')) // 4

```

In this code, we first convert the string to lower case to make the function case insensitive. We then create a loop that iterates over each character in the string. If the character is not already in the array distinctCharacters, we add it to the array and increment the count. At the end, we return the count.
*/

function countDistinctCharacters(string) {
  let count = 0
  let lowerCaseString = string.toLowerCase()
  let distinctCharacters = []
  
  for (let i = 0; i < lowerCaseString.length; i++) {
    if (!distinctCharacters.includes(lowerCaseString[i])) {
      distinctCharacters.push(lowerCaseString[i])
      count++
    }
  }
  return count
}

console.log(countDistinctCharacters('xyzXYZ')) // 3
console.log(countDistinctCharacters('Jerry')) // 4
```

This code will work for any string input provided.

*/










































































































































