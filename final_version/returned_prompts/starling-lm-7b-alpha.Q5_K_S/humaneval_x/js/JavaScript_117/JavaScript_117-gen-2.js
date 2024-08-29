  let result = [];
  let vowels = ["a", "e", "i", "o", "u"];

  for (const word of s.split(' ')) {
    let count = 0;
    for (const letter of word) {
      if (!vowels.includes(letter.toLowerCase())) {
        count += 1;
      }
    }
    if (count == n) {
      result.push(word);
    }
  }

  return result;
}



