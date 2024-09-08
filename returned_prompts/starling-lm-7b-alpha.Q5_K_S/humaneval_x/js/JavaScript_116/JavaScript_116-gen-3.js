  const binary_count = (num) => {
    let result = 0;
    while (num > 0) {
      result += num & 1;
      num >>= 1;
    }
    return result;
  };

  return arr.sort((a, b) => {
    const count_a = binary_count(a);
    const count_b = binary_count(b);
    if (count_a < count_b) {
      return -1;
    } else if (count_a > count_b) {
      return 1;
    } else if (a < b) {
      return -1;
    } else {
      return 1;
    }
  });
}



