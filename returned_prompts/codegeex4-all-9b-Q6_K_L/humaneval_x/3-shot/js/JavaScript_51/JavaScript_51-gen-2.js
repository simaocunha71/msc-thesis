  var vowels = ['a', 'e', 'i', 'o', 'u'];
  var result = '';
  for (const c of text) {
    if (!vowels.includes(c.toLowerCase())) {
      result += c;
    }
  }
  return result;
}