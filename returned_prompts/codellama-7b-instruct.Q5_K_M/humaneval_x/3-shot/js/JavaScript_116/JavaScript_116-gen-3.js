  return arr.sort((a, b) => {
    const binary_a = a.toString(2);
    const binary_b = b.toString(2);
    const ones_a = binary_a.split('1').length - 1;
    const ones_b = binary_b.split('1').length - 1;
    if (ones_a === ones_b) {
      return a - b;
    }
    return ones_a - ones_b;
  });
}



