  const sortedList = lst.sort((a, b) => a.length - b.length);
  const uniqueList = new Set(sortedList);
  const result = [];
  for (const word of uniqueList) {
    const count = lst.filter(w => w === word).length;
    result.push(word.repeat(count));
  }
  return result.join('');
}



