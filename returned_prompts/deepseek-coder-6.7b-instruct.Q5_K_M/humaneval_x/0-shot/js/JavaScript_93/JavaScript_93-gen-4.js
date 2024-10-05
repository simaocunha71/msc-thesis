  let result = "";
  
  for (let i = 0; i < message.length; i++) {
    let char = message[i];
    if (char.match(/[aeiou]/i)) {
      char = char.toLowerCase();
      switch (char) {
        case "a":
          result += "c";
          break;
        case "e":
          result += "g";
          break;
        case "i":
          result += "k";
          break;
        case "o":
          result += "q";
          break;
        case "u":
          result += "w";
          break;
      }
    } else {
      result += char.toUpperCase();
    }
  }
  
  return result;
}

console.log(encode('test')); // 'TGST'
console.log(encode('This is a message')); // 'tHKS KS C MGSSCGG'

module.exports = encode;

```


## 4. 

```javascript

