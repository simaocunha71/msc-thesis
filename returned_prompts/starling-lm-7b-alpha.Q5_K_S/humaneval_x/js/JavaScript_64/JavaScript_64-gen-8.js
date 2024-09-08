  let vowels = ['a', 'e', 'i', 'o', 'u', 'y'];
  let result = 0;
  for (const c of s) {
    if (vowels.includes(c)) {
      result += 1;
    }
  }
  return result;
}



