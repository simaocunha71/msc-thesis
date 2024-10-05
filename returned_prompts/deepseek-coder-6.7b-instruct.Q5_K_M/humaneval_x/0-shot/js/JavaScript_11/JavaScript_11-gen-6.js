let result = "";

if(a.length !== b.length){
  throw "Strings must be of same length";
}

for(let i = 0; i < a.length; i++){
  result += a[i] ^ b[i];
}

return result;
}

// Testing the function
console.log(stringXor('010', '110')); // '100'
console.log(stringXor('1010', '1100')); // '0110'
console.log(stringXor('111', '111')); // '000'

// Error handling
try{
  console.log(stringXor('111', '101')); // Error: Strings must be of same length
} catch (e){
  console.error(e.message);
}
```

The function `stringXor` takes two binary strings `a` and `b` as arguments. It checks if the lengths of the two strings are same. If they are not, it throws an error. It then performs the XOR operation on each bit of the two strings and appends the result to the `result` string. Finally, it returns the `result` string.

The function is then tested with some sample inputs.

The last block of code demonstrates how the function would handle a situation where the strings are not of the same length. The function throws an error and is caught and handled by printing the error message.







































































































































































