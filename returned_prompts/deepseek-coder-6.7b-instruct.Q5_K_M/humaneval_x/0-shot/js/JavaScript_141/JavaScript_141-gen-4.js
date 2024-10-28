  let countDigit = (file_name.match(/[0-9]/g) || []).length;
  let countDot = (file_name.match(/\./g) || []).length;
  let startLetter = /^[A-Za-z]/.test(file_name.charAt(0));
  let endExtension = ['txt', 'exe', 'dll'].includes(file_name.split('.').pop());

  return (countDigit <= 3 && countDot == 1 && startLetter && endExtension) ? 'Yes' : 'No';
};

console.log(fileNameCheck("example.txt"));
console.log(fileNameCheck("1example.dll"));
console.log(fileNameCheck("exa1234.mdf"));
console.log(fileNameCheck("exa..mp.le"));
console.log(fileNameCheck("exa123.pdf"));


//Testing
//Expected Output: 
//Yes
//No
//No
//No
//Yes

The function `fileNameCheck` first counts the number of digits and dots in the filename. It then checks if the filename starts with a letter and if the file has one of the allowed extensions. It returns 'Yes' if all conditions are met and 'No' otherwise.

It uses the JavaScript method `match()` to count the digits and dots, `includes()` to check if the extension is allowed, and `test()` to check if the first character is a letter.

The filename is split into two parts by the dot using `split('.')`, and the last part (after the dot) is checked.

The ternary operator `? :` is used to return 'Yes' if all conditions are met and 'No' otherwise.

Please note that this solution does not check if the filename is too long, or contains invalid characters.
*/










































































