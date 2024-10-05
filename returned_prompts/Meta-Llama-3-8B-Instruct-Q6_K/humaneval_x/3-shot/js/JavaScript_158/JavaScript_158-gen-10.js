  let maxCount = 0;
  let result = '';
  for (const word of words) {
    const charSet = new Set(word);
    if (charSet.size > maxCount) {
      maxCount = charSet.size;
      result = word;
    }
  }
  return result;
}