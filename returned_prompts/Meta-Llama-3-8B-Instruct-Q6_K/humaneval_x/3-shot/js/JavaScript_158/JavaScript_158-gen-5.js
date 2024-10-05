  let maxUnique = -1;
  let result = '';

  for (const word of words) {
    const unique_chars = new Set(word).size;
    if (unique_chars > maxUnique) {
      maxUnique = unique_chars;
      result = word;
    }
  }
  return result;
}