  var vowels = 'aeiou';
  var result = '';
  for (const c of text) {
    if (vowels.includes(c)) {
      continue;
    }
    result += c;
  }
  return result;
}



