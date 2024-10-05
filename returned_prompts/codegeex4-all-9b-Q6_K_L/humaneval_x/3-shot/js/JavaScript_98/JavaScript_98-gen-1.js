  var count = 0;
  for (let i = 0; i < s.length; i++) {
    if (i % 2 == 0 && /[AEIOU]/i.test(s[i])) {
      count += 1;
    }
  }
  return count;
}



