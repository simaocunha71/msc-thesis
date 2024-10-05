  if(text === '') {
    return null;
  } else {
    return crypto.createHash('md5').update(text).digest('hex');
  }
};
```

## 2.2.2. Hash Function

A hash function is a mathematical algorithm that takes an input (or 'message') and returns an output (or 'hash', a fixed-size string of bytes).

The output is unique to the input. In theory, it is impossible to find the original input from the hash. This makes it useful for data storage and retrieval, and for checksums, message authentication, and secure data transmission. 

There are many different types of hash functions, but one of the most common is the MD5 (Message Digest Algorithm 5).

## 2.2.3. Crypto Library

The 'crypto' library in Node.js provides cryptographic functionality that includes a set of wrappers for OpenSSL's hash, HMAC, cipher, decipher, sign, and verify functions.

The `createHash(algorithm)` function creates and returns a hash object.

The `update(data)` function is used to pass data through the hash.

The `digest(encoding)` function is used to finalize the hash computation and return the resulting string.

The 'encoding' can be 'hex' for hexadecimal string representation or 'binary' for a binary string representation.

## 2.2.4. MD5

MD5 (Message Digest Algorithm 5) is a widely used cryptographic hash function that produces a 128-bit (16-byte) hash value.

Although MD5 is no longer considered secure against well-funded attackers, it is still widely used for a variety of security applications, including to provide a checksum for data.

## 2.2.5. Node.js Example

Here's an example of how to use the crypto library to create an MD5 hash:

```javascript
const crypto = require('crypto');

const text = 'Hello world';
const hash = crypto.createHash('md5').update(text).digest('hex');

console.log(hash);  // Outputs: 3e2596