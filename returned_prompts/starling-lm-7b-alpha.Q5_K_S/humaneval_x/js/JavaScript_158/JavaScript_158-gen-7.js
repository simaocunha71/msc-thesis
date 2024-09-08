  const maxLength = Math.max(...words.map(word => word.length));
  const maxLengthWords = words.filter(word => word.length == maxLength);

  let result = maxLengthWords[0];
  for (const word of maxLengthWords.slice(1)) {
    let uniqueCharCount = new Set(word).size;
    let resultCharCount = new Set(result).size;
    if (uniqueCharCount > resultCharCount) {
      result = word;
    } else if (uniqueCharCount == resultCharCount) {
      result = word < result ? word : result;
    }
  }

  return result;
}



