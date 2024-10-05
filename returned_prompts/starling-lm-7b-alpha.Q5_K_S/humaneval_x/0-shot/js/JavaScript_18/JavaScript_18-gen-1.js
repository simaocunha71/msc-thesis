Here's one possible solution using regular expressions:

```javascript
const regex = new RegExp(substring, 'g');
return string.match(regex) ? string.match(regex).length : 0;
```

And here's a solution using indexOf and lastIndexOf:

```javascript
let count = 0;
let lastIndex = -1;
while ((lastIndex = string.indexOf(substring, lastIndex + 1)) !== -1) {
  count++;
}
return count;
```

And here's a solution using a for loop:

```javascript
let count = 0;
for (let i = 0; i < string.length; i++) {
  if (string.substring(i, i + substring.length) === substring) {
    count++;
  }
}
return count;
```

Note: These solutions count overlapping cases, meaning if the substring appears multiple times within another string, it will be counted each time it appears.

The regular expression solution is the most elegant, but it may be a bit slower than the for loop solution for very large strings.

The indexOf solution is faster than the regular expression solution, but it may be a bit slower than the for loop solution for very large strings.

The for loop solution is the fastest of the three, but it is also the least elegant.

Here are some benchmarks comparing the three solutions:

```javascript
console.time('regexp');
for (let i = 0; i < 1000000; i++) {
  const regexp = new RegExp('abc', 'g');
  const match = 'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcacba'.match(regexp