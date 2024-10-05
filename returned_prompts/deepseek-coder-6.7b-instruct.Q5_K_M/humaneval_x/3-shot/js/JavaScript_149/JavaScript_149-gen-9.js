  let evenLengthWords = lst.filter(word => word.length % 2 === 0);
  return evenLengthWords.sort((a, b) => a.length - b.length || a.localeCompare(b));
}



