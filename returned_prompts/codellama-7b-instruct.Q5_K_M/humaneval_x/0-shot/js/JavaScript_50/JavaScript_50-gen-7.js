/*
  returns decoded string by shifting every character back by 5 in the alphabet.
  */
const decodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - 5 - "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)
  )).join("");
}

const encoded = encodeShift("hello");
const decoded = decodeShift(encoded);
console.log(encoded); // expected output: "mjqqt"
console.log(decoded); // expected output: "hello"
```

## 10. [Coding Problem #12](https://github.com/nashville-software-school/client-side-mastery/blob/master/readings/interview-questions.md#coding-problem-12)

```
