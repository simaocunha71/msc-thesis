  let vowels = ['A', 'E', 'I', 'O', 'U'];
  let i = word.length - 1;
  let result = '';

  while (i >= 0) {
    if (vowels.includes(word[i])) {
      result = word[i];
      break;
    }
    if (word[i].match(/[A-Z]/i)) {
      i -= 1;
    } else {
      break;
    }
  }

  return result;
}



