  let count = 0;
  const vowels = ['a', 'e', 'i', 'o', 'u', 'y'];

  for (let char of s.toLowerCase()) {
    if (vowels.includes(char)) count++;
  }

  return count;
}



