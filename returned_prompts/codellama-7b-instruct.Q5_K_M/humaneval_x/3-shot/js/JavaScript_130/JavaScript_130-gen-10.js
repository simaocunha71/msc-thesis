  if (n == 1) {
    return [1, 3, 2, 8];
  } else {
    let result = [1, 3, 2, 8];
    let n_minus_1 = tri(n - 1);
    let n_minus_2 = tri(n - 2);
    let n_plus_1 = tri(n + 1);
    for (let i = 4; i <= n + 1; i++) {
      if (i % 2 == 0) {
        result.push(n_minus_1[i / 2] + n_minus_2[i / 2] + n_plus_1[i / 2]);
      } else {
        result.push(n_minus_1[i / 2] + n_minus_2[i / 2] + n_plus_1[i / 2]);
      }
    }
    return result;
  }
}



