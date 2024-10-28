  let newMessage = "";

  for (let i = 0; i < message.length; i++) {
    let char = message[i];
    if (char.match(/[a-z]/i)) {
      if (char === char.toLowerCase()) {
        newMessage += char.toUpperCase();
      } else {
        newMessage += char.toLowerCase();
      }
    } else if (char.match(/[aeiou]/i)) {
      switch (char.toLowerCase()) {
        case 'a':
          newMessage += 'c';
          break;
        case 'e':
          newMessage += 'g';
          break;
        case 'i':
          newMessage += 'k';
          break;
        case 'o':
          newMessage += 'q';
          break;
        case 'u':
          newMessage += 'w';
          break;
      }
    } else {
      newMessage += char;
    }
  }

  return newMessage;
};

console.log(encode('test')); // 'TGST'
console.log(encode('This is a message')); // 'tHKS KS C MGSSCGG'
console.log(encode('JavaScript is fun')); // 'JGVCKSVW KS C MZGSSKGVW'
console.log(encode('123abc')); // '123ABC'
console.log(encode('@#$%')); // '@#$%'
console.log(encode('')); // ''
```

## Question 4:

```markdown
