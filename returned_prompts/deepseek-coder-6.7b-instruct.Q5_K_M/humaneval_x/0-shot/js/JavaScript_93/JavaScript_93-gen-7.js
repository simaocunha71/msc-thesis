  let encodedMessage = '';

  for (let i = 0; i < message.length; i++) {
    let char = message[i];

    if (char.match(/[a-z]/)) {
      char = char === char.toLowerCase() ? char.toUpperCase() : char.toLowerCase();
    }

    if (char.match(/[aeiou]/)) {
      char = String.fromCharCode(char.charCodeAt(0) + 2);
    }

    encodedMessage += char;
  }

  return encodedMessage;
};

console.log(encode('test')); // TGST
console.log(encode('This is a message')); // tHKS KS C MGSSCGG

```

## Question 2

```js
