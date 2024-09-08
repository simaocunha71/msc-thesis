  const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
  let result = '';

  for (const char of text) {
    if (!vowels.includes(char)) {
      result += char;
    }
  }

  return result;
}



