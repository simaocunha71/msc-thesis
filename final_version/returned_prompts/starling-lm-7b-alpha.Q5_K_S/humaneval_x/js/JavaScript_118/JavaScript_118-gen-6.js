  let vowel = ["a", "e", "i", "o", "u"];
  let index = 0;
  let closest_vowel = "";
  while (index < word.length) {
    if (vowel.includes(word[index].toLowerCase())) {
      closest_vowel = word[index];
      break;
    }
    index += 1;
  }
  let left_index = index;
  let right_index = index;
  while (left_index > 0) {
    if (word[left_index - 1].match(/[^aeiou]/)) {
      if (closest_vowel == "") {
        closest_vowel = word[left_index - 1];
      } else if (word[left_index - 1].toLowerCase() != closest_vowel) {
        closest_vowel = word[left_index - 1];
      }
    }
    left_index -= 1;
  }
  while (right_index < word.length - 1) {
    if (word[right_index + 1].match(/[^aeiou]/)) {
      if (closest_vowel == "") {
        closest_vowel = word[right_index + 1];
      } else if (word[right_index + 1].toLowerCase() != closest_vowel) {
        closest_vowel = word[right_index + 1];
      }
    }
    right_index += 1;
  }
  return closest_vowel;
}



