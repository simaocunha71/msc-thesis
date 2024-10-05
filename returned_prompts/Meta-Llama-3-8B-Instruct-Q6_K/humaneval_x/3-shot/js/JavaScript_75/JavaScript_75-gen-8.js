  for (let i = 2; i < 100; i++) {
    for (let j = i; j < 100; j++) {
      for (let k = j; k < 100; k++) {
        if (i * j * k == a) {
          let flag = true;
          for (let l = 2; l * l <= i; l++) {
            if (i % l == 0) {
              flag = false;
              break;
            }
          }
          for (let l = 2; l * l <= j; l++) {
            if (j % l == 0) {
              flag = false;
              break;
            }
          }
          for (let l = 2; l * l <= k; l++) {
            if (k % l == 0) {
              flag = false;
              break;
            }
          }
          if (flag) {
            return true;
          }
        }
      }
    }
  }
  return false;
}
// The above code has a time complexity of O(n^3), which might be slow for large inputs.
// Here's an improved version with a time complexity of O(n^2):
function isMultiplyPrime(a) {
  for (let i = 2; i < 100; i++) {
    for (let j = i; j < 100; j++) {
      let product = i * j;
      let k = 2;
      while (product * k <= a) {
        if (product * k == a) {
          let flag = true;
          for (let l = 2; l * l <= i; l++) {
            if (i % l == 0) {
              flag = false;
              break;
            }
          }
          for (let l = 2; l * l <= j; l++) {
            if (j % l == 0) {
              flag = false;
              break;
            }
          }
          for (let l = 2; l * l <= k; l++) {
            if (k % l == 0) {
              flag = false;
              break;
            }
          }
          if (flag) {
            return true;
          }
        }
        k++;
      }
    }
  }
  return false;
}