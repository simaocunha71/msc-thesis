  let longest = null;
  for (const s of strings) {
    if (longest == null || s.length > longest.length) {
      longest = s;
    }
  }
  return longest;
}



