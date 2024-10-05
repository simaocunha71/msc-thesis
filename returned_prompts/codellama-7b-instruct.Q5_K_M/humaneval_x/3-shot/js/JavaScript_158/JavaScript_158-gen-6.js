  const countChars = (s) => {
    var count = {};
    for (const c of s) {
      count[c] = (count[c] || 0) + 1;
    }
    return count;
  }

  const maxCount = Math.max(...words.map(countChars).map(Object.keys).map(arr => arr.length));
  const maxChars = words.find(s => countChars(s).length == maxCount);
  return maxChars;
}



