  let arr = test.split(' ');
  let count = {};
  let max = 0;
  let result = {};

  for(let i = 0; i < arr.length; i++){
    if(count[arr[i]]){
      count[arr[i]]++;
    }else{
      count[arr[i]] = 1;
    }
    if(count[arr[i]] > max){
      max = count[arr[i]];
    }
  }

  for(let key in count){
    if(count[key] === max){
      result[key] = count[key];
    }
  }

  return result;
}

console.log(histogram('a b c')) //== {'a': 1, 'b': 1, 'c': 1}
console.log(histogram('a b b a')) //== {'a': 2, 'b': 2}
console.log(histogram('a b c a b')) //== {'a': 2, 'b': 2}
console.log(histogram('b b b b a')) //== {'b': 4}
console.log(histogram('')) //== {}
```

This program takes a string of lowercase letters and splits it into an array. It then loops through the array to count the number of occurrences of each letter and keep track of the max count. It then loops through the count object to find the letters that have the max count and adds them to the result object.

Finally, it returns the result object.

The time complexity of this solution is O(n), where n is the number of letters in the string. The space complexity is also O(n) because of the space required to store the count and result objects.

The solution assumes that the input string will not contain any non-alphabetic characters or uppercase letters. If this is not the case, additional error checking or data cleaning would be needed.

This solution assumes that the count of a letter is case-sensitive. If this is not the case, the letter 'a' and 'A' would both be counted as 1. If this is desired, the string can be converted to either lower or upper case before counting