  let vowels = ['a', 'e', 'i', 'o', 'u'];
  let encoded_message = '';
  for (let c of message) {
    let is_vowel = vowels.includes(c.toLowerCase());
    if (is_vowel) {
      encoded_message += String.fromCharCode(c.charCodeAt(0) + 2);
    } else {
      encoded_message += c.swapCase();
    }
  }
  return encoded_message;
}