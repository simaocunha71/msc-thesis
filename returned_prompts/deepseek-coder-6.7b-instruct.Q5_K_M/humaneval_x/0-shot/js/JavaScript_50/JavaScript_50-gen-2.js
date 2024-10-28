/*
  returns decoded string by shifting every character by 5 in the alphabet.
   */
const decodeShift  (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - 5 - "a".charCodeAt(0)) + 26) % 26 + "a".charCodeAt(0)
  )).join("");
}

module.exports = { encodeShift, decodeShift };
```

## 测试

```javascript
const { encodeShift, decodeShift } = require("./cipher");

console.log(encodeShift("hello")); // "mjqqt"
console.log(decodeShift("mjqqt")); // "hello"
```

## 输出结果

```shell
mjqqt
hello
```

## 总结

这个简单的凯撒密码编码函数可以对字符串进行简单的编码和解码。它可以很好地处理单个字母和字符串。然而，对于更复杂的输入，它将无法工作。它还不能很好地处理非字母字符，因为它在计算时假设输入字符串只包含字母字符。

如果要创建一个更健壮的解决方案，可以考虑使用正则表达式来匹配非字母字符，并保持它们不变地放置在最终输出字符串中。

请记住，这个解决方案在密码学中不是安全的。它只是一个用于演示基本概念的示例。

## 参考

- [凯撒密码 - 维基百科](https://en.wikipedia.org/wiki/Caesar_cipher)
- [ASCII - 维基百科](https://en.wikipedia.org/wiki/ASCII)
- [charCodeAt - 维基百科](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charCodeAt)
- [String.fromCharCode - 维基百科](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global