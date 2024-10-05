  var sentences = S.split(/[.!?]/);
  var count = 0;
  for (const s of sentences) {
    if (s.trim().startsWith('I')) {
      count += 1;
    }
  }
  return count;
}



