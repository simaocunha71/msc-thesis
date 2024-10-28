  let newMessage = '';
  for(let i = 0; i < message.length; i++) {
    let char = message[i];
    if(char.match(/[aeiou]/i)) {
      char = char.toUpperCase();
      if(char === 'E') char = 'G';
      else if(char === 'I') char = 'K';
      else if(char === 'O') char = 'Q';
      else if(char === 'U') char = 'W';
      else if(char === 'A') char = 'C';
      else {
        char = String.fromCharCode(char.charCodeAt() + 2);
      }
    } else if(char.match(/[AEIOU]/)) {
      char = char.toLowerCase();
      if(char === 'e') char = 'g';
      else if(char === 'i') char = 'k';
      else if(char === 'o') char = 'q';
      else if(char === 'u') char = 'w';
      else if(char === 'a') char = 'c';
      else {
        char = String.fromCharCode(char.charCodeAt() - 2);
      }
    }
    newMessage += char;
  }
  return newMessage;
};

console.log(encode('test'));
console.log(encode('This is a message'));
console.log(encode('JavaScript is fun'));
console.log(encode('Switch Case'));
console.log(encode('Loops'));
```

## Output
```
tGST
tHKS KS C MGSSCGG
jWvScs ks c MGSSCGG
TkcU Vs c MGSSCGG
TkcS
vSks
```


```















































































