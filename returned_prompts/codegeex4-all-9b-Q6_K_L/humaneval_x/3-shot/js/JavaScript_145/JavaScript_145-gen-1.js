  nums.sort((a, b) => {
    let sumA = 0;
    let sumB = 0;
    let tempA = a;
    let tempB = b;

    while (tempA >= 1) {
      sumA += tempA % 10;
      tempA = Math.floor(tempA / 10);
    }

    while (tempB >= 1) {
      sumB += tempB % 10;
      tempB = Math.floor(tempB / 10);
    }

    if (sumA == sumB) {
      return nums.indexOf(a) - nums.indexOf(b);
    } else {
      return sumA - sumB;
    }
  });

  return nums;
}