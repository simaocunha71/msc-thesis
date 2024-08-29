  if (s.length < 3) return false;
  var char_set = new Set();
  for (let i = 0; i < 3; i++) {
    char_set.add(s[i]);
  }
  for (let i = 3; i < s.length; i++) {
    char_set.add(s[i]);
    if (char_set.size > 3) return false;
  }
  return true;
}



