  let str = '';
  for(let i = 0; i < s.length; i++){
    if(!c.includes(s[i])) str += s[i];
  }
  let revStr = str.split('').reverse().join('');
  return [revStr, revStr === str];
};

console.log(reverseDelete('abcde', 'ae')); //  ('bcd',false)
console.log(reverseDelete('abcdef', 'b')); //  ('acdef',false)
console.log(reverseDelete('abcdedcba', 'ab')); //  ('cdedc',true)



```

---
## 2. Write a JavaScript function to get the list of elements with duplicate numbers in a given array.

