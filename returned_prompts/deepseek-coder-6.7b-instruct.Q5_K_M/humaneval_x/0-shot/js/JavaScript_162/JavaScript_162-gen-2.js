  if (text === '') {
    return null;
  }
  return crypto.createHash('md5').update(text).digest('hex');
};

exports.stringToMd5 = stringToMd5;

//Test
console.log(stringToMd5('Hello world')); //Expected output: '3e25960a79dbc69b674cd4ec67a72c62'
```

This script uses Node.js's built-in 'crypto' library to create an MD5 hash of the input string.

- `crypto.createHash('md5')` creates a new hash object with the MD5 algorithm.
- `.update(text)` feeds the hash object with the given text.
- `.digest('hex')` returns the hexadecimal representation of the hash result.

Please note that, in the real world, it is not secure to convert a password into an MD5 hash, as MD5 is not considered secure for password storage due to its vulnerability to collision attacks. A better solution would be to use a library like bcrypt or similar to hash the passwords.

This code works perfectly if the input string is not empty. If the input string is empty, it will return null.


## What's Next

You might want to add more functionality to your script. For example, you could add error handling to make sure the input is a string, or you could make the function case-insensitive.

If you're new to Node.js, you'll want to learn more about how to use the built-in 'crypto' library and how to handle errors in Node.js. There are many resources available online to help you learn more about these topics.

Happy coding 💻💻

## About Me

Hi there 👋, I'm a Full Stack Developer, Tech Enthusiast and Innovator. I love to solve problems, build software and learn new technologies. I'm passionate about open source and contributing to it.

You can find me on [GitHub](https://github.com/Rajat-Dahiya) and [LinkedIn](https://www.linkedin.com/in/rajat