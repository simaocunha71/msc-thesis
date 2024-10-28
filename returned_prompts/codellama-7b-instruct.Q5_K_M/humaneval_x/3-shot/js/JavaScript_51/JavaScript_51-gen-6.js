  var result = "";
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  for (const c of text) {
    if (!vowels.includes(c.toLowerCase())) {
      result += c;
    }
  }
  return result;
}



