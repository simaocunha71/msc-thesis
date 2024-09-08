  const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
  const indexes = [];
  for (let i = 0; i < word.length; i++) {
    if (vowels.includes(word[i])) {
      indexes.push(i);
    }
  }
  if (indexes.length == 0) {
    return '';
  }
  const indexesSorted = indexes.sort((a, b) => a - b);
  const leftIndex = indexesSorted[0];
  const rightIndex = indexesSorted[indexesSorted.length - 1];
  const leftChar = word[leftIndex];
  const rightChar = word[rightIndex];
  if (rightIndex - leftIndex == 1) {
    return '';
  }
  for (let i = leftIndex + 1; i < rightIndex; i++) {
    const char = word[i];
    if (char == ' ') {
      continue;
    }
    if (!vowels.includes(char)) {
      return char;
    }
  }
  return '';
}



