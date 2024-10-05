  for (let i = 0; i < l.length; i++) {
    for (let j = i + 1; j < l.length; j++) {
      for (let k = j + 1; k < l.length; k++) {
        if (l[i] + l[j] + l[k] === 0) {
          return true;
        }
      }
    }
  }
  return false;
}  // O(n^3) time complexity, not efficient for large inputs. Better solution is to sort the array first and then use two pointers.  // O(n log n) time complexity.