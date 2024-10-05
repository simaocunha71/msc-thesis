  let result = '';
  for (let i = word.length - 1; i > 0; i--) {
    if ('AEIOUaeiou'.includes(word[i])) {
      let left = true;
      for (let j = i - 1; j >= 0; j--) {
        if (!'AEIOUaeiou'.includes(word[j])) {
          left = false;
          break;
        }
      }
      if (left) {
        result = word[i];
        break;
      }
    }
  }
  return result;
}