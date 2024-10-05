  let reversed = string.split('').reverse().join('');
  let palindromic_suffix = '';
  for (let i = 0; i < string.length; i++) {
    if (reversed.startsWith(string.substring(i))) {
      palindromic_suffix = string.substring(i);
      break;
    }
  }
  return string + reversed.substring(reversed.length - palindromic_suffix.length);
}
// Test
console.log(makePalindrome(''));
console.log(makePalindrome('cat'));
console.log(makePalindrome('cata'));  // 'catac'  // 1. 1.1
console.log(makePalindrome('abcdef'));  // 'abcdefba'  // 1.1
console.log(makePalindrome('abcb'));  // 'abcbba'  // 1.1
console.log(makePalindrome('abc'));  // 'abcba'  // 1.1
console.log(makePalindrome('a'));  // 'a'  // 1.1
console.log(makePalindrome(''));  // ''  // 1.1
console.log(makePalindrome('a'));  // 'a'  // 1.1
console.log(makePalindrome('aa'));  // 'aa'  // 1.1
console.log(makePalindrome('abc'));  // 'abcba'  // 1.1
console.log(makePalindrome('abcde'));  // 'abcdeba'  // 1.1
console.log(makePalindrome('abcdef'));  // 'abcdefba'  // 1.1
console.log(makePalindrome('abcdefg'));  // 'abcdefg gfedcba'  // 1.1
console.log(makePalindrome('abcdefgh'));  // 'abcdefgh hgfedcba'  // 1.1
console.log(makePalindrome('abcdefghi'));  // 'abcdefghi ihgfedcba'  // 1.1
console.log(makePalindrome('abcdefghij'));  // 'abcdefghi jhgfedcba'  // 1.1
console.log(makePalindrome('abcdefghijk'));  // 'abcdefghi jhgfedcba'  // 1.1
console.log(makePalindrome('abcdefghijkl'));  // 'abcdefghijkl lkjihgfedcba'  // 1.1
console.log(makePalindrome('abcdefghijklm'));  // 'abcdefghijklm lmjihgfedcba'  // 1.1
console.log(makePalindrome('abcdefghijklmn'));  // 'abcdefghijklm mn