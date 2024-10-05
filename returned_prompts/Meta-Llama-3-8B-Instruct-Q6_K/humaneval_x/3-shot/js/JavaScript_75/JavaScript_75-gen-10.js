  for (let i = 2; i <= a; i++) {
    let isPrime = true;
    for (let j = 2; j * j <= i; j++) {
      if (i % j == 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      for (let k = 2; k <= a; k++) {
        let isPrime2 = true;
        for (let l = 2; l * l <= k; l++) {
          if (k % l == 0) {
            isPrime2 = false;
            break;
          }
        }
        if (isPrime2) {
          for (let m = 2; m <= a; m++) {
            let isPrime3 = true;
            for (let n = 2; n * n <= m; n++) {
              if (m % n == 0) {
                isPrime3 = false;
                break;
              }
            }
            if (isPrime3) {
              if (i * k * m == a) {
                return true;
              }
            }
          }
        }
      }
    }
  }
  return false;
}