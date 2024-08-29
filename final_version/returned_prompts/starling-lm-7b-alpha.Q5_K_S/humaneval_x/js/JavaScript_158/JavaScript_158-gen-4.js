  const uniqueChar = (word) => {
    const charSet = new Set();
    for (const c of word) {
      charSet.add(c);
    }
    return charSet.size;
  };

  const maxUnique = Math.max(...words.map(uniqueChar));

  return words.find(word => uniqueChar(word) == maxUnique);
}



