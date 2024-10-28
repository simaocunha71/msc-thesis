  let result = '';
  const vowels = ['a', 'e', 'i', 'o', 'u'];

  for (const char of message) {
    if (vowels.includes(char)) {
      result += String.fromCharCode(char.charCodeAt(0) + 2);
    } else if (char.match(/[A-Z]/)) {
      result += String.fromCharCode(char.charCodeAt(0) - 65);
    } else {
      result += char;
    }
  }
  return result;
}



