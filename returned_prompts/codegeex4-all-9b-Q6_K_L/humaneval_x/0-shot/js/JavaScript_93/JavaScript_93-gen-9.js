```java
const encode = (message) => {
  let vowels = 'aeiouAEIOU';
  let encoded = '';
  for (let i = 0; i < message.length; i++) {
    let char = message[i];
    if (vowels.includes(char)) {
      let nextChar = String.fromCharCode(char.charCodeAt(0) + 2);
      encoded += nextChar;
    } else if (char === char.toLowerCase()) {
      encoded += char.toUpperCase();
    } else {
      encoded += char.toLowerCase();
    }
  }
  return encoded;
}
```