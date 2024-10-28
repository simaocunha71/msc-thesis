  const vowels = 'AEIOU';
  const word_upper = word.toUpperCase();
  const word_length = word.length;
  let closest_vowel = '';

  for (let i = 1; i < word_length - 1; i++) {
    const current_char = word_upper[i];
    const prev_char = word_upper[i - 1];
    const next_char = word_upper[i + 1];

    if (vowels.includes(current_char) && !vowels.includes(prev_char) && !vowels.includes(next_char)) {
      closest_vowel = current_char;
      break;
    }
  }

  return closest_vowel;
}