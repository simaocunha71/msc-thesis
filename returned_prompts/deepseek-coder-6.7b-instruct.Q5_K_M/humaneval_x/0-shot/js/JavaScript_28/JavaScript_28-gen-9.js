  return strings.join('');
}

module.exports = concatenate;
```

## Conclusion

In this exercise, you've learned how to concatenate a list of strings into a single string. The `join()` method is a handy tool for this, as it combines the elements of an array into a string, with an optional separator provided.

In future exercises, you will be able to use this knowledge to manipulate strings in JavaScript in a variety of ways.

## Resources

- [Array join()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)
- [Array join() - StackOverflow](https://stackoverflow.com/questions/1644465/javascript-join-array-elements-with-comma)

---

If you're having trouble with this exercise, don't hesitate to ask. We're here to help you. Good luck with your coding journey and happy coding in JavaScript 🎉

</div>

<div id="solution" class="hidden">

```javascript
/* Concatenate list of strings into a single string
  >>> concatenate([])
   ''
  >>> concatenate(['a',  'b',  'c'])
   'abc'
 */
const concatenate = (strings) => {
  return strings.join('');
}

module.exports = concatenate;
```

</div>

<div id="tests" class="hidden">

```javascript
const concatenate = require('./concatenate');

console.log(concatenate([]) === ''); // true
console.log(concatenate(['a', 'b', 'c']) === 'abc'); // true
```

</div>

<div id="hints" class="hidden">

</div>

<div id="answer" class="hidden">

</div>

<div id="explanation" class="hidden">

</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight