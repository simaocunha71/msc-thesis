  for(let i = 0; i < b.length; i++){
    if(a.includes(b)) return true;
    b = b.slice(1) + b[0];
  }
  return false;
}

console.log(cycpatternCheck("abcd","abd")); // false
console.log(cycpatternCheck("hello","ell")); // true
console.log(cycpatternCheck("whassup","psus")); // false
console.log(cycpatternCheck("abab","baa")); // true
console.log(cycpatternCheck("efef","eeff")); // false
console.log(cycpatternCheck("himenss","simen")); // true

//The function `cycpatternCheck` first checks if the second word b is a substring of the first word a. 
//If it is, it returns true. If it's not, it rotates the word b and checks again. 
//It continues this rotation until it has rotated the word b as many times as its length. 
//If no rotation of b is a substring of a, it returns false.

//The function `cycpatternCheck` uses the JavaScript string method `includes` to check if a string is a substring of another string, 
//and the `slice` method to rotate the string. This is accomplished by slicing the string from the second character to the end, 
//and then concatenating the first character to the end of this slice.

//The time complexity of the function `cycpatternCheck` is O(n*m), where n is the length of the first word a and m is the length of the second word b. 
//This is because for each rotation of the word b, it checks if it is a substring of a, which takes O(n) time. 
//Since there are m rotations of b, the total time complexity is O(n*m).

//The space complexity of the function `cycpatternCheck` is O(1), as it only uses a constant amount of space to store the words and the index. 
//This does not change with the size of the input words.

//In conclusion, the function `cycpatternCheck` is a linear time solution to the problem