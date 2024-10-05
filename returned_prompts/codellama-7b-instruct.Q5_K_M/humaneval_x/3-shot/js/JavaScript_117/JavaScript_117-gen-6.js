  if (s == "") return [];

  var result = [];
  var word = "";
  var count = 0;

  for (const c of s) {
    if (c == ' ') {
      if (count == n) {
        result.push(word);
      }
      count = 0;
      word = "";
    } else if (c != ' ') {
      if (isVowel(c) == false) {
        count += 1;
      }
      word += c;
    }
  }

  if (count == n) {
    result.push(word);
  }

  return result;
}



