  let max = 0;
  let result = "";

  for (let word of words) {
    let unique_chars = new Set(word).size;
    if (unique_chars > max || (unique_chars === max && word < result)) {
      max = unique_chars;
      result = word;
    }
  }

  return result;
}