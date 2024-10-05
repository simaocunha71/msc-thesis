  let result = '';
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  for (let i = 0; i < message.length; i++) {
    let char = message[i];
    if (char.match(/[a-z]/i)) {
      if (vowels.includes(char.toLowerCase())) {
        char = char === char.toLowerCase() ? char.toUpperCase() : char.toLowerCase();
        char = String.fromCharCode(char.charCodeAt(0) + 2);
      }
      char = char === char.toLowerCase() ? char.toUpperCase() : char.toLowerCase();
    }
    result += char;
  }
  return result;
}



