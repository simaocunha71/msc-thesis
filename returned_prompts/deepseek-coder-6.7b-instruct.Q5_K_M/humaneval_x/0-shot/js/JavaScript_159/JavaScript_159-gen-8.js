  const total = number + Math.min(need, remaining);
  const left = remaining <= need ? 0 : remaining - need;
  return [total, left];
}

console.log(eat(5, 6, 10)); // [11, 4]
console.log(eat(4, 8, 9)); // [12, 1]
console.log(eat(1, 10, 10)); // [11, 0]
console.log(eat(2, 11, 5)); // [7, 0]

/*
  Explanation:
  
  In the first example, you have 5 carrots and need 6. The minimum between 6 and 10 remaining carrots is 10, so you'll eat 15 carrots.
  
  In the second example, you have 4 carrots and need 8. The minimum between 8 and 9 remaining carrots is 8, so you'll eat 12 carrots.
  
  In the third example, you have 1 carrot and need 10. The minimum between 10 and 10 remaining carrots is 10, so you'll eat 11 carrots.
  
  In the fourth example, you have 2 carrots and need 11. The minimum between 11 and 5 remaining carrots is 5, so you'll eat 7 carrots.
 */

```

## Solution 2:

```javascript
