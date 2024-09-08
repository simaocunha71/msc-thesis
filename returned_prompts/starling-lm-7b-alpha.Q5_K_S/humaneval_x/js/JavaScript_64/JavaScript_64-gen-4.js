  const vowels = ['a', 'e', 'i', 'o', 'u'];

  let count = 0;
  for (const c of s) {
    if (c == 'y' && s.length == 1) {
      count += 1;
    }
    if (vowels.includes(c)) {
      count += 1;
    }
  }

  return count;
}



