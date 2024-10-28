  const vowels = ['a', 'e', 'i', 'o', 'u'];

  let result = '';

  for (const c of message) {
    let lower = c.toLowerCase();
    if (lower == lower.toUpperCase()) {
      if (vowels.includes(lower)) {
        result += String.fromCharCode(c.charCodeAt(0) + 2);
      } else {
        result += c.toUpperCase() == c ? c.toLowerCase() : c.toUpperCase();
      }
    } else {
      result += c;
    }
  }

  return result;
}



