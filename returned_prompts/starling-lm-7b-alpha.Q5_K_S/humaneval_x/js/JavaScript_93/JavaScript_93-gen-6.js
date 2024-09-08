  const lowercase = message.toLowerCase();
  const uppercase = message.toUpperCase();
  const vowels = 'aeiou';

  let result = '';
  for (const c of lowercase) {
    if (vowels.includes(c)) {
      result += String.fromCharCode(
        (c === 'a' ? 97 : (c === 'e' ? 101 : (c === 'i' ? 105 : (c === 'o' ? 111 : 117)))));
    } else {
      result += c;
    }
  }

  for (const c of uppercase) {
    if (vowels.includes(c)) {
      result += String.fromCharCode(
        (c === 'A' ? 65 : (c === 'E' ? 69 : (c === 'I' ? 73 : (c === 'O' ? 79 : 85)))));
    } else {
      result += c;
    }
  }

  return result;
}



