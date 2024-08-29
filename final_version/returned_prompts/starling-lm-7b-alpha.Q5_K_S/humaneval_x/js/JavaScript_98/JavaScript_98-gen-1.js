  const vowels = ['A', 'E', 'I', 'O', 'U'];
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === s[i].toUpperCase() && vowels.includes(s[i]) && i % 2 === 0) {
      count += 1;
    }
  }
  return count;
}



