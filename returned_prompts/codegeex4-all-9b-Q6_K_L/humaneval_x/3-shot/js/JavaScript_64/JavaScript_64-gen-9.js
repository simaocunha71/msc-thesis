  var vowels = ['a', 'e', 'i', 'o', 'u'];
  var count = 0;

  for (const c of s) {
    if (c == 'y' && s.length == 1) {
      count += 1;
    } else if (vowels.includes(c)) {
      count += 1;
    }
  }

  return count;
}