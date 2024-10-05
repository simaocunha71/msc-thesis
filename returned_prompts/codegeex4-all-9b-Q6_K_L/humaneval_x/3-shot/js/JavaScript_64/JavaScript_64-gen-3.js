  let vowels = ['a', 'e', 'i', 'o', 'u'];
  let count = 0;
  for (const c of s.toLowerCase()) {
    if (vowels.includes(c)) {
      count += 1;
    }
  }
  return count;
}



