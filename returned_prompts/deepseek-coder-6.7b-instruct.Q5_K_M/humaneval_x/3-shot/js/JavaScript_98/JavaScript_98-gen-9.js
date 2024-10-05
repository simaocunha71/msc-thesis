  let count = 0;
  const vowels = 'AEIOU';
  
  for (let i = 0; i < s.length; i += 2) {
    if (vowels.includes(s[i])) {
      count++;
    }
  }
  
  return count;
}



