  let isPrime = true;

  if (n === 1) {
    isPrime = false;
  }
  else if (n > 1) {
    for(let i = 2; i < n; i++) {
      if(n % i === 0) {
        isPrime = false;
        break;
      }
    }
  }

  return isPrime ? x : y;
}

console.log(xOrY(7, 34, 12)); // 34
console.log(xOrY(15, 8, 5)); // 5
console.log(xOrY(2, 10, 20)); // 10
console.log(xOrY(3, 10, 20)); // 10
console.log(xOrY(4, 10, 20)); // 20
```

</details>

<details>
<summary><b>Exercise 4</b></summary>

