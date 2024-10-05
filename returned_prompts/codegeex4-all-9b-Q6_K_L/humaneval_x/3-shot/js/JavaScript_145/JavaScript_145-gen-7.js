  return nums.sort((a, b) => {
    var sumA = 0;
    var sumB = 0;

    for (const digit of a.toString()) {
      sumA += parseInt(digit);
    }

    for (const digit of b.toString()) {
      sumB += parseInt(digit);
    }

    if (sumA == sumB) {
      return nums.indexOf(a) - nums.indexOf(b);
    } else {
      return sumA - sumB;
    }
  });
}