  for (let i = 0; i < 100; i++) {
    if (i % 2 == 0) {
      for (let j = i + 1; j < 100; j++) {
        if (j % 2 == 0) {
          for (let k = j + 1; k < 100; k++) {
            if (k % 2 == 0) {
              for (let l = k + 1; l < 100; l++) {
                if (l % 2 == 0) {
                  if (i + j + k + l == n) {
                    return true;
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  return false;
}



