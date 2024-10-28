  var vowels_count = 0;
  for (const c of s) {
    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || (c == 'y' && s.length - 1 == s.indexOf(c))) {
      vowels_count += 1;
    }
  }
  return vowels_count;
}



