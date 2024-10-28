```java
const encode = (message) => {
  var vowels = ['a', 'e', 'i', 'o', 'u'];
  var encodedMessage = '';
  for (let i = 0; i < message.length; i++) {
    let currentChar = message[i];
    if (currentChar === currentChar.toUpperCase()) {
      if (vowels.includes(currentChar.toLowerCase())) {
        let nextChar = String.fromCharCode(currentChar.charCodeAt(0) + 2);
        encodedMessage += nextChar.toUpperCase();
      } else {
        encodedMessage += currentChar.toLowerCase();
      }
    } else {
      if (vowels.includes(currentChar)) {
        let nextChar = String.fromCharCode(currentChar.charCodeAt(0) + 2);
        encodedMessage += nextChar;
      } else {
        encodedMessage += currentChar.toUpperCase();
      }
    }
  }
  return encodedMessage;
}
```
