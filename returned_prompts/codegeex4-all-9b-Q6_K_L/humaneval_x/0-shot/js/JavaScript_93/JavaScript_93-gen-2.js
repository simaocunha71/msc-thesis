```java
const encode = (message) => {
  let vowels = ['a', 'e', 'i', 'o', 'u'];
  let encodedMessage = '';
  for (let i = 0; i < message.length; i++) {
    let letter = message[i];
    if (vowels.includes(letter.toLowerCase())) {
      letter = String.fromCharCode(letter.charCodeAt(0) + 2);
    }
    if (letter === letter.toUpperCase()) {
      letter = letter.toLowerCase();
    } else {
      letter = letter.toUpperCase();
    }
    encodedMessage += letter;
  }
  return encodedMessage;
}
```
