  var vowels = ['a', 'e', 'i', 'o', 'u', 'y'];
  var vowels_count = 0;

  for (const c of s) {
    if (vowels.includes(c)) {
      vowels_count += 1;
    }
  }

  return vowels_count;
}



