  if(strings.length === 0){
    return null;
  }

  let longestString = strings[0];

  for(let i = 1; i < strings.length; i++){
    if(strings[i].length > longestString.length){
      longestString = strings[i];
    }
  }
  return longestString;
}

console.log(longest([])); // null
console.log(longest(['a', 'b', 'c'])); // 'a'
console.log(longest(['a', 'bb', 'ccc'])); // 'ccc'
console.log(longest(['hello', 'hi', 'hola'])); // 'hello'
console.log(longest(['one', 'two', 'three'])); // 'one'
console.log(longest(['short', 'longer', 'longest'])); // 'longest'

*/

// Write a function that accepts a list of strings and returns a new list containing only the strings that start with a vowel.

