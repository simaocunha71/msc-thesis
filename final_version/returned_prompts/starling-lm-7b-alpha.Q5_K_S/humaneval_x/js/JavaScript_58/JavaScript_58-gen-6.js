  const combined = [...new Set(l1.concat(l2))];
  const unique = [...new Set(combined)];
  const sorted = unique.sort();
  const result = [];

  for (let i = 0; i < sorted.length; i++) {
    if (l1.includes(sorted[i]) && l2.includes(sorted[i])) {
      result.push(sorted[i]);
    }
  }

  return result;
}



