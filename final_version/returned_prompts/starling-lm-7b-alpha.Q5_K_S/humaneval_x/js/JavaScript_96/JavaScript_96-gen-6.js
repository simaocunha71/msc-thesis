  if (n <= 2) {
    return [];
  } else {
    let result = [2];
    for (let i = 3; i < n; i++) {
      let is_prime = true;
      for (let j = 2; j < i; j++) {
        if (i % j === 0) {
          is_prime = false;
          break;
        }
      }
      if (is_prime) {
        result.push(i);
      }
    }
    return result;
  }
}



