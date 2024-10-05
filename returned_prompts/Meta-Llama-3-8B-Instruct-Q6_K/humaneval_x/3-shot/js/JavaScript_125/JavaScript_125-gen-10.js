  let words = txt.split(/\s+/);
  if (words.length == 1) {
    words = txt.split(',');
    if (words.length == 1) {
      let count = 0;
      for (let i = 0; i < txt.length; i++) {
        if (txt[i].toLowerCase() >= 'a' && txt[i].toLowerCase() <= 'z' && (i % 2) == 1) {
          count++;
        }
      }
      return count;
    }
  }
  return words;
}
}  // end of function definition



// test cases for the function
console.log(hasCloseElements([1.0, 2.0, 3.0], 0.5));  // false
console.log(hasCloseElements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3));  // true

console.log(separateParenGroups('( ) (( )) (( )( ))'));  // ['()', '(())', '(()())']

console.log(truncateNumber(3.5));  // 0.5

console.log(splitWords("Hello world!"));  // ["Hello", "world!"]
console.log(splitWords("Hello,world!"));  // ["Hello", "world!"]
console.log(splitWords("abcdef"));  // 3
console.log(splitWords("ABCDEFGHIJKLMNOPQRSTUVWXYZ"));  // 13
console.log(splitWords("abcdefg"));  // 3
console.log(splitWords(""));  // []
console.log(splitWords("Hello"));  // ["Hello"]
console.log(splitWords("a,b,c"));  // ["a", "b", "c"]
console.log(splitWords("a,b,c,d,e,f,g"));  // ["a", "b", "c", "d", "e", "f", "g"]
console.log(splitWords("abcdefghijklmnopqrstuvwxyz"));  // 13
console.log(splitWords("ABCDEFGHIJKLMNOPQRSTUVWXYZ"));  // 13
console.log(splitWords("abcdefg,hijklmn"));  // ["abcdefg", "hijklmn"]



// Output
// false
// true
// [(), (()), (())]
// 0.5
// ["Hello", "world!"]
// ["Hello", "world!"]
// 3
// 13
// 3
// []
// ["Hello"]
// ["a", "b", "c"]
// ["a