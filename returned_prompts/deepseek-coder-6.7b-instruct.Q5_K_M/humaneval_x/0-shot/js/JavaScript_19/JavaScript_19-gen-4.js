  const words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
  const numbersArray = numbers.split(" ");

  numbersArray.sort((a, b) => {
    return words.indexOf(a) - words.indexOf(b);
  });

  return numbersArray.join(" ");
}

console.log(sortNumbers('three one five'));

*/

let sortNumbers = (numbers) => {
  let words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
  let numbersArray = numbers.split(" ");

  numbersArray.sort((a, b) => {
    return words.indexOf(a) - words.indexOf(b);
  });

  return numbersArray.join(" ");
}

console.log(sortNumbers('three one five'));
```

# --solutions--

```javascript
let sortNumbers = (numbers) => {
  let words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
  let numbersArray = numbers.split(" ");

  numbersArray.sort((a, b) => {
    return words.indexOf(a) - words.indexOf(b);
  });

  return numbersArray.join(" ");
}

console.log(sortNumbers('three one five'));
```

# --output--

```
one three five
```

# --celebrate--

![Party popper](https://cdn.freecodecamp.org/platform/200HxCE0WPRN2rJsNR6NP9e6JU53/v1/img/party-popper.jpg)

## ![:rocket:](https://cdn.freecodecamp.org/platform/200HxCE0WPRN2rJsNR6NP9e6JU53/v1/img/solution-icon/rocket.png) Solution Explanation:
