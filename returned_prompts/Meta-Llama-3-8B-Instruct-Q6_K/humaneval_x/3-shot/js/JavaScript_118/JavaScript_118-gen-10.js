  let result = "";
  for (let i = word.length - 1; i > 0; i--) {
    if (["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"].includes(word[i])) {
      if (result !== "") {
        return result;
      } else {
        result = word[i];
      }
    }
  }
  return result;
}