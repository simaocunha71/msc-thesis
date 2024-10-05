```java
const encode = (message) => {
  var vowels = 'aeiouAEIOU';
  var encoded = '';
  for (var i = 0; i < message.length; i++) {
    var char = message[i];
    if (vowels.includes(char)) {
      var nextChar = String.fromCharCode(char.charCodeAt(0) + 2);
      encoded += nextChar.toUpperCase() === nextChar ? nextChar.toLowerCase() : nextChar.toUpperCase();
    } else {
      encoded += char.toUpperCase() === char ? char.toLowerCase() : char.toUpperCase();
    }
  }
  return encoded;
}
```