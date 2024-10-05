To convert a number from a base to another base, you can use the following steps:

1. Convert the number to a string.
2. Reverse the string.
3. For each digit in the string, convert it to its equivalent in the desired base.
4. Multiply the converted digit by the corresponding power of the base.
5. Add up all the converted and multiplied values.
6. Return the result.

Here's a step-by-step explanation of the solution:

- First, convert the input number `x` to a string using the `toString()` method. This will give us a string representation of the number in base 10.

```javascript
const xString = x.toString();
```

- Next, reverse the string using the `split().reverse().join()` method. This will reverse the order of the digits in the string.

```javascript
const reversedString = xString.split('').reverse().join('');
```

- Now, we need to convert each digit in the reversed string to its equivalent in the desired base. We can do this by iterating over each digit and using a switch statement to convert the digit to the desired base.

```javascript
const result = [];
for (let i = 0; i < reversedString.length; i++) {
  switch (reversedString[i]) {
    case '0':
      result.push(0);
      break;
    case '1':
      result.push(1);
      break;
    case '2':
      result.push(2);
      break;
    case '3':
      result.push(3);
      break;
    case '4':
      result.push(4);
      break;
    case '5':
      result.push(5);
      break;
    case '6':
      result.push(6);
      break;
    case '7':
      result.push(7);
      break;
    case '8':
      result.push(8);
      break;
    case '9':
      result.push(9);
      break;
    default:
      break;
  }
}
```

