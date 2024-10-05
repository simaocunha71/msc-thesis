  let count = 0;
  let vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'Y', 'y'];
  for (let i = 0; i < s.length; i++) {
    if (vowels.includes(s[i])) {
      count += 1;
    }
  }
  return count;
}



