  let counts = {};
  let max_count = 0;
  for (const c of test.split(' ')) {
    counts[c] = (counts[c] || 0) + 1;
    max_count = Math.max(max_count, counts[c]);
  }

  let result = {};
  for (const c of Object.keys(counts)) {
    if (counts[c] === max_count) {
      result[c] = counts[c];
    }
  }

  return result;
}



