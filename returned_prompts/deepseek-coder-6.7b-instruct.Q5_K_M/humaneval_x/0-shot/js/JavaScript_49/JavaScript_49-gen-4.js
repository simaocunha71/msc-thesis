  return BigInt(2) ** BigInt(n) % BigInt(p);
};

console.log(modp(3, 5));
console.log(modp(1101, 101));
console.log(modp(0, 101));
console.log(modp(3, 11));
console.log(modp(100, 101));
```

The solution uses JavaScript's BigInt type to handle very large numbers. The ** operator raises the first operand to the power of the second operand, and % returns the remainder of division. By using BigInt, we can handle numbers that would exceed JavaScript's Number.MAX_SAFE_INTEGER.

This solution will work as expected and should be able to handle any numbers that the JavaScript BigInt type can handle.

---

**Note:**

This solution assumes that you are using a JavaScript environment that supports ES6 (ECMAScript 6) or a later version. JavaScript ES6 was released in 2015 and includes features such as BigInt and exponentiation operator (**), which are not supported in older environments.

If you're using an older JavaScript environment, you may need to find a different solution or use a polyfill for BigInt and exponentiation.

---

**Further Reading:**

- [JavaScript BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
- [JavaScript Exponentiation (**)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation)
- [JavaScript Modulus (%)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Modulus)
- [ES6 Features](https://www.w3schools.com/Js/js_es6.asp)
- [Using BigInts](https://javascript.info/bigint)
- [JavaScript BigInt Polyfill](https://github.com/Nikaple/BigInteger.js)
- [JavaScript ES6 Support](https://caniuse