  if (s.length < 3) {
    return false;
  }

  const letters = {
    'a': true,
    'b': true,
    'c': true,
    'd': true,
    'e': true,
    'f': true,
    'g': true,
    'h': true,
    'i': true,
    'j': true,
    'k': true,
    'l': true,
    'm': true,
    'n': true,
    'o': true,
    'p': true,
    'q': true,
    'r': true,
    's': true,
    't': true,
    'u': true,
    'v': true,
    'w': true,
    'x': true,
    'y': true,
    'z': true
  };

  for (let i = 0; i < s.length - 2; i++) {
    const letter_1 = s[i];
    const letter_2 = s[i + 1];
    const letter_3 = s[i + 2];

    if (letters[letter_1] && letters[letter_2] && letters[letter_3]) {
      letters[letter_1] = false;
      letters[letter_2] = false;
      letters[letter_3] = false;
    } else {
      return false;
    }
  }

  return true;
}



