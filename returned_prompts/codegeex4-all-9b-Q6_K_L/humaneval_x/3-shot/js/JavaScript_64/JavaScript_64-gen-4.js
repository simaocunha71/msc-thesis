  var count = 0;
  const vowels = "aeiouAEIOU";
  for (const c of s) {
    if (vowels.includes(c)) {
      count += 1;
    }
  }
  return count;
}



