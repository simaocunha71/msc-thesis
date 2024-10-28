  for (let i = 2; i < n; i++) {
    for (let j = 2; j < n; j++) {
      for (let k = 2; k < n; k++) {
        for (let l = 2; l < n; l++) {
          if (i + j + k + l === n) {
            return true;
          }
        }
      }
    }
  }
  return false;
}
// This code runs in O(n^3) time complexity and is not efficient for large inputs. A more efficient solution would be to use a different algorithm or data structure.