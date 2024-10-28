  let letter_counts = {};
  test.split(' ').forEach((letter) => {
    if (letter in letter_counts) {
      letter_counts[letter]++;
    } else {
      letter_counts[letter] = 1;
    }
  });
  let max_count = Math.max(...Object.values(letter_counts));
  let max_letters = Object.keys(letter_counts).filter((letter) => letter_counts[letter] === max_count);
  return Object.fromEntries(max_letters.map((letter) => [letter, max_count]));
} 



