  let vowels = ['a', 'e', 'i', 'o', 'u'];
  let consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'];

  let vowel_index = 0;
  let consonant_index = 0;
  let closest_vowel = '';

  for (let i = 0; i < word.length; i++) {
    let char = word[i];
    if (vowels.includes(char)) {
      vowel_index = i;
      closest_vowel = char;
    } else if (consonants.includes(char)) {
      consonant_index = i;
    }
  }

  if (vowel_index < consonant_index) {
    closest_vowel = word[vowel_index];
  } else if (vowel_index > consonant_index) {
    closest_vowel = word[consonant_index];
  }
  return closest_vowel;
}



