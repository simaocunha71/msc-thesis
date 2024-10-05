  let count = [0,0];
  let strNum = Math.abs(num).toString();

  for(let i = 0; i < strNum.length; i++){
    if(strNum[i] % 2 === 0) count[0]++;
    else count[1]++;
  }
  return count;
}

console.log(evenOddCount(-12));
console.log(evenOddCount(123));
console.log(evenOddCount(1122334455));
console.log(evenOddCount(9876543210));
console.log(evenOddCount(0));

```

### Code:

```javascript
