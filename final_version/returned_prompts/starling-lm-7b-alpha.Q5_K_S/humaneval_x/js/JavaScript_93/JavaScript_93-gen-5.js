  let result = "";
  const vowels = "aeiou";
  const vowel_index = vowels.indexOf(message[0].toLowerCase());
  const letter_index = message[0].toLowerCase() - 'a';

  for (const c of message) {
    if (vowels.indexOf(c.toLowerCase()) >= 0) {
      result += String.fromCharCode((vowel_index + 2) % 26 + 'a');
    } else {
      result += String.fromCharCode((letter_index + 1) % 26 + 'a');
    }
  }

  return result;
}



