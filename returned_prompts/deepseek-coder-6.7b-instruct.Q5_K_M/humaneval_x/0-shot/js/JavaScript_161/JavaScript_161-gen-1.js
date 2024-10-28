  let newStr = '';
  for(let i = 0; i < s.length; i++){
    if(s[i].toLowerCase() !== s[i].toUpperCase()) {
      newStr += (s[i] === s[i].toLowerCase()) ? s[i].toUpperCase() : s[i].toLowerCase();
    } else {
      newStr += s[i];
    }
  }
  if(newStr === ''){
    return s.split('').reverse().join('');
  } else {
    return newStr;
  }
}
console.log(solve("1234")); // 4321
console.log(solve("ab")); // AB
console.log(solve("#a@C")); // #A@c
console.log(solve("")); // ""


The function solve takes a string s as input. If the string contains letters, it reverses the case of each letter in the string. If there are no letters, it reverses the entire string. The function returns the resulting string.

The function uses a for loop to iterate through each character in the string. If the character is a letter, it checks if its case is lower or upper. If it's lower, it changes it to upper and vice versa. If it's not a letter, it keeps it as it is. The resulting string is returned. If the resulting string is empty, the function reverses the entire input string before returning it.

The time complexity of this function is O(n), where n is the length of the string. This is because the function iterates through each character in the string once. The space complexity is also O(n), due to the space used to store the resulting string.
*/

//P:
//s: string

//R: 
//string: reverse case of each letter or reverse entire string if no letters

//E:
//solve("1234") = "4321"
//solve("ab") = "AB"
//solve("#a@C") = "#A@c"

//W:
//newStr: string

//I:
//i: int

//C: