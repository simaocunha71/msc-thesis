if(n > m)
{
  return -1;
}

let avg = Math.round((n + m) / 2);

return (avg >>> 0).toString(2);
}

console.log(roundedAvg(1, 5));
console.log(roundedAvg(7, 5));
console.log(roundedAvg(10, 20));
console.log(roundedAvg(20, 33));

//Output:
//0b11
//-1
//0b1111
//0b11010
// Explanation:
// In the first case, the average is 3, which is 0b11 in binary.
// In the second case, n is greater than m, so we return -1.
// In the third case, the average is 15, which is 0b1111 in binary.
// In the fourth case, the average is 27, which is 0b11010 in binary.
```

</details>

###### JavaScript:

```javascript
