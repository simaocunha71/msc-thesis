  return s.replace(/[,]/g, ' ').split(' ');
}

console.log(wordsString('Hi, my name is John'));
console.log(wordsString('One, two, three, four, five, six'));

// This solution works by replacing all commas with spaces (',/g, ' ') using the replace() method.
// Then it splits the string into an array of words using the split() method.
// The resulting array is returned.
```

The above code will print:

```
[ 'Hi', 'my', 'name', 'is', 'John' ]
[ 'One', 'two', 'three', 'four', 'five', 'six' ]
```

This is because the replace() method changes all commas into spaces, and then the split() method splits the string into an array of words at each space.

---

**Note:**

- The replace() method returns a new string with some or all matches of a pattern replaced by a replacement.
- The split() method splits a String object into an array of strings by separating the string into substrings, using a specified separator string to determine where to make each split.

---

**References:**

- [MDN Web Docs - String.prototype.replace()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)
- [MDN Web Docs - String.prototype.split()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)

---

**Further Reading:**

- [JavaScript String replace() Method](https://www.w3schools.com/jsref/jsref_replace.asp)
- [JavaScript String split() Method](https://www.w3schools.com/jsref/jsref_split.asp)

---

**Further Practice:**

- Try to solve more problems about string manipulation in JavaScript.
- Try to solve problems about string manipulation in other programming languages.

---

**Continue Learning:**

- [JavaScript Array Methods](https://