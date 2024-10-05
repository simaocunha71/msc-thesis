let result = "";
let current = x;

while (current > 0) {
  result = (current % base) + result;
  current = Math.floor(current/base);
}

return result;
}

console.log(changeBase(8, 3));  // '22'
console.log(changeBase(8, 2));  // '1000'
console.log(changeBase(7, 2));  // '111'

```

</details>

### 16.11.2020

<details>
  <summary>
    Write a function to calculate the greatest common divisor of two numbers.
  </summary>

