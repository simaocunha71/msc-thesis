  let result = '';
  let consecutiveSpaces = 0;
  for (let i = 0; i < text.length; i++) {
    const char = text[i];
    if (char === ' ') {
      consecutiveSpaces += 1;
      result += '_';
    } else if (char !== ' ') {
      consecutiveSpaces = 0;
      result += char;
    }
    if (consecutiveSpaces > 2) {
      result += '-';
      consecutiveSpaces = 2;
    }
  }

  return result;
}



