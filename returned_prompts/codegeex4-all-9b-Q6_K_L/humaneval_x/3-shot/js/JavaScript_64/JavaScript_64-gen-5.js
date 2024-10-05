  var count = 0;
  var vowels = ["a", "e", "i", "o", "u"];
  for (var i = 0; i < s.length; i++) {
    if (vowels.includes(s[i].toLowerCase())) {
      count++;
    }
  }
  if (s[s.length - 1].toLowerCase() == 'y') {
    count++;
  }
  return count;
}