  const vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"];
  let isFound = false;
  let result = "";

  for (let i = word.length - 1; i >= 0; i--) {
    const currentChar = word[i];
    if (!isFound && !vowels.includes(currentChar)) {
      for (let j = i - 1; j >= 0; j--) {
        const prevChar = word[j];
        if (!vowels.includes(prevChar)) {
          for (let k = j - 1; k >= 0; k--) {
            const prevPrevChar = word[k];
            if (vowels.includes(prevPrevChar)) {
              result = prevPrevChar;
              isFound = true;
              break;
            }
          }
        }
      }
    }
  }

  return result;
}



