/*
  returns decoded string by shifting every character by -5 in the alphabet.
   */
const decodeShift  (s)  {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - 5 - "a".charCodeAt(0) + 26) % 26) + "a".charCodeAt(0)
  )).join("");
}

module.exports = { encodeShift, decodeShift };
```

## ✍️ Solutions

### Q1

```javascript
let string = "Hello, World!";
console.log(string);
```

### Q2

```javascript
let string1 = "Programming";
let string2 = "Javascript";
console.log(string1 + " " + string2);
```

### Q3

```javascript
let string = "Hello, World!";
console.log(string.length);
```

### Q4

```javascript
let string = "Programming";
console.log(string.toUpperCase());
```

### Q5

```javascript
let string = "Javascript";
console.log(string.slice(0, 4));
```

### Q6

```javascript
let string = "Hello, World!";
console.log(string.replace("World", "Students"));
```

### Q7

```javascript
let string = "Javascript";
console.log(string.split("").reverse().join(""));
```

### Q8

```javascript
let string = "Hello, World!";
console.log(string.includes("World"));
```

### Q9

```javascript
let string = "Programming";
console.log(string.charAt(string.length - 1));
```

### Q10

```javascript
let string = "Javascript";
console.log(string.charCodeAt(0));
```

### Q11

```javascript
let string = "Hello, World!";
console.log(string.replace(/World/g, "Students"));
```

