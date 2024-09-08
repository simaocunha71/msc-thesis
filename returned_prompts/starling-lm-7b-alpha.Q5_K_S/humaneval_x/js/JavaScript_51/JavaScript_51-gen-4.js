  const vowels = ['a', 'e', 'i', 'o', 'u'];
  let result = '';

  for (const char of text) {
    if (!vowels.includes(char)) {
      result += char;
    }
  }

  return result;
}



