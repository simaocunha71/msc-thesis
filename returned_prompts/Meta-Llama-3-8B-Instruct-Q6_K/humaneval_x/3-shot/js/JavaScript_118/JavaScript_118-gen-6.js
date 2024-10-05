  for (let i = word.length - 1; i > 0; i--) {
    if ("AEIOUaeiou".includes(word[i])) {
      for (let j = i - 1; j >= 0; j--) {
        if (!"AEIOUaeiou".includes(word[j])) {
          return word[i];
        }
      }
    }
  }
  return "";
}