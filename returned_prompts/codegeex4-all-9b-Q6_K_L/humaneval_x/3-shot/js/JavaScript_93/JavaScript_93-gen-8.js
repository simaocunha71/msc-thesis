  const vowels = ['a', 'e', 'i', 'o', 'u'];
  let encoded_message = '';
  for (const c of message) {
    if (c == c.toLowerCase()) {
      if (vowels.includes(c)) {
        encoded_message += c.toUpperCase().charCodeAt(0) + 2;
      } else {
        encoded_message += c.toUpperCase();
      }
    } else {
      if (vowels.includes(c.toLowerCase())) {
        encoded_message += c.toLowerCase().charCodeAt(0) - 2;
      } else {
        encoded_message += c.toLowerCase();
      }
    }
  }

  return encoded_message;
}