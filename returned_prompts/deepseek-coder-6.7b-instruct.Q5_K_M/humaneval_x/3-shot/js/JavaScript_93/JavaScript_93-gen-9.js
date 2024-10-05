  let result = '';
  const vowels = 'aeiou';
  const upperVowels = vowels.toUpperCase();

  for  (let i = 0; i < message.length; i++) {
    let char = message[i];
    if  (char.match(/[a-z]/)) {
      if  (vowels.includes(char)) {
        result += upperVowels[vowels.indexOf(char) + 2];
      } else {
        result += char.toUpperCase();
      }
    } else if  (char.match(/[A-Z]/)) {
      if  (upperVowels.includes(char)) {
        result += vowels[upperVowels.indexOf(char) + 2];
      } else {
        result += char.toLowerCase();
      }
    } else {
      result += char;
    }
  }

  return result;
}



