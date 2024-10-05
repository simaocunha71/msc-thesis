  // split the string on the dot
  let split_name = file_name.split(".");
  
  // check if there is exactly one dot and if the split string has two elements
  if (split_name.length !== 2) {
    return "No";
  }
  
  // check if there are more than three digits in the filename
  let countDigit = (split_name[0].match(/\d/g) || []).length;
  if(countDigit > 3) {
    return "No";
  }
  
  // check if the first substring is not empty and starts with a latin alphapet letter
  let regexp_first = /^[A-Za-z][A-Za-z0-9]*$/;
  if (!regexp_first.test(split_name[0])) {
    return "No";
  }
  
  // check if the second substring is one of these:  ['txt',  'exe',  'dll']
  if (!['txt', 'exe', 'dll'].includes(split_name[1])) {
    return "No";
  }
  
  // if all the conditions are met
  return "Yes";
};
```

Here, we are implementing a function `fileNameCheck` that takes a file name as a string and checks whether it is valid or not based on the given conditions. The function splits the filename on the basis of the '.' character, checks the number of digits and if the filename starts with a latin alphapet letter. It also checks if the extension of the file is one of the three given options. If all conditions are met, it returns 'Yes', otherwise it returns 'No'.

The time complexity of the function is O(n), where n is the length of the file name.

Here, we are considering that the file name is a string of characters. If the file name is not a string, the function will not work as expected.

The space complexity of the function is O(n), where n is the length of the file name.

This function is case sensitive and will not work as expected if the file name contains uppercase letters.

It is also assuming that the file