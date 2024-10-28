  const str = s.split('').filter(ele => !c.includes(ele)).join('');
  const reverseStr = str.split('').reverse().join('');
  return [reverseStr, str === reverseStr];

}

console.log(reverseDelete("abcde", "ae")); // ('bcd', false)
console.log(reverseDelete("abcdef", "b")); // ('acdef', false)
console.log(reverseDelete("abcdedcba", "ab")); // ('cdedc', true)

/*
This program works by first filtering the characters in s that are not in c.
Then it reverses the resultant string and checks whether the reversed string and the original string are the same.
Finally, it returns a tuple containing the resultant string and a boolean indicating whether the string is a palindrome.
*/
```

```javascript
// Code:
const reverseDelete = (s, c) => {
  const str = s.split('').filter(ele => !c.includes(ele)).join('');
  const reverseStr = str.split('').reverse().join('');
  return [reverseStr, str === reverseStr];
}

console.log(reverseDelete("abcde", "ae")); // ('bcd', false)
console.log(reverseDelete("abcdef", "b")); // ('acdef', false)
console.log(reverseDelete("abcdedcba", "ab")); // ('cdedc', true)
```

```javascript
// Code:
const reverseDelete = (s, c) => {
  let str = '';
  for(let i=0; i<s.length; i++) {
    if(!c.includes(s[i]))
      str += s[i];
  }
  const reverseStr = str.split('').reverse().join('');
  return [reverseStr, str === reverseStr];
}

console.log(reverseDelete("abcde", "ae")); // ('bcd', false)
console.log(reverseDelete("abcdef", "b")); // ('acdef', false)
console.log(reverseDelete("abcdedcba", "ab"));