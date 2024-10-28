  let result = s.split('').filter(e => !c.includes(e)).join('');
  let isPalindrome = result === result.split('').reverse().join('');
  return [result, isPalindrome];
}

console.log(reverseDelete("abcde", "ae")); // ['bcd', false]
console.log(reverseDelete("abcdef", "b")); // ['acdef', false]
console.log(reverseDelete("abcdedcba", "ab")); // ['cdedc', true]

*/

// Q2:
/*
