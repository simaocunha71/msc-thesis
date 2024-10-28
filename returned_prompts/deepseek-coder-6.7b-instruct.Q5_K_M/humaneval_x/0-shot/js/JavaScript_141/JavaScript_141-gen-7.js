  const countDigit = (str) => {
    let count = 0;
    for(let i = 0; i < str.length; i++) {
        if(str[i] >= '0' && str[i] <= '9') count++;
    }
    return count;
  }

  const countPoint = (str) => {
    let count = 0;
    for(let i = 0; i < str.length; i++) {
        if(str[i] === '.') count++;
    }
    return count;
  }

  if(countPoint(file_name) !== 1) return 'No';
  if(countDigit(file_name) > 3) return 'No';

  let [name, extention] = file_name.split('.');

  if(!name || !name[0].match(/[a-zA-Z]/)) return 'No';
  if(!['txt', 'exe', 'dll'].includes(extention)) return 'No';

  return 'Yes';
}

console.log(fileNameCheck("example.txt"));  //  'Yes'
console.log(fileNameCheck("1example.dll"));  //  'No'

This program works by first splitting the file name into the name and the extention. It then checks if there is exactly one dot in the file name, if there are more than 3 digits in the name, if the name starts with a letter, and if the extention is one of the allowed ones. If any of these conditions are not met, the function returns 'No'. Otherwise, it returns 'Yes'. 

The countDigit and countPoint functions are used to count the number of digits and dots in the file name respectively. The match method is used to check if the first character of the name is a letter. The includes method is used to check if the extention is one of the allowed ones.
*/































































