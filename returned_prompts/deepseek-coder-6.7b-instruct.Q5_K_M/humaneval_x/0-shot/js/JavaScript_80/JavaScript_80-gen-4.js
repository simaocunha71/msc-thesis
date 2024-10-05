  if(s.length < 3){
    return false;
  }

  for(let i = 0; i < s.length - 2; i++){
    if(s[i] == s[i+1] || s[i] == s[i+2] || s[i+1] == s[i+2]){
      return false;
    }
  }
  return true;
}

console.log(isHappy('a'));  // false
console.log(isHappy('aa')); // false
console.log(isHappy('abcd')); // true
console.log(isHappy('aabb')); // false
console.log(isHappy('adb')); // true
console.log(isHappy('xyy')); // false


```



## Answer:
```javascript
