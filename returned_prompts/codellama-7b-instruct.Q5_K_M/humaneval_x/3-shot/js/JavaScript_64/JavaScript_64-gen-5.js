  var vowels = "aeiouy";
  var count = 0;
  for (var i = 0; i < s.length; i++) {
    if (vowels.indexOf(s[i]) != -1) {
      count += 1;
    }
  }
  return count;
}



