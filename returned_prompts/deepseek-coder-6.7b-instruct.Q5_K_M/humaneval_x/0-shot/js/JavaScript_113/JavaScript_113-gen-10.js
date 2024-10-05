  return lst.map((str, i) => {
    let count = 0;
    for (let j = 0; j < str.length; j++) {
      if (parseInt(str[j]) % 2 !== 0) {
        count++;
      }
    }
    return `the number of odd elements ${count}n the str${count}ng ${count} of the ${count}nput.`;
  });
};

console.log(oddCount(['1234567']));
console.log(oddCount(['3',"11111111"]));

//expected output
// [ "the number of odd elements 4n the str4ng 4 of the 4nput."]
// [ "the number of odd elements 1n the str1ng 1 of the 1nput.",
// "the number of odd elements 8n the str8ng 8 of the 8nput."]
```

## JavaScript: 
```javascript
