  const vowels = 'aeiou';
  const vowel_shift = vowels.length;
  let result = '';

  for (const c of message) {
    let new_c = c;
    if (vowels.includes(c)) {
      const vowel_index = vowels.indexOf(c);
      new_c = vowels[(vowel_index + vowel_shift) % vowels.length];
    } else if (c.toLowerCase() == c) {
      new_c = c.toUpperCase();
    } else {
      new_c = c.toLowerCase();
    }
    result += new_c;
  }

  return result;
}



