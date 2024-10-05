  return s.replace(/[ ,]+/g, ' ').split(' ');

};

console.log(wordsString("Hi, my name is John"));
console.log(wordsString("One, two, three, four, five, six"));


/*
  This solution uses the JavaScript string method `split()`. It splits a string into an array of substrings based on a specified separator (in this case, a comma or space). The `replace()` function is used to replace any sequence of one or more spaces or commas with a single space.
*/
```




## 2. String to Array of Words


```javascript
const stringToArray = (s) => {
  return s.split(' ');
};

console.log(stringToArray("Hi my name is John"));
```



## 3. Words to Sentence


```javascript
const wordsToString = (words) => {
  return words.join(' ');
};

console.log(wordsToString(["Hi", "my", "name", "is", "John"]));
```




## 4. Capitalize First Letter


```javascript
const capitalizeFirstLetter = (s) => {
  return s.charAt(0).toUpperCase() + s.slice(1);
};

console.log(capitalizeFirstLetter("hi"));
```




## 5. Reverse String


```javascript
const reverseString = (s) => {
  return s.split('').reverse().join('');
};

console.log(reverseString("Hi"));
```




## 6. Count Characters


```javascript
const countCharacters = (s) => {
  return s.length;
};

console.log(countCharacters("Hi"));
```




## 7. Check If Palindrome


```javascript
const isPalindrome = (s) => {
  return s.split('').reverse().join('') === s;
};

console.log(isPalindrome("Hi"));
```




## 