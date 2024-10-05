  let result = '';
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  for (let i = 0; i < message.length; i++) {
    let char = message[i];
    if (char.match(/[a-z]/i)) {
      if (vowels.includes(char.toLowerCase())) {
        let index = vowels.indexOf(char.toLowerCase());
        char = vowels[(index + 2) % 5];
      }
      char = char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase();
    }
    result += char;
  }
  return result;
}



