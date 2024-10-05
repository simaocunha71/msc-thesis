  var vowels = "aeiouyAEIOUY";
  var count = 0;

  for (const c of s) {
    if (vowels.includes(c)) {
      count += 1;
    }
  }

  return count;
}



