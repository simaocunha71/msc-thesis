  let result = [...l];
  const indexes = result.findIndexes(i => i % 3 === 0);
  const sortedIndexes = indexes.sort((a, b) => result[a] - result[b]);
  indexes.forEach(i => result[i] = result[sortedIndexes[i % sortedIndexes.length]]);
  return result;
}



