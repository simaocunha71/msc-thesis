  let vowels = new Set(["a", "e", "i", "o", "u", "y"]);
  let count = 0;

  for (const c of s) {
    if (vowels.has(c)) {
      count += 1;
    }
  }

  return count;
}



