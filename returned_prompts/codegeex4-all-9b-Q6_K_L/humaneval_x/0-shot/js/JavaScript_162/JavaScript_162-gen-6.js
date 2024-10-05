You can solve this problem using JavaScript's built-in crypto API. Here's how you can do it:

```javascript
const stringToMd5 = (text) => {
  if (!text) return null;
  const encoder = new TextEncoder();
  const data = encoder.encode(text);
  const hashBuffer = crypto.subtle.digest('MD5', data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  return hashHex;
}
```

In this solution, we first check if the input string is empty. If it is, we return null. Otherwise, we create a new instance of TextEncoder and use it to convert the string to an array of bytes. Then, we use the crypto.subtle.digest() method to compute the MD5 hash of the byte array. The result is a buffer, which we convert to an array of bytes, and then to a string of hexadecimal digits.