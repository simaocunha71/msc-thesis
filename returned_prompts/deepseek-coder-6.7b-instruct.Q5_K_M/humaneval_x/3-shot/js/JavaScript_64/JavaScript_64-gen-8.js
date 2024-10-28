  const vowels = ['a', 'e', 'i', 'o', 'u', 'y'];
  let count = 0;

  for (let char of s.toLowerCase()) {
    if (vowels.includes(char)) {
      count++;
    }
  }

  return count;
}



