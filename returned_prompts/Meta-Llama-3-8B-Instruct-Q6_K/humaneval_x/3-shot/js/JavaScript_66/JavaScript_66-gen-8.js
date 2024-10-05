  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i].toUpperCase() === s[i]) {
      sum += s.charCodeAt(i);
    }
  }
  return sum;
}  // This function works by iterating over each character in the string. It checks if the character is uppercase (by comparing it to its uppercase version) and if so, adds its ASCII value to the sum. This is because ASCII values for uppercase letters are distinct and greater than those for lowercase letters. The function then returns the sum.  // This function works by iterating over each character in the string. It checks if the character is uppercase (by comparing it to its uppercase version) and if so, adds its ASCII value to the sum. This is because ASCII values for uppercase letters are distinct and greater than those for lowercase letters. The function then returns the sum.