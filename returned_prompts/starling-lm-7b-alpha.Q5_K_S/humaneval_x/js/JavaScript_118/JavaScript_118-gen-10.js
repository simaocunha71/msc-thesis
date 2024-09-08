  const vowel = ["a", "e", "i", "o", "u"];
  let result = "";
  let left = 0;
  let right = word.length - 1;

  while (left < right) {
    const c = word[left];
    const d = word[right];

    if (!vowel.includes(c) && !vowel.includes(d)) {
      while (!vowel.includes(word[right]) && right > 0) {
        right -= 1;
      }
      while (!vowel.includes(word[left]) && left < word.length - 1) {
        left += 1;
      }
    } else {
      break;
    }
  }

  if (left < word.length - 1) {
    result = word[left + 1];
  } else if (left > 0) {
    result = word[left - 1];
  }

  return result;
}



