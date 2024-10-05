  let count = 0;
  
  for(let i = 0; i < brackets.length; i++) {
    if(brackets[i] === "(") {
      count++;
    } else if(brackets[i] === ")") {
      count--;
      if(count < 0) {
        return false;
      }
    }
  }
  
  return count === 0;
}

console.log(correctBracketing("("));  // false
console.log(correctBracketing("()"));  // true
console.log(correctBracketing("(()())"));  // true
console.log(correctBracketing(")(()"));  // false

// Time complexity: O(n)
// Space complexity: O(1)

```


## 4. Split an array into two parts at a given index

```javascript
