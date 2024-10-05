  let reversed = '';
  for(let i = 0; i < s.length; i++){
    if(s[i].toLowerCase() !== s[i].toUpperCase()){
      reversed += (s[i] === s[i].toUpperCase()) ? s[i].toLowerCase() : s[i].toUpperCase();
    } else {
      reversed += s[i];
    }
  }
  return reversed;
}

console.log(solve("1234")); // "4321"
console.log(solve("ab")); // "AB"
console.log(solve("#a@C")); // "#A@c"

// Solution 2
const solve2 = s => {
  let reversed = '';
  for(let i = 0; i < s.length; i++){
    reversed += (s[i] === s[i].toUpperCase()) ? s[i].toLowerCase() : s[i].toUpperCase();
  }
  return reversed;
}

console.log(solve2("1234")); // "4321"
console.log(solve2("ab")); // "AB"
console.log(solve2("#a@C")); // "#A@c"

// Solution 3
const solve3 = s => [...s].map(el => el === el.toLowerCase() ? el.toUpperCase() : el.toLowerCase()).join('');

console.log(solve3("1234")); // "4321"
console.log(solve3("ab")); // "AB"
console.log(solve3("#a@C")); // "#A@c"
```

## 🌟 Q3. Is Palindrome?
```javascript
