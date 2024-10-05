  const words = sentence.split(' ');
  let result = [];

  for (const word of words) {
    const length = word.length;
    if (length % 2 !== 0 && length % 3 !== 0 && length % 5 !== 0 && length % 7 !== 0) {
      result.push(word);
    }
  }

  return result.join(' ');
}