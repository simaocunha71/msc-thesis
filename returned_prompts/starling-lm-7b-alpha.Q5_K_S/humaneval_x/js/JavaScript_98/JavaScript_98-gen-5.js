  let vowels = ['A','E','I','O','U'];
  let result = 0;
  for (let i = 0; i < s.length; i += 2) {
    if (vowels.includes(s[i].toUpperCase())) {
      result += 1;
    }
  }
  return result;
}



