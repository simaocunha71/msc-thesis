The code is correct and should work as expected. 

To test it, you can use the following examples:

```javascript
console.log(encodeShift("hello")); // "mjqqt"
console.log(decodeShift("mjqqt")); // "hello"
```

The `encodeShift` function takes a string as input and returns a new string with each character shifted by 5 positions in the alphabet. The `decodeShift` function does the opposite, it takes a string encoded with `encodeShift` and returns the original string.