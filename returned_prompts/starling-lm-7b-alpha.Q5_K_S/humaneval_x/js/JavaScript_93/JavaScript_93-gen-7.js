  let result = "";
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  for (const c of message) {
    let c_lower = c.toLowerCase();
    if (vowels.includes(c_lower)) {
      result += String.fromCharCode(c_lower.charCodeAt() + 2);
    } else if (vowels.includes(c)) {
      result += String.fromCharCode(c.charCodeAt() + 2);
    } else {
      result += c;
    }
  }
  return result.toUpperCase();
}



