  let vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
  let result = '';
  for (let i = word.length - 2; i >= 0; i -= 1) {
    if (vowels.includes(word[i]) && !vowels.includes(word[i + 1])) {
      result = word[i];
      break;
    }
  }
  return result;
}



