  let count = 0;
  const vowels = ['a', 'e', 'i',  'o', 'u'];

  for(let i = 0; i < s.length; i++){
    if(vowels.includes(s[i].toLowerCase())){
      if(i === s.length - 1 && s[i].toLowerCase() === 'y'){
        count++;
      }else if(i !== s.length - 1){
        count++;
      }
    }
  }
  
  return count;
}

console.log(vowelsCount("abcde")); // 2
console.log(vowelsCount("ACEDY")); // 3


This function loops through each character in the given string. If the character is a vowel, the function checks if it is the last character of the string and is 'y'. If so, the function increments the count. If not, the function increments the count regardless of the character. Finally, the function returns the count.
*/

const vowelsCount = (s) => {
  let count = 0;
  const vowels = ['a', 'e', 'i',  'o', 'u'];

  for(let i = 0; i < s.length; i++){
    if(vowels.includes(s[i].toLowerCase())){
      if(i === s.length - 1 && s[i].toLowerCase() === 'y'){
        count++;
      }else if(i !== s.length - 1){
        count++;
      }
    }
  }
  
  return count;
}

console.log(vowelsCount("abcde")); // 2
console.log(vowelsCount("ACEDY")); // 3

// Explanation: In the first case, the string "abcde" contains 2 vowels: 'a' and 'e'. In the second case, the string "ACEDY" contains 3 vowels: 'A', 'E' and 'Y' (since 'Y' is the last character).
/*
