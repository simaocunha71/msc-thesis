  for (let i = 0; i < l.length; i++) {
    for (let j = i + 1; j < l.length; j++) {
      if (l[i] + l[j] === 0) {
        return true;
      }
    }
  }
  return false;
}  // O(n^2) time complexity, where n is the length of the list.



