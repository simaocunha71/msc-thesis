```java
const encrypt = (s) => {
  let alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let encrypted = '';
  for (let i = 0; i < s.length; i++) {
    let char = s[i];
    let index = alphabet.indexOf(char);
    if (index !== -1) {
      let newIndex = (index + 4) % alphabet.length;
      encrypted += alphabet[newIndex];
    } else {
      encrypted += char;
    }
  }
  return encrypted;
}
```